import service from './user';

// 评论类型定义
export interface Comment {
  id: number;
  article: number; // 文章ID
  author: {
    id: number;
    username: string;
  };
  content: string;
  create_time: string;
}

// 新增评论参数
export interface CommentCreateParams {
  article: number; // 关联文章ID
  content: string; // 评论内容
}

// 类型守卫：校验评论数据
function isComment(data: unknown): data is Comment {
  return (
    typeof data === 'object' &&
    data !== null &&
    'id' in data && typeof (data as Comment).id === 'number' &&
    'author' in data && typeof (data as Comment).author === 'object'
  );
}

function isCommentArray(data: unknown): data is Comment[] {
  return Array.isArray(data) && data.every(isComment);
}

// 获取评论列表（按文章ID筛选）
export async function getComments(articleId: number): Promise<Comment[]> {
  try {
    const response = await service.get('/comments/', {
      params: { article_id: articleId } // 传递文章ID过滤
    });
    if (!isCommentArray(response)) {
      throw new Error('评论列表数据格式错误');
    }
    return response;
  } catch (err: any) {
    const msg = err.response?.data?.non_field_errors?.[0] || '获取评论失败';
    throw new Error(`[评论列表] ${msg}`);
  }
}

// 提交评论
export async function postComment(data: CommentCreateParams): Promise<Comment> {
  // 前端校验
  if (!data.article || !data.content.trim()) {
    throw new Error('评论内容不能为空');
  }
  try {
    const response = await service.post('/comments/', {
      article: data.article,
      content: data.content.trim()
    });
    if (!isComment(response)) {
      throw new Error('提交评论返回数据格式错误');
    }
    return response;
  } catch (err: any) {
    const msg = err.response?.data?.content?.[0] || err.message || '提交评论失败';
    throw new Error(`[提交评论] ${msg}`);
  }
}

export type { CommentCreateParams };