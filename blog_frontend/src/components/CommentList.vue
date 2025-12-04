<template>
  <div class="comment-list">
    <h3>评论区（{{ comments.length }}条）</h3>
    <div class="comment-item" v-for="comment in comments" :key="comment.id">
      <div class="comment-header">
        <span class="username">{{ comment.username }}</span>
        <span class="time">{{ formatTime(comment.create_time) }}</span>
      </div>
      <div class="comment-content">{{ comment.content }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'

// 接收父组件传递的评论列表
const props = defineProps({
  comments: {
    type: Array,
    default: () => []
  }
})

// 时间格式化
const formatTime = (timeStr) => {
  const date = new Date(timeStr)
  return date.toLocaleString()  // 本地时间格式
}
</script>

<style scoped>
.comment-list {
  margin-top: 30px;
}
.comment-item {
  padding: 15px 0;
  border-bottom: 1px dashed #eee;
}
.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  color: #666;
}
.username {
  font-weight: bold;
  color: #42b983;
}
.comment-content {
  line-height: 1.6;
}
</style>