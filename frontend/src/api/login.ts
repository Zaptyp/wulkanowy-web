import axios, { AxiosResponse } from 'axios';
import Cookies from 'universal-cookie';

export default {
  register: async (email: string, password: string, symbol: string): Promise<AxiosResponse> => {
    const cookies = new Cookies();
    const response = await axios({
      method: 'post',
      url: 'http://localhost:8000/api/login',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': cookies.get('csrf-token'),
      },
      data: {
        loginName: email,
        Password: password,
        Symbol: symbol,
        diaryUrl: 'http://cufs.fakelog.cf/',
      },
    });

    document.cookie = response.headers['Set-Cookie'];
    return response;
  },
};
