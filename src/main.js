import { createApp } from 'vue'
import { createWebHistory, createRouter } from "vue-router";
import App from './App.vue'
import MakroView from './components/Router-Views/MakroView.vue'
import MikroView from './components/Router-Views/MikroView.vue'
import ProstorskiView from './components/Router-Views/ProstorskiView.vue'
import './index.css'

const routes = [
    {
        path: "",
        name: "Main",
        component: MakroView,
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
  history: createWebHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
