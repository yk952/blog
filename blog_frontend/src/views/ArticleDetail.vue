<template>
  <div class="detail-container">
    <h1 class="article-title">测试文章 {{ articleId }} 标题</h1> 
    <div class="article-content">
      <p>这是文章 {{ articleId }} 的正文内容。</p>
      <p>这里是一些示例文本，用于展示文章详情页的布局效果。实际应用中，这里会显示从服务器获取的文章内容。</p>
      <p>段落1：Vue 是一套用于构建用户界面的渐进式框架，易学易用，性能出色。</p>
      <p>段落2：本文主要介绍了 Vue 路由的基本使用方法，包括路由配置、页面跳转和动态路由参数等内容。</p>
    </div>
    <div class="comments-section">
      <h2>评论区</h2>
      <div class="comment-list">
        <div class="comment-item">
          <div class="comment-author">用户A</div>
          <div class="comment-content">这篇文章很有帮助，谢谢分享！</div>
        </div>
        <div class="comment-item">
          <div class="comment-author">用户B</div>
          <div class="comment-content">请问动态路由参数怎么获取？</div>
        </div>
      </div>
    </div>
  </div>
  <div class="article-detail">
    <div class="loading" v-if="loading">
      正在加载内容
    </div>
    <div class="error" v-if="error">
      <p>加载文章详情失败：{{ error }}</p>
      <button @click="fetchArticle">重试</button>
      <router-link to="/" class="back-home">返回首页</router-link>
    </div>
    <div class="content" v-if="article && !loading && !error">
      <h1>{{ article.title }}</h1>
      <p class="meta-info">发布于：{{ article.create_time }}</p>
      <div class="article-content">
        <p v-html="article.content"></p>
      </div>
      <hr>
      <router-link to="/" class="back-link">返回文章列表</router-link>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { getArticle } from '@/api/article'
// 组合式 API 中用 ref 声明响应式变量（替代选项式的 data）
import { ref } from 'vue'

// 1. 声明响应式变量
const article = ref(null)
const loading = ref(false)
const error = ref(null)

// 2. 获取路由信息
const route = useRoute()
const articleId = route.params.id

// 3. 定义请求函数（替代选项式的 methods）
const fetchArticle = async () => {
  loading.value = true
  error.value = null
  try {
    // 调用接口并赋值（组合式中用 .value 访问 ref 变量）
    article.value = await getArticle(articleId)
  } catch (err) {
    error.value = err.message || '加载失败'
  } finally {
    loading.value = false
  }
}

// 4. 组件创建时执行（替代选项式的 created）
fetchArticle()
</script>

<style scoped>
.detail-container {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 2rem;
}

.article-title {
  color: var(--yk-fontcolor); 
  text-align: center;
  margin: 2rem 0;
}

.article-content {
  line-height: 1.8;
  color: var(--yk-fontcolor); 
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: var(--style-border);
}

.comments-section {
  margin-top: 2rem;
}
.comments-section h2 {
  color: var(--yk-fontcolor);
  border-bottom: var(--style-border);
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
}

.comment-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.comment-item {
  padding: 1rem;
  background-color: var(--yk-card-bg);
  border: var(--style-border);
  border-radius: 6px;
  transition: border-color 0.3s;
}
.comment-item:hover {
  border-color: var(--yk-main-op);
}

.comment-author {
  font-weight: bold;
  color: var(--yk-fontcolor); 
  margin-bottom: 0.5rem;
}

.comment-content {
  color: var(--yk-secondtext); 
}
</style>