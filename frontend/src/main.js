import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
// import VueAuth from '@websanova/vue-auth'
// import WebsanovaAxios from '@websanova/vue-auth/drivers/http/axios.1.x'
// import VueRouter from '@websanova/vue-auth/drivers/router/vue-router.2.x'
// import { sync } from 'vuex-router-sync'
import Vuelidate from 'vuelidate'
// import store from './store'
import { MdButton, MdContent, MdTabs } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'

Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)

Vue.use(VueAxios, axios)
Vue.use(Vuelidate)

Vue.router = router
Vue.axios.defaults.baseURL = 'http://localhost:8000/api/'
Vue.axios.defaults.xsrfCookieName = 'csrftoken'
Vue.axios.defaults.xsrfHeaderName = 'X-CSRFToken'
Vue.axios.defaults.headers = {'X-Requested-With': 'XMLHttpRequest'}

// // authorization
// /* eslint-disable no-new */
// Vue.use(VueAuth, {
//   auth: {
//     request (req, token) {
//       this.options.http._setHeaders.call(this, req, {
//         Authorization: `JWT ${token}`
//       })
//     },
//     response (res) {
//       // Get Token from response body
//       return res.data.token
//     }
//   },
//   http: WebsanovaAxios,
//   router: VueRouter,
//   registerData: {
//     url: 'auth/register'
//   },
//   loginData: {
//     url: 'auth/login',
//     redirect: '/',
//     fetchUser: false
//   },
//   fetchData: {
//     enabled: false
//   },
//   refreshData: {
//     enabled: false
//   },
//   rolesVar: 'role'
// })
//
// sync(store, router)

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  // store,
  template: '<App/>',
  components: {
    App
  },
  render: h => h(App)
})
