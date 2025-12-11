import axios from 'axios';
import type { AxiosInstance, AxiosResponse, InternalAxiosRequestConfig } from 'axios';
import { ElMessage } from 'element-plus'; // 需确保已安装element-plus
import router from '../router'; // 导入路由实例，用于401时跳转登录页

// ===================== 核心类型定义（适配后端实际返回结构） =====================
// 登录请求参数类型
interface LoginParams {
  username: string;
  password: string;
}

// 注册请求参数类型
interface RegisterParams {
  username: string;
  password: string;
  email?: string;
  phone?: string;
}

// 登录响应数据类型（完全匹配后端返回：token + username + user_id）
interface LoginResponse {
  token: string;
  username: string;
  user_id: number; // 注意后端是user_id，不是userId
}

// 注册响应数据类型（根据后端实际返回调整）
interface RegisterResponse {
  user_id: number;
  username: string;
}

// ===================== 创建Axios实例 =====================
const service: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json;charset=utf-8'
  }
});

// ===================== 请求拦截器：自动携带Token =====================
service.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // 从localStorage获取登录时存储的Token
    const token = localStorage.getItem('token');
    console.log(`[请求拦截器] 准备请求 ${config.url}`);
    console.log(`[请求拦截器] 读取到的Token: ${token}`);
    if (token) {
      // 强制转字符串（避免Token为null/undefined），严格匹配DRF的Token格式
      config.headers.Authorization = `Token ${String(token).trim()}`;
      console.log(`[请求拦截器] 请求头已添加: ${config.headers.Authorization}`);
    } else {
      console.warn(`[请求拦截器] 未读取到Token，URL: ${config.url}`);
    }
    return config;
  },
  (error) => {
    // 请求错误前置处理
    ElMessage.error('请求发送失败，请检查网络');
    return Promise.reject(error);
  }
);

// ===================== 响应拦截器：统一处理结果 + 401错误 =====================
service.interceptors.response.use(
  (response: AxiosResponse) => {
    // 直接返回响应体（后端无code/message包裹，简化前端解析）
    return response.data;
  },
  (error) => {
    // 处理响应错误（重点处理401未授权）
    const status = error.response?.status;
    const errMsg = error.response?.data?.non_field_errors?.[0] || error.message;

    if (status === 401) {
      // 401：Token过期/无效/未携带，清除本地存储并跳回登录页
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      localStorage.removeItem('user_id');
      ElMessage.error('登录已过期，请重新登录');
      // 跳转到登录页（避免重复跳转）
      if (router.currentRoute.value.path !== '/login') {
    router.push('/login');
      }
    } else {
      // 其他错误（如400/500）提示具体信息
      ElMessage.error(errMsg || '服务器响应失败');
    }

    return Promise.reject(error);
  }
);

// ===================== 工具函数：URL末尾补斜杠 =====================
const addTrailingSlash = (url: string): string => {
  return url.endsWith('/') ? url : `${url}/`;
};

// ===================== 接口封装：登录/注册 =====================
/**
 * 登录接口
 * @param data 登录参数
 * @returns 登录响应数据（token + username + user_id）
 */
export const login = async (data: LoginParams): Promise<LoginResponse> => {
  return service({
    url: addTrailingSlash('/users/login'),
    method: 'post',
    data
  });
};

/**
 * 注册接口
 * @param data 注册参数
 * @returns 注册响应数据
 */
export const register = async (data: RegisterParams): Promise<RegisterResponse> => {
  return service({
    url: addTrailingSlash('/users/register'),
    method: 'post',
    data
  });
};

export default service;