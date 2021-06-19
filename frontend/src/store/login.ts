import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

interface LoginState {
  isLoading: boolean
  loginData: any
  showStudentsList: boolean
}

export default new Vuex.Store({
  state: (): LoginState => ({
    isLoading: false,
    loginData: null,
    showStudentsList: false,
  }),
  mutations: {
  },
  actions: {
  },
  modules: {
  },
});
