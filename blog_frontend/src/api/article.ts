import service from './user';

// 核心类型定义（保留，后续微调）
export interface Article {
  id: number;
  title: string;
  content: string;
  author: {
    id: number;
    username: string;
  };
  category?: {
    id: number;
    name: string;
  } | null; // 允许category为null（后端可能返回null）
  create_time: string;
  update_time?: string;
}

export interface ArticleCreateParams {
  title: string;
  content: string;
  category?: number; // 关键：改为category（后端接收category，不是category_id）
  tags?: number[];
}

// 类型守卫：增强校验逻辑（后续修改）
function isArticle(data: unknown): data is Article {
  return (
    typeof data === 'object' &&
    data !== null &&
    'id' in data && typeof (data as Article).id === 'number' &&
    'title' in data && typeof (data as Article).title === 'string' &&
    'content' in data && typeof (data as Article).content === 'string' && // 新增：校验content
    'author' in data && typeof (data as Article).author === 'object' &&
    (data as Article).author !== null && // 确保author不是null
    'id' in (data as Article).author && typeof (data as Article).author.id === 'number' && // 校验author.id
    'create_time' in data && typeof (data as Article).create_time === 'string' // 新增：校验create_time
  );
}

function isArticleArray(data: unknown): data is Article[] {
  return Array.isArray(data) && data.every(item => isArticle(item));
}

/**
 * 获取文章列表（支持筛选参数，向后兼容无参调用）
 * @param params 筛选参数（如 { category: 1 }），可选
 * @returns 文章列表数组
 */
export function getArticles(params: Record<string, any> = {}): Promise<Article[]> {
  console.log('[文章接口] 请求文章列表，筛选参数：', params);
  return service.get('/articles/', {  
    params: params 
  }).then(response => {
    // ========== 新增：打印原始数据（调试核心） ==========
    console.log('[文章列表] 后端返回原始数据：', response); 
    // ========== 临时注释类型守卫（先看数据是否正常） ==========
    // if (!isArticleArray(response)) {
    //   throw new Error('文章列表数据格式错误');
    // }
    return response as Article[]; // 临时强制类型转换
  }).catch(err => {
    const errorMsg = err.message || '获取文章列表失败';
    console.error('[文章接口] 失败：', errorMsg);
    throw new Error(`[文章列表] ${errorMsg}`);
  });
}

// 以下函数暂时不变（先调试列表接口）
/**
 * 获取单篇文章详情
 * @param id 文章ID（必填）
 * @returns 单篇文章详情
 */
export function getArticle(id: number | string): Promise<Article> {
  const articleId = Number(id);
  if (isNaN(articleId) || articleId <= 0) {
    throw new Error('文章ID必须是正整数');
  }

  console.log('[文章接口] 请求文章详情，ID：', articleId);
  return service.get(`/articles/${articleId}/`).then(response => {  
    // ========== 新增：打印详情原始数据 ==========
    console.log(`[文章${articleId}] 后端返回原始数据：`, response);
    // if (!isArticle(response)) {
    //   throw new Error('文章详情数据格式错误');
    // }
    return response as Article;
  }).catch(err => {
    const errorMsg = err.message || '获取文章详情失败';
    console.error('[文章接口] 失败：', errorMsg);
    throw new Error(`[文章${articleId}] ${errorMsg}`);
  });
}

/**
 * 新增文章（核心修改：字段名 category_id → category）
 * @param data 文章创建参数
 * @returns 创建后的文章完整信息
 */
export function postArticle(data: ArticleCreateParams): Promise<Article> {
  const trimmedTitle = data.title.trim();
  const trimmedContent = data.content.trim();
  if (!trimmedTitle) throw new Error('文章标题不能为空');
  if (!trimmedContent) throw new Error('文章内容不能为空');

  console.log('[文章接口] 创建文章，标题：', trimmedTitle);
  return service.post('/articles/', {  
    ...data,
    title: trimmedTitle,
    content: trimmedContent,
    // 移除category_id，改用category（匹配后端序列化器字段）
    category: data.category // 后端接收category（ID），不是category_id
  }).then(response => {
    console.log('[新增文章] 后端返回数据：', response); // 新增：打印返回数据
    // if (!isArticle(response)) throw new Error('新增文章数据格式错误');
    return response;
  }).catch(err => {
    const errorMsg = err.response?.data?.non_field_errors?.[0] || err.message || '新增文章失败';
    console.error('[文章接口] 失败：', errorMsg);
    throw new Error(`[新增文章] ${errorMsg}`);
  });
}

/**
 * 编辑文章（同步修改category_id → category）
 * @param id 文章ID
 * @param data 编辑参数
 * @returns 编辑后的文章信息
 */
export function putArticle(id: number | string, data: Partial<ArticleCreateParams>): Promise<Article> {
  const articleId = Number(id);
  if (isNaN(articleId) || articleId <= 0) throw new Error('文章ID必须是正整数');

  if (data.title) {
    const trimmedTitle = data.title.trim();
    if (!trimmedTitle) throw new Error('文章标题不能为空');
    data.title = trimmedTitle;
  }

  console.log('[文章接口] 编辑文章，ID：', articleId);
  return service.put(`/articles/${articleId}/`, {
    ...data,
    category: data.category // 同步改为category
  }).then(response => {
    console.log(`[编辑文章${articleId}] 后端返回数据：`, response); // 新增：打印返回数据
    // if (!isArticle(response)) throw new Error('编辑文章数据格式错误');
    return response;
  }).catch(err => {
    const errorMsg = err.response?.data?.non_field_errors?.[0] || err.message || '编辑文章失败';
    console.error('[文章接口] 失败：', errorMsg);
    throw new Error(`[编辑文章${articleId}] ${errorMsg}`);
  });
}