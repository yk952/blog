// src/router/index.d.ts
import type { Router } from 'vue-router';

// 匹配你实际的导入路径：'./router'
declare module './router' {
  const router: Router;
  export default router;
}