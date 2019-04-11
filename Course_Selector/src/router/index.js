import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Classestest from '@/components/Classes_Test';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/Ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Classes_Test',
      component: Classestest,
    },
  ],
  mode: 'history',
});
