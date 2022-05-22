import axios from 'axios';
import store from '@/store/index';

export default {
  login: async (username: string, password: string, symbol: string, host: string, ssl: boolean) => {
    const response: any = await axios({
      method: 'POST',
      url: 'http://localhost:8000/login',
      headers: {
        'Content-Type': 'application/json',
      },
      data: {
        username,
        password,
        symbol,
        host,
        ssl,
      },
      withCredentials: true,
    })
    .catch(function (error: any) {
      if(error.toJSON().message == 'Network Error'){
        store.state.error.description = 'No internet connection';
        store.state.error.details = error.toJSON().stack;
        store.state.error.show = true;
        store.state.loading = false;
      } else {
        store.state.error.description = error.response.data.detail;
        store.state.error.details = error.toJSON().stack;
        store.state.error.show = true;
        store.state.loading = false;
      }
    });
    if (!response.data.students.length) {
      store.state.error.description = 'This account have not any students';
      store.state.error.show = true;
      store.state.loading = false;
      return null;
    } else {
      store.state.logged_in = true;
      store.state.loading = false;
      return response;
    }
  },
};
