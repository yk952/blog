import axios from 'axios'

// 创建Axios实例（统一配置基础路径）
const service = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 5000
})

const addTrailingSlash = (url) => {
  return url.endsWith('/') ? url : url + '/'
}

// 登录接口
export const login = (data) => {
  return service({
    url: '/users/login/',
    method: 'post',
    data
  })
}

// 注册接口
export const register = (data) => {
  return service({
    url: '/users/register/',
    method: 'post',
    data
  })
}

export default service