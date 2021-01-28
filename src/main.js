import { createApp } from 'vue'
import { createWebHashHistory , createRouter } from "vue-router";
import App from './App.vue'
import MakroView from './components/Router/Views/Makro.vue'
import MikroView from './components/Router/Views/Mikro.vue'
import ProstorskiView from './components/Router/Views/Prostorski.vue'
import './index.css'

const routes = [
    {
      path: "/",
      name: "Main",
      component: MikroView,
    },
    {
      path: "/makro",
      name: "Makro",
      component: MakroView,
    },
    {
      path: "/mikro",
      name: "Mikro",
      component: MikroView,
    },
    {
      path: "/prostorski",
      name: "Prostorski",
      component: ProstorskiView,
    }
  ];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
