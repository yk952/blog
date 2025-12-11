<template>
  <div class="comment-list">
    <h3>评论区（{{ comments.length }}条）</h3>
    <!-- 空评论提示 -->
    <div v-if="comments.length === 0 && !loading" class="empty">暂无评论，快来抢沙发～</div>
    <!-- 加载中 -->
    <div v-if="loading" class="loading">加载评论中...</div>
    <!-- 评论列表 -->
    <div v-for="comment in comments" :key="comment.id" class="comment-item">
      <div class="author">{{ comment.author.username }}</div>
      <div class="content">{{ comment.content }}</div>
      <div class="time">{{ formatTime(comment.create_time) }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { getComments, type Comment } from '../api/comment';
import { ElMessage } from 'element-plus';

// 接收父组件传的文章ID
const props = defineProps<{
  articleId: number;
}>();

// 响应式数据
const comments = ref<Comment[]>([]);
const loading = ref(false);

// 格式化时间（简化版）
const formatTime = (timeStr: string) => {
  return new Date(timeStr).toLocaleString();
};

// 加载评论
const fetchComments = async () => {
  if (!props.articleId) return;
  loading.value = true;
  try {
    const res = await getComments(props.articleId);
    comments.value = res;
  } catch (err: any) {
    ElMessage.error(err.message);
  } finally {
    loading.value = false;
  }
};

// 监听文章ID变化，重新加载评论
watch(() => props.articleId, fetchComments, { immediate: true });

// 暴露刷新方法（供父组件调用）
defineExpose({
  refresh: fetchComments
});
</script>

<style scoped>
.comment-list {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #eee;
}
.comment-item {
  padding: 10px 0;
  border-bottom: 1px solid #f5f5f5;
}
.author {
  font-weight: 500;
  color: #42b983;
  margin-bottom: 5px;
}
.content {
  line-height: 1.6;
  margin-bottom: 5px;
}
.time {
  font-size: 12px;
  color: #999;
}
.empty, .loading {
  color: #999;
  text-align: center;
  padding: 20px;
}
</style>