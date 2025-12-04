<!-- src/views/NotFound.vue -->
<template>
  <div class="not-found-container">
    <h1 class="not-found-code">404</h1>
    <p class="not-found-desc">页面不存在或已被删除</p>
    <!-- 跳转回首页的链接 -->
    <router-link to="/" class="back-home-btn">返回首页</router-link>
  </div>
</template>

<script setup>
// 纯 JS 组件，无需额外逻辑
</script>

<style scoped>
.not-found-container {
  max-width: 1200px;
  margin: 5rem auto;
  padding: 0 2rem;
  text-align: center;
}

.not-found-code {
  font-size: 5rem;
  color: #ff4d4f;
  margin-bottom: 1rem;
  font-weight: bold;
}

.not-found-desc {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 2rem;
}

.back-home-btn {
  display: inline-block;
  padding: 0.8rem 1.6rem;
  background: #42b983;
  color: white;
  border-radius: 6px;
  text-decoration: none;
  transition: background 0.3s;
}

.back-home-btn:hover {
  background: #359469;
}
</style>