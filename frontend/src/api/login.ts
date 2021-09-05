import axios, { AxiosResponse } from 'axios';
import Cookies from 'universal-cookie';

export default {
  login: async (email: string, password: string, symbol: string, diaryUrl: string)
    : Promise<AxiosResponse> => {
    const cookies = new Cookies();
    const response = await axios({
      method: 'POST',
      url: 'http://localhost:8000/api/login',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': cookies.get('csrftoken'),
      },
      data: {
        loginName: email,
        Password: password,
        Symbol: symbol,
        diaryUrl,
      },
      withCredentials: true,
    });

    document.cookie = response.headers['Set-Cookie'];
    return response;
  },
};
