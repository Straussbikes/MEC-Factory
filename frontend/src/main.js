import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import { createPinia } from 'pinia';
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { useUserStore } from '@/services/user-store';
// Set the base URL for your API requests
axios.defaults.baseURL = 'https://backend-94yb.onrender.com/api/v1';
axios.defaults.withCredentials = true;

const app = createApp(App);
const pinia = createPinia();

// Use Axios in Vue app
app.config.globalProperties.$axios = axios;
app.use(pinia);

// Create a Vuetify instance and pass it to the app
const vuetify = new createVuetify({
    components,
    directives,
    
});
app.use(vuetify);

app.use(router).mount('#app');
