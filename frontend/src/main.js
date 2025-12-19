import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
//import router from './router'

const app = createApp(App)

app.use(createPinia())
//app.use(router)

// Expose console globally
app.config.globalProperties.$log = console.log;
app.config.globalProperties.$console = console;

app.mount('#app')
