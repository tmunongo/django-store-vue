import axios from "axios";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

axios.defaults.baseURL = "http://localhost:8000";
// axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

createApp(App).use(store).use(router, axios).mount("#app");
