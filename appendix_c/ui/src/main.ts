import { createApp } from 'vue'
import App from './App.vue'
import store from './store'

import 'bootstrap/dist/js/bootstrap.min'
import 'bootstrap/dist/css/bootstrap.min.css'

import { setupAuth } from '@/auth'

const app = createApp(App)

app.use(store)

function callbackRedirect(appState: any) {
  if (appState) {
    console.log(appState.targetUrl)
  }
  window.location.href = ''
}

const authConfig = {
  domain: process.env.VUE_APP_AUTH_DOMAIN,
  client_id: process.env.VUE_APP_AUTH_CLIENT_ID,
  redirect_uri: process.env.VUE_APP_AUTH_REDIRECT_URI,
  audience: process.env.VUE_APP_AUTH_AUDIENCE,
  scope: process.env.VUE_APP_AUTH_SCOPE,
};

setupAuth(authConfig, callbackRedirect).then((auth) => {
  app.use(auth).mount('#app')
});
