import Vue from 'vue';
import Vuex, { Store } from 'vuex';

Vue.use(Vuex);

interface IndexState {
  drawer: boolean
  group: any
  mini: boolean
  appbarTitle: string
  selectedStudent: number
}

export default new Vuex.Store({
  state: (): IndexState => ({
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
