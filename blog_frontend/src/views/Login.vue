<template>
  <div class="login-container">
    <h2>用户登录</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-item">
        <label>用户名：</label>
        <input 
          v-model="username" 
          type="text" 
          required 
          placeholder="请输入用户名"
        >
      </div>
      <div class="form-item">
        <label>密码：</label>
        <input 
          v-model="password" 
          type="password" 
          required 
          placeholder="请输入密码"
        >
      </div>
      <button type="submit" class="login-btn">登录</button>
      <div class="register-link">
        没有账号？<router-link to="/register">立即注册</router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '@/api/user'
import { ElMessage } from 'element-plus'

const router = useRouter()
const username = ref('')
const password = ref('')

const handleLogin = async () => {
  try {
    const res = await login({ username: username.value, password: password.value });
    
    // 1. 强制校验Token存在
    if (!res.token) {
      ElMessage.error('登录失败：未获取到Token');
      return;
    }

    // 2. 正确存储（确保key与请求拦截器读取的一致）
    localStorage.setItem('token', res.token.trim());
    localStorage.setItem('username', res.username);
    localStorage.setItem('user_id', res.user_id.toString());

    // 3. 验证存储结果（调试用）
    console.log('存储的Token：', localStorage.getItem('token'));

    ElMessage.success('登录成功');
    router.push('/');
  } catch (err) {
    console.error('登录错误：', err);
    ElMessage.error('登录失败');
  }
};
</script>

<style scoped>
.login-container {
  width: 350px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
}
.form-item {
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}
.form-item label {
  width: 80px;
  text-align: right;
  margin-right: 10px;
}
.form-item input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.login-btn {
  width: 100%;
  padding: 10px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.login-btn:hover {
  background: #359469;
}
.register-link {
  margin-top: 10px;
  text-align: center;
}
.register-link a {
  color: #42b983;
  text-decoration: none;
}
</style>