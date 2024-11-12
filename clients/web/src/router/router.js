import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/MainApp',
    name: 'MainApp',
    component: () => import('@/views/MainApp.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LogIn.vue'),
  },
  {
    path: '/HistoricalData',
    name: 'HistoricalData',
    component: () => import('@/views/HistoricalData.vue'),
    meta: { requiresAuth: true }
  },
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  // 配置router active的類名
  // 每個router都會經過/所以會被激活，通過exact可以精準選擇所在路由
  // linkActiveClass: '', // 模糊比對
  linkExactActiveClass: 'active', // 準確比對
  routes
})


router.beforeEach((to) => {
  // to：使用者要跳轉的路由
  // from：使用者前一個訪問的路由
  // 回傳 false 取消跳轉，true / undefined（預設）容許跳轉
  // next 參數在 Vue Router 4 並非必須

  const token = sessionStorage.getItem("token");

  if (to.fullPath == '/login') return; // 登入頁不用驗證

  if (token === null) {
    router.push('/login')
  }
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!sessionStorage.getItem('token'); // 假設登入 token 存在 sessionStorage 中
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    // 如果頁面需要登入但使用者未登入，則重新導向到登入頁面
    next('/login');
  } else {
    next(); // 允許進入頁面
  }
});
export default router
