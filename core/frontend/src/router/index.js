import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListReservation from '@/components/reservations/ListReservations'
import EditReservation from '@/components/reservations/EditReservation'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/reservaciones',
      name: 'ListReservation',
      component: ListReservation
    },
    {
      path: '/reservaciones/:reservacionId/edit',
      name: 'ListReservation',
      component: EditReservation
    }
  ],
  mode: 'history'
})
