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
  selected_student: {
    symbol?: string;
    school?: string;
    student?: string;
    register?: number;
  };
  tableView: boolean;
  small_ui: boolean;
  schoolInfoTabs: number;
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
    selected_student: {
      symbol: undefined,
      school: undefined,
      student: undefined,
      register: undefined
    },
    tableView: false,
    small_ui: false,
    schoolInfoTabs: 0,
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
      state.loginData.symbols = undefined;
      state.loginData.host = undefined;
      state.loginData.ssl = undefined;
      state.selected_student.symbol = undefined;
      state.selected_student.school = undefined;
      state.selected_student.student = undefined;
      state.selected_student.register = undefined;
      state.logged_in = false;
      router.push("/");
    },
    drawer_show(state) {
      state.drawer.show = !state.drawer.show;
    },
    drawer_mini(state) {
      state.drawer.mini = !state.drawer.mini;
    },
    tableView(state) {
      state.tableView = !state.tableView;
    }
  },
  actions: {},
  modules: {},
});
