<template>
  <div class="home-container">
    <h1>最新文章</h1>
    <div class="article-list">
      <div class="article-item">
        <router-link to="/article/1" class="article-title">创建者</router-link>
        <p class="article-desc">yk</p>
        <div class="article-meta">发布时间：2025-11-17</div>
      </div>

      <div class="article-item">
        <router-link to="/article/2" class="article-title">内容</router-link>
        <p class="article-desc">blog</p>
        <div class="article-meta">发布时间：2025-11-17</div>
      </div>
    </div>
  </div>
  <div class="home-page">
    <h2>文章列表</h2>
    <div class="loading" v-if="loading">
      正在努力加载文章
    </div>
    <div class="error" v-if="error">
      <p>-_-:{{ error }}</p>
      <button @click="fetchArticles">重试</button>
    </div>
    <div class="article-list" v-if="articles.length>0">
      <div class="article-item" v-for="article in articles" :key="article.id">
        <router-link :to="'/article/' + article.id" class="article-title">{{ article.title }}</router-link>
        <p class="article-desc">{{ article.content }}</p>
        <div class="article-meta">发布时间：{{ article.create_time }}</div>
      </div>
    </div>
    <div class="no-articles" v-if="articles.length === 0 && !loading && !error">
      <p>暂无文章</p>
    </div>
  </div>
</template>

<script setup>
import { getArticles } from '@/api/article'
import { ref } from 'vue'
import { RouterLink } from 'vue-router' // 若用了<RouterLink>需要导入

// 确认文件运行的日志
console.log("首页文件已经启动了！");

// 组合式API的响应式变量（替代选项式的data）
const articles = ref([])
const loading = ref(false)
const error = ref(null)

// 加载文章的函数（替代选项式的methods）
async function fetchArticles() {
  console.log("开始尝试加载文章了！");
  loading.value = true
  try {
    const 后端数据 = await getArticles()
    console.log("后端给的数据：", 后端数据);
    articles.value = 后端数据
  } catch (err) {
    console.log("加载失败了：", err);
    error.value = "加载失败"
  } finally {
    loading.value = false
  }
}

// 组件启动时自动加载（替代选项式的created）
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
</style>