import service from './user';

// 核心类型定义
export interface Category {
  id: number;
  name: string;
  description?: string;
  create_time?: string;
  update_time?: string;
}

export interface CategoryCreateParams {
  name: string;
  description?: string;
}

// 类型守卫
function isCategory(data: unknown): data is Category {
  return (
    typeof data === 'object' &&
    data !== null &&
    'id' in data && typeof (data as Category).id === 'number' &&
    'name' in data && typeof (data as Category).name === 'string'
  );
}

function isCategoryArray(data: unknown): data is Category[] {
  return Array.isArray(data) && data.every(item => isCategory(item));
}

/**
 * 获取分类列表
 * @returns 分类数组
 */
export function getCategories(): Promise<Category[]> {
  console.log('[分类接口] 请求分类列表');
  return service.get('/categories/').then(response => {
    if (!isCategoryArray(response)) throw new Error('分类列表数据格式错误');
    return response;
  }).catch(err => {
    const errorMsg = err.response?.data?.non_field_errors?.[0] || err.message || '获取分类列表失败';
    console.error('[分类接口] 失败：', errorMsg);
    throw new Error(`[分类列表] ${errorMsg}`);
  });
}

/**
 * 获取单个分类详情
 * @param id 分类ID
 * @returns 分类详情
 */
export function getCategory(id: number | string): Promise<Category> {
  const categoryId = Number(id);
  if (isNaN(categoryId) || categoryId <= 0) throw new Error('分类ID必须是正整数');

  console.log('[分类接口] 请求分类详情，ID：', categoryId);
  return service.get(`/categories/${categoryId}/`).then(response => {
    if (!isCategory(response)) throw new Error('分类详情数据格式错误');
    return response;
  }).catch(err => {
    const errorMsg = err.response?.data?.non_field_errors?.[0] || err.message || '获取分类详情失败';
    console.error('[分类接口] 失败：', errorMsg);
    throw new Error(`[分类${categoryId}] ${errorMsg}`);
  });
}

/**
 * 新增分类
 * @param data 分类创建参数
 * @returns 创建后的分类
 */
export function postCategory(data: CategoryCreateParams): Promise<Category> {
  const trimmedName = data.name.trim();
  if (!trimmedName) throw new Error('分类名称不能为空');

  console.log('[分类接口] 创建分类，名称：', trimmedName);
  return service.post('/categories/', {
    ...data,
    name: trimmedName
  }).then(response => {
    if (!isCategory(response)) throw new Error('新增分类数据格式错误');
    return response;
  }).catch(err => {
    const errorMsg = err.response?.data?.name?.[0] || err.message || '新增分类失败';
    console.error('[分类接口] 失败：', errorMsg);
    throw new Error(`[新增分类] ${errorMsg}`);
  });
}