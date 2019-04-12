import Vue from 'vue';
import Router from 'vue-router';
import Classestest from '@/components/Classes_Test';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Classes_Test',
      component: Classestest,
    },
  ],
  mode: 'history',
});
