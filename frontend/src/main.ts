import 'modern-normalize/modern-normalize.css'
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';
import 'primevue/resources/primevue.min.css';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia()).use(router).use(PrimeVue).use(ToastService)

app.mount('#app')
