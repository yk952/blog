import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

// Axios请求拦截器：自动添加Token
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Token ${token}`  // 与后端Token认证格式一致
    }
    return config
  },
  (error) => Promise.reject(error)
)

app.config.globalProperties.$axios = axios
app.use(router).mount('#app')