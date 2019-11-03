import Vue from "vue";
import VueRouter from "vue-router";
import Dashboard from '@/views/Dashboard.vue'


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: Dashboard
  },
  // {
  //   path: '/projects',
  //   name: 'projects',
  //   component: Projects
  // },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
