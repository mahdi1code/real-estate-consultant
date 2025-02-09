import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
// import AboutView from '@/views/AboutView.vue'
// import JobsView from '../views/JOBS/Jobs.vue'
// import JobsDeteils from '../views/JOBS/JobsDetails.vue'
import NotFound from '@/views/NotFound.vue'


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => 
      import ('../views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'about',
    component : () => 
      import ('../views/AboutView.vue')
  },

  {
    path: '/jobs',
    name: 'jobs',
    component: () => 
      import ('../views/JOBS/Jobs.vue')
  },

  {
    path: '/jobs/:id',
    name: 'JobsDeteils',
    component: () => 
      import ('../views/JOBS/JobsDetails.vue'),
    props: true,
  },
  // Redirect
  {
    path: '/all-jobs',
    redirect: '/jobs', 
  },
  // Page Not Found
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound,
    }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
