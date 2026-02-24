import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
//import router from './router'

import { useAuthStore } from './stores/auth'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
//app.use(router)

// Expose console.log globally for inline template use
// Ex. <span>{{ $log('Message or variable') }}</span>
app.config.globalProperties.$log = console.log;

const authStore = useAuthStore()
authStore.getSession()

app.mount('#app')
