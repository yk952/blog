<template>
  <div class="post-article-container">
    <h2>{{ isEdit ? '编辑文章' : '发布文章' }}</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-item">
        <label>文章标题：</label>
        <input 
          v-model="form.title" 
          type="text" 
          required 
          placeholder="请输入文章标题"
        >
      </div>
      <div class="form-item">
        <label>文章分类：</label>
        <select v-model="form.category" required>
          <option value="">请选择分类</option>
          <option v-for="cat in categories" :key="cat.id" :value="cat.id">
            {{ cat.name }}
          </option>
        </select>
      </div>
      <div class="form-item">
        <label>文章内容：</label>
        <!-- 富文本编辑器 -->
        <quill-editor 
          v-model="form.content" 
          ref="quillRef" 
          :options="editorOptions"
          class="editor"
        />
      </div>
      <button type="submit" class="submit-btn">
        {{ isEdit ? '更新文章' : '发布文章' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { QuillEditor } from '@vueup/vue-quill'  // 导入富文本编辑器
import '@vueup/vue-quill/dist/vue-quill.snow.css'  // 编辑器样式
import axios from 'axios'
import { ElMessage } from 'element-plus'

const router = useRouter()
const route = useRoute()
const isEdit = !!route.query.id  // 是否为编辑模式（通过URL参数判断）
const quillRef = ref(null)

// 表单数据
const form = ref({
  title: '',
  content: '',
  category: ''
})

// 分类列表（需后端提供分类接口，这里简化为请求示例）
const categories = ref([])

// 富文本编辑器配置
const editorOptions = ref({
  theme: 'snow',
  modules: {
    toolbar: [
      ['bold', 'italic', 'underline'],
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      [{ 'align': [] }],
      ['link', 'image'],
      ['clean']
    ]
  }
})

// 获取分类列表
const getCategories = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/categories/')  // 需后端实现分类列表接口
    categories.value = res.data
  } catch (err) {
    ElMessage.error('获取分类失败')
  }
}

// 编辑模式：获取文章详情
const getArticleDetail = async () => {
  try {
    const res = await axios.get(`http://localhost:8000/api/articles/${route.query.id}/`)
    form.value = {
      title: res.data.title,
      content: res.data.content,
      category: res.data.category
    }
  } catch (err) {
    ElMessage.error('获取文章详情失败')
  }
}

// 提交文章（创建/更新）
const handleSubmit = async () => {
  try {
    if (isEdit) {
      // 编辑：PUT请求
      await axios.put(`http://localhost:8000/api/articles/${route.query.id}/`, form.value)
      ElMessage.success('文章更新成功！')
    } else {
      // 发布：POST请求
      await axios.post('http://localhost:8000/api/articles/', form.value)
      ElMessage.success('文章发布成功！')
    }
    router.push('/')  // 跳转到首页
  } catch (err) {
    ElMessage.error(err.response?.data?.non_field_errors?.[0] || '操作失败')
  }
}

// 初始化：获取分类 + 编辑模式加载详情
onMounted(() => {
  getCategories()
  if (isEdit) {
    getArticleDetail()
  }
})
</script>

<style scoped>
.post-article-container {
  width: 800px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
}
.form-item {
  margin-bottom: 20px;
}
.form-item label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}
.form-item input, .form-item select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.editor {
  height: 400px;
}
.submit-btn {
  padding: 10px 20px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>