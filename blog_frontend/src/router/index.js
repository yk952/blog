import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import ArticleDetail from '@/views/ArticleDetail.vue'
import PostArticle from '@/views/PostArticle.vue'
import Login from '@/views/Login.vue'  //导入模块核心和组件

const routers = [
    {
        path:'/',
        name:'home',
        component:Home,
    },
    {
        path:'/article/:id',//动态路由，其中的：表示为占位符，示意后面ID会被实际参数替换
        name:'articleDetail',
        component:ArticleDetail,
    },
    {
        path:'/post',
        name:'PostArticle',
        component:PostArticle,
    },
    {
        path:'/Login',
        name:'Login',
        component:Login,
    }
]
//注册路由

const router=createRouter({
    history:createWebHashHistory(),//会自动适配为对应的子路径，确保路由跳转不会出现路径错误。
    routes:routers
})


export default router