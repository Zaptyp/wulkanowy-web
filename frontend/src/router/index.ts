import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Login from '../views/Login.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/user',
    name: 'User',
    component: () => import('../views/Panel.vue'),
  },
  {
    path: '*',
    name: 'Login',
    component: () => import('../views/Login.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
