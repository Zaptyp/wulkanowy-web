import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoading: false,
  },
  mutations: {
  },
  actions: {
    setLoading(state) {
      if (!this.state.isLoading) {
        this.state.isLoading = true;
      }

      this.state.isLoading = false;
    }
  },
  modules: {

  },
});
