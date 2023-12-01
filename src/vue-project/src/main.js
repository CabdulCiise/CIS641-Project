import { createApp } from 'vue'
import App from './App.vue'

import router from './router'

import 'primevue/resources/primevue.min.css';
import 'primevue/resources/themes/bootstrap4-dark-blue/theme.css';
import 'primeicons/primeicons.css';

import PrimeVue from 'primevue/config';
import PrimeIcons from 'primevue/config';

const app = createApp(App);

app.use(router);
app.use(PrimeVue);
app.use(PrimeIcons);

app.mount('#app')
