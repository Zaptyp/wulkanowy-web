import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#9a0007",
        error: "#ff5722",
        snackbar: "#e57373",
      },
      dark: {
        primary: "#e57373",
        error: "#ff5722",
        snackbar: "#9a0007",
      },
    },
  },
});
