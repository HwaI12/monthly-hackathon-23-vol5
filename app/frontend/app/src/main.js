import axios from 'axios'
import { createApp } from 'vue'
import VueAxios from 'vue-axios'
import AxiosPlugin from './../plugin/axios'
import App from './App.vue'

createApp(App).use(VueAxios, axios).use(AxiosPlugin).mount('#app')
