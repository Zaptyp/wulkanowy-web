import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: true,
    group: null,
    mini: true,
    appbarTitle: 'Dashboard',
    selcetDialog: false,
    page: 'about',
    showStudentsList: false,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
});
