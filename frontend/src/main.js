import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
//import router from './router'

const app = createApp(App)

app.use(createPinia())
//app.use(router)

// Expose console.log globally for inline template use
// Ex. <span>{{ $log('Message or variable') }}</span>
app.config.globalProperties.$log = console.log;

app.mount('#app')
