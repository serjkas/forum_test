import { createRouter, createWebHistory } from 'vue-router'
import Users from '@/components/Users.vue'

const routes = [
  {
    path: '',
    component: Users
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
