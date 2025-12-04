<template>
  <div class="detail-container">
    <!-- 加载状态 -->
    <div class="loading" v-if="loading">
      正在加载内容
    </div>

    <!-- 错误状态 -->
    <div class="error" v-if="error && !loading">
      <p>加载文章详情失败：{{ error }}</p>
      <button @click="fetchArticle">重试</button>
      <router-link to="/" class="back-home">返回首页</router-link>
    </div>

    <!-- 文章详情 + 评论区（加载成功且无错误） -->
    <div class="content" v-if="article && !loading && !error">
      <!-- 文章主体 -->
      <h1 class="article-title">{{ article.title }}</h1>
      <p class="meta-info">
        作者：{{ article.author_name }} | 
        分类：{{ article.category_name }} | 
        发布时间：{{ formatTime(article.create_time) }}
      </p>
      <div class="article-content" v-html="article.content"></div>

      <hr>

      <!-- 评论表单 -->
      <div class="comment-form" v-if="hasLogin">
        <h3>发表评论</h3>
        <textarea 
          v-model="commentContent" 
          rows="4" 
          placeholder="请输入评论内容"
          required
        ></textarea>
        <button @click="submitComment" class="submit-comment-btn">提交评论</button>
      </div>
      <div class="login-tip" v-else>
        <router-link to="/login">请登录后发表评论</router-link>
      </div>

      <!-- 评论列表 -->
      <div class="comments-section">
        <CommentList :comments="comments" />
      </div>

      <router-link to="/" class="back-link">返回文章列表</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { ElMessage } from 'element-plus'
import { getArticle } from '@/api/article'
import CommentList from '@/components/CommentList.vue' // 导入评论列表组件

// 1. 响应式变量声明
const article = ref(null)
const loading = ref(false)
const error = ref(null)
const articleId = ref('')
const commentContent = ref('') // 评论输入内容
const comments = ref([]) // 评论列表数据
const hasLogin = !!localStorage.getItem('token') // 是否登录（通过token判断）

// 2. 路由参数获取
const route = useRoute()

// 3. 时间格式化函数
const formatTime = (timeStr) => {
  if (!timeStr) return ''
  const date = new Date(timeStr)
  return date.toLocaleString() // 格式：2025/12/3 15:30:00（根据本地时间适配）
}

// 4. 获取文章详情（保留原有逻辑）
const fetchArticle = async () => {
  loading.value = true
  error.value = null
  articleId.value = route.params.id // 从路由获取文章ID
  try {
    article.value = await getArticle(articleId.value)
  } catch (err) {
    error.value = err.message || '加载失败'
    ElMessage.error('获取文章详情失败')
  } finally {
    loading.value = false
  }
}

// 5. 获取文章对应的评论
const getComments = async () => {
  if (!articleId.value) return
  try {
    const res = await axios.get(`http://localhost:8000/api/comments/?article_id=${articleId.value}`)
    comments.value = res.data // 存入评论列表
  } catch (err) {
    ElMessage.error('获取评论失败')
    console.error(err)
  }
}

// 6. 提交评论
const submitComment = async () => {
  // 表单验证
  if (!commentContent.value.trim()) {
    ElMessage.warning('评论内容不能为空')
    return
  }

  try {
    // 调用评论提交接口
    await axios.post('http://localhost:8000/api/comments/', {
      article: articleId.value, // 关联当前文章ID
      content: commentContent.value.trim() // 评论内容
    })
    ElMessage.success('评论成功！')
    commentContent.value = '' // 清空输入框
    getComments() // 刷新评论列表
  } catch (err) {
    ElMessage.error('评论失败，请重试')
    console.error(err)
  }
}

// 7. 组件挂载时加载文章和评论
onMounted(() => {
  fetchArticle() // 加载文章详情
  articleId.value = route.params.id // 提前获取文章ID，确保评论能加载
  setTimeout(getComments, 300) // 延迟一小段时间，确保articleId已获取
})
</script>

<style scoped>
.detail-container {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 2rem;
}

/* 加载状态 */
.loading {
  text-align: center;
  padding: 5rem 0;
  color: #666;
  font-size: 1.2rem;
}

/* 错误状态 */
.error {
  text-align: center;
  padding: 5rem 0;
  color: #ff4d4f;
}
.error .back-home {
  display: inline-block;
  margin-left: 1rem;
  color: #42b983;
  text-decoration: none;
}
.error button {
  padding: 8px 16px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* 文章内容 */
.content {
  padding: 2rem 0;
}
.article-title {
  color: var(--yk-fontcolor);
  text-align: center;
  margin: 2rem 0;
}
.meta-info {
  color: #666;
  margin: 1rem 0;
  border-bottom: var(--style-border);
  padding-bottom: 1rem;
}
.article-content {
  line-height: 1.8;
  color: var(--yk-fontcolor);
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: var(--style-border);
}

/* 评论表单 */
.comment-form {
  margin: 2rem 0;
}
.comment-form h3 {
  color: var(--yk-fontcolor);
  margin-bottom: 1rem;
}
.comment-form textarea {
  width: 100%;
  padding: 10px;
  border: var(--style-border);
  border-radius: 6px;
  margin-bottom: 1rem;
  resize: vertical;
}
.submit-comment-btn {
  padding: 8px 16px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}
.submit-comment-btn:hover {
  background: #359469;
}

/* 登录提示 */
.login-tip {
  margin: 2rem 0;
  color: #666;
}
.login-tip a {
  color: #42b983;
  text-decoration: none;
  margin-left: 0.5rem;
}

/* 评论区 */
.comments-section {
  margin: 3rem 0;
}

/* 返回链接 */
.back-link {
  display: inline-block;
  margin: 2rem 0;
  color: #42b983;
  text-decoration: none;
}
.back-link:hover {
  text-decoration: underline;
}
</style>