import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '../components/HomePage'
import NotFound from '../components/NotFound'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
