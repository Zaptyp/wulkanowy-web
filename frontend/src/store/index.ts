import Vue from "vue";
import Vuex from "vuex";
import router from "@/router";

Vue.use(Vuex);

interface State {
  loading: boolean;
  loginData: {
    symbols?: any;
    host?: string;
    ssl?: boolean;
  };
  repo_info: any;
  logged_in: boolean;
  selected_student: number;
  small_ui: boolean;
  view: string;
  drawer: {
    show: boolean;
    mini: boolean;
  };
  error: {
    show: boolean;
    description: string;
    details: string;
  };
}

export default new Vuex.Store({
  state: (): State => ({
    loading: false,
    loginData: {
      symbols: undefined,
      host: undefined,
      ssl: undefined,
    },
    repo_info: [],
    logged_in: false,
    selected_student: 0,
    small_ui: false,
    view: "dashboard",
    drawer: {
      show: true,
      mini: false,
    },
    error: {
      show: false,
      description: "",
      details: "",
    },
  }),
  mutations: {
    log_out(state) {
      state.loginData = [];
      state.logged_in = false;
      router.push("/");
    },
    drawer_show(state) {
      state.drawer.show = !state.drawer.show;
    },
    drawer_mini(state) {
      state.drawer.mini = !state.drawer.mini;
    },
  },
  actions: {},
  modules: {},
});
