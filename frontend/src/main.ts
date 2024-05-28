import PrimeVue from 'primevue/config';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia()).use(router).use(PrimeVue)

app.mount('#app')
