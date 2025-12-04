<template>
  <div class="home-container">
    <h1>最新文章</h1>
    
    <!-- 加载状态 -->
    <div class="loading" v-if="loading">
      正在努力加载文章
    </div>
    
    <!-- 错误提示 -->
    <div class="error" v-if="error">
      <p>-_-:{{ error }}</p>
      <button @click="fetchArticles">重试</button>
    </div>
    
    <!-- 文章列表 -->
    <div class="article-list" v-if="articles.length>0">
      <div class="article-item" v-for="article in articles" :key="article.id">
        <router-link :to="'/article/' + article.id" class="article-title">{{ article.title }}</router-link>
        <p class="article-desc">{{ article.content }}</p>
        <div class="article-meta">发布时间：{{ article.create_time }}</div>
      </div>
    </div>
    
    <!-- 无文章提示 -->
    <div class="no-articles" v-if="articles.length === 0 && !loading && !error">
      <p>暂无文章</p>
    </div>
  </div>
</template>

<script setup>
import { getArticles } from '@/api/article'
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

console.log("首页文件已经启动了！");

const articles = ref([])
const loading = ref(false)
const error = ref(null)

async function fetchArticles() {
  console.log("开始尝试加载文章了！");
  loading.value = true
  try {
    const response = await getArticles() // 规范变量名
    console.log("后端返回的数据：", response);
    articles.value = response.data || []; // 兼容接口返回格式
  } catch (err) {
    console.log("加载失败了：", err);
    // 更具体的错误信息
    error.value = err.response?.data?.message || "加载文章失败，请稍后重试"
  } finally {
    loading.value = false
  }
}

// 组件启动时自动加载
fetchArticles()
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}

h1 {
  color: var(--heo-fontcolor);
  margin-bottom: 2rem;
  border-bottom: 2px solid var(--heo-main);
  padding-bottom: 0.5rem;
}

.article-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.article-item {
  padding: 1.5rem;
  border: var(--style-border);
  border-radius: 8px;
  background: var(--heo-card-bg);
  box-shadow: var(--heo-card-box-shadow);
  transition: all 0.3s;
}
.article-item:hover {
  box-shadow: var(--heo-card-hover-box-shadow);
  border-color: var(--heo-main-op);
}

.article-title {
  font-size: 1.5rem;
  color: var(--heo-fontcolor);
  text-decoration: none;
  margin-bottom: 1rem;
  display: block;
  transition: color 0.3s;
}
.article-title:hover {
  color: var(--heo-hovertext);
}

.article-desc {
  color: var(--heo-secondtext);
  line-height: 1.6;
  margin: 1rem 0;
}

.article-meta {
  color: var(--heo-secondtext);
  font-size: 0.9rem;
}

/* 加载和错误样式可补充 */
.loading {
  color: var(--heo-secondtext);
  padding: 2rem;
  text-align: center;
}

.error {
  color: #ff4d4f; /* 错误色 */
  padding: 2rem;
  text-align: center;
}

.error button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  background: var(--heo-main);
  color: white;
  cursor: pointer;
}

.no-articles {
  color: var(--heo-secondtext);
  padding: 2rem;
  text-align: center;
}
</style>