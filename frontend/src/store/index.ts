import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: true,
    group: null,
    mini: true,
    appbarTitle: 'Dashboard',
    selectedStudent: 0,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
});
