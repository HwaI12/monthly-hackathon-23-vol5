import axios from 'axios';
import { createApp } from "vue";

import App from './App.vue';
import router from './router';

const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.headers.post['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000';
axios.defaults.baseURL = 'http://127.0.0.1:8000';  // the FastAPI backend

app.use(router);
app.mount("#app");
