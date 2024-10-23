import { createRouter, createWebHistory } from 'vue-router'
import makefriends from '../components/makefriends.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/makefriends',
      name: 'makefriends',
      component: makefriends
    }
  ]
})

export default router
