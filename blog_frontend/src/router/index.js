// src/router/index.js
import { createRouter, createWebHashHistory } from 'vue-router'

// 路由配置：保留所有功能，移除 TS 类型注解
const routes = [
  {
    path: '/',
    name: 'home',
    // 懒加载（纯 JS 保留 import() 语法，无需 TS 类型）
    component: () => import('@/views/Home.vue'),
    meta: {
      title: '首页 - 我的博客' // 页面标题
    }
  },
  {
    path: '/article/:id',
    name: 'articleDetail',
    component: () => import('@/views/ArticleDetail.vue'),
    meta: {
      title: '文章详情 - 我的博客'
    }
  },
  {
    path: '/post',
    name: 'postArticle',
    component: () => import('@/views/PostArticle.vue'),
    meta: {
      requiresAuth: true, // 需要登录拦截
      title: '发布文章 - 我的博客'
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/Login.vue'),
    meta: {
      title: '登录 - 我的博客'
    }
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/Register.vue'),
    meta: {
      title: '注册 - 我的博客'
    }
  },
  // 404 兜底路由（访问不存在的路径跳转）
  {
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: () => import('@/views/NotFound.vue'),
    meta: {
      title: '404 - 页面不存在'
    }
  }
]

const router = createRouter({
  history: createWebHashHistory(), // 哈希模式（无需后端配置）
  routes,
  // 路由切换时滚动到顶部（优化体验）
  scrollBehavior: () => ({ top: 0 })
})

// 路由守卫：登录拦截 + 动态设置页面标题（纯 JS 移除 TS 类型注解）
router.beforeEach((to, from, next) => {
  // 动态设置浏览器标题
  if (to.meta.title) {
    document.title = to.meta.title
  }

  // 登录拦截逻辑（核心功能保留）
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('token')
    if (token) {
      next() // 已登录，放行
    } else {
      // 未登录，跳转到登录页，并记录原路径（登录后可跳转回）
      next({
        name: 'login',
        query: { redirect: to.fullPath } // 存储原路径到 query 参数
      })
    }
  } else {
    next() // 无需登录的路由，直接放行
  }
})

export default router