import Vue from "vue";
import App from "@/App.vue";
import router from "@/router";
import store from "@/store";
import vuetify from "@/plugins/vuetify";
import VueI18n from "vue-i18n";
import { languages, defaultLocale } from "@/i18n";

Vue.config.productionTip = false;

Vue.use(VueI18n)
const messages = Object.assign(languages)
const i18n = new VueI18n({
  locale: defaultLocale,
  fallbackLocale: 'pl',
  messages,
  pluralizationRules: {
    'pl': function(choice: number) {
      if (choice === 0) {
        return 0;
      }
      if (choice === 1) {
        return 1;
      }
      if (choice > 1 && choice < 5) {
        return 2;
      }
      if (choice > 4) {
        return 3;
      }
      return 3;
    }
  }
})

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: (h) => h(App),
}).$mount("#app");
