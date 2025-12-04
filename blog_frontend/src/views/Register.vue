<template>
  <div class="register-container">
    <h2>用户注册</h2>
    <div class="form-item">
      <label>用户名：</label>
      <input v-model="username" type="text" placeholder="请输入用户名">
    </div>
    <div class="form-item">
      <label>密码：</label>
      <input v-model="password" type="password" placeholder="请输入6位以上密码">
    </div>
    <div class="form-item">
      <label>邮箱：</label>
      <input v-model="email" type="email" placeholder="如 test@example.com">
    </div>
    <!-- 纯按钮，无任何form干扰 -->
    <button @click="handleRegister" class="register-btn">注册</button>
    <div class="login-link">已有账号？<router-link to="/login">立即登录</router-link></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const username = ref('test006') // 固定测试用户名，避免输入错误
const password = ref('123456')  // 固定测试密码，避免输入错误
const email = ref('test006@example.com') // 固定测试邮箱

const handleRegister = async () => {
  // 日志1：证明函数被触发
  console.log('=== 注册函数开始执行 ===')
  console.log('要发送的方法：POST（强制指定）')
  console.log('要发送的数据：', {
    username: username.value,
    password: password.value,
    email: email.value
  })

  try {
    // 强制POST：用axios.post，地址和后端完全一致
    const res = await axios.post(
      'http://localhost:8000/api/users/register/', // 后端接口地址
      { username: username.value, password: password.value, email: email.value },
      {
        // 强制设置请求头，告诉后端这是POST提交
        headers: { 'Content-Type': 'application/json' },
        // 禁用缓存，避免旧请求干扰
        cache: false
      }
    )

    console.log('注册成功！后端响应：', res.data)
    alert('注册成功！')
    router.push('/login')
  } catch (err) {
    console.log('注册失败详情：', err)
    alert('失败原因：' + (err.response?.data?.message || err.message))
  }
}
</script>

<style scoped>
.register-container { width: 350px; margin: 100px auto; padding: 20px; border: 1px solid #eee; border-radius: 8px; }
.form-item { margin-bottom: 15px; display: flex; align-items: center; }
.form-item label { width: 80px; text-align: right; margin-right: 10px; }
.form-item input { flex: 1; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
.register-btn { width: 100%; padding: 10px; background: #42b983; color: white; border: none; border-radius: 4px; cursor: pointer; }
.login-link { margin-top: 10px; text-align: center; }
</style>