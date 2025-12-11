<template>
  <div class="home-container">
    <h1>最新文章</h1>

    <!-- ========== 新增：分类筛选栏 ========== -->
    <div class="category-filter">
      <button @click="handleFilter(0)" :class="{ active: selectedCate === 0 }">
        全部文章
      </button>
      <button
        v-for="cate in categories"
        :key="cate.id"
        @click="handleFilter(cate.id)"
        :class="{ active: selectedCate === cate.id }"
      >
        {{ cate.name }}
      </button>
    </div>

    <!-- 加载状态 -->
    <div class="loading" v-if="loading">
      正在努力加载文章
    </div>

    <!-- 错误提示 -->
    <div class="error" v-if="error">
      <p>-_-:{{ error }}</p>
      <button @click="fetchArticles(selectedCate)">重试</button> <!-- 改动：重试时携带当前选中分类 -->
    </div>

    <!-- 文章列表 -->
    <div class="article-list" v-if="articles.length>0">
      <div class="article-item" v-for="article in articles" :key="article.id">
        <router-link :to="'/article/' + article.id" class="article-title">{{ article.title }}</router-link>
        <p class="article-desc">{{ article.content }}</p>
        <div class="article-meta">
          发布时间：{{ article.create_time }} 
          <!-- ========== 新增：显示文章分类 ========== -->
          <span v-if="article.category" class="article-category">| 分类：{{ article.category.name }}</span>
        </div>
      </div>
    </div>

    <!-- 无文章提示 -->
    <div class="no-articles" v-if="articles.length === 0 && !loading && !error">
      <p>暂无文章</p>
    </div>
  </div>
</template>

<script setup lang="ts">
// 1. 导入TS类型（复用article.ts中定义的Article类型）
import { getArticles, type Article } from '../api/article';
// ========== 新增：导入分类相关接口和类型 ==========
import { getCategories, type Category } from '../api/categories';
import { ref, onMounted } from 'vue'; // 新增：导入onMounted
import { RouterLink, useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';

console.log("首页文件已经启动了！");

// 2. 给数据添加TS类型约束，明确是Article数组
const articles = ref<Article[]>([]);
const loading = ref<boolean>(false);
const error = ref<string | null>(null);
// ========== 新增：分类相关响应式数据 ==========
const categories = ref<Category[]>([]); // 分类列表
const selectedCate = ref(0); // 选中的分类ID（0=全部）

// 3. 获取路由实例（解决router is not defined）
const router = useRouter();

// ========== 改动：fetchArticles支持分类参数 ==========
async function fetchArticles(categoryId = 0) { // 新增默认参数：全部分类
  console.log("开始尝试加载文章了！当前筛选分类ID：", categoryId);
  loading.value = true;
  error.value = null; // 重置错误状态
  try {
    // 关键：传递分类筛选参数（categoryId>0时才传）
    const params = categoryId > 0 ? { category: categoryId } : {};
    // 调用getArticles，传递分页=false + 筛选参数
    const response = await getArticles(); // 适配你改造后的getArticles接口
    console.log("后端返回的数据：", response);
    
    // 直接赋值，无需.data（response本身就是文章数组）
    articles.value = response || [];

    // 空数据提示（可选）
    if (articles.value.length === 0) {
      ElMessage.info(categoryId === 0 ? "暂无文章数据" : `该分类下暂无文章`);
    }
  } catch (err: any) { // 显式声明err类型
    console.log("加载失败了：", err);
    // 健壮的错误信息解析（覆盖所有场景）
    if (err.response?.status === 401) {
      // 401单独处理：跳登录页
      error.value = "登录已过期，请重新登录";
      ElMessage.error(error.value);
      router.push('/login'); // 跳登录页
    } else {
      // 其他错误：适配不同后端错误字段
      error.value = 
        err.response?.data?.non_field_errors?.[0] || 
        err.response?.data?.message || 
        err.message || 
        "加载文章失败，请稍后重试";
      ElMessage.error(error.value ?? "请求失败，请稍后重试");
    }
  } finally {
    loading.value = false;
  }
}

// ========== 新增：加载分类列表 ==========
const fetchCategories = async () => {
  try {
    const res = await getCategories();
    categories.value = res;
    console.log("加载分类列表成功：", res);
  } catch (err: any) {
    ElMessage.error(`加载分类失败：${err.message}`);
  }
};

// ========== 新增：分类筛选点击事件 ==========
const handleFilter = (cateId: number) => {
  selectedCate.value = cateId; // 更新选中分类
  fetchArticles(cateId); // 重新加载对应分类的文章
};

// ========== 改动：初始化逻辑（先加载分类，再加载文章） ==========
onMounted(async () => {
  await fetchCategories(); // 先加载分类
  fetchArticles(); // 加载全部文章（默认）
});
</script>

<style scoped>
.home-container {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}

h1 {
  color: var(--heo-fontcolor);
  margin-bottom: 2rem;
  border-bottom: 2px solid var(--heo-main);
  padding-bottom: 0.5rem;
}

/* ========== 新增：分类筛选栏样式 ========== */
.category-filter {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 2rem; /* 和原有样式的间距对齐 */
}
.category-filter button {
  padding: 6px 15px;
  border: 1px solid var(--heo-main); /* 复用你的主题色 */
  border-radius: 20px;
  background: var(--heo-card-bg); /* 复用你的卡片背景 */
  color: var(--heo-main); /* 复用主题色 */
  cursor: pointer;
  transition: all 0.3s;
}
.category-filter button.active {
  background: var(--heo-main);
  color: white;
}
.category-filter button:hover:not(.active) {
  border-color: var(--heo-main-op);
  color: var(--heo-hovertext);
}

.article-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.article-item {
  padding: 1.5rem;
  border: var(--style-border);
  border-radius: 8px;
  background: var(--heo-card-bg);
  box-shadow: var(--heo-card-box-shadow);
  transition: all 0.3s;
}
.article-item:hover {
  box-shadow: var(--heo-card-hover-box-shadow);
  border-color: var(--heo-main-op);
}

.article-title {
  font-size: 1.5rem;
  color: var(--heo-fontcolor);
  text-decoration: none;
  margin-bottom: 1rem;
  display: block;
  transition: color 0.3s;
}
.article-title:hover {
  color: var(--heo-hovertext);
}

.article-desc {
  color: var(--heo-secondtext);
  line-height: 1.6;
  margin: 1rem 0;
}

.article-meta {
  color: var(--heo-secondtext);
  font-size: 0.9rem;
}
/* ========== 新增：文章分类样式 ========== */
.article-category {
  margin-left: 10px;
  color: var(--heo-main);
}

/* 加载和错误样式可补充 */
.loading {
  color: var(--heo-secondtext);
  padding: 2rem;
  text-align: center;
}

.error {
  color: #ff4d4f; /* 错误色 */
  padding: 2rem;
  text-align: center;
}

.error button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  background: var(--heo-main);
  color: white;
  cursor: pointer;
}

.no-articles {
  color: var(--heo-secondtext);
  padding: 2rem;
  text-align: center;
}
</style>