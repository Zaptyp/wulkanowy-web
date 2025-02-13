import axios from "axios";
import store from "@/store/index";

const baseURL = process.env.VUE_APP_BASE_URL;
export default {
  login: async (
    username: string,
    password: string,
    host: string,
    ssl: boolean
  ) => {
    const response: any = await axios({
      method: "POST",
      url: `${baseURL}/api/v1/auth/signin`,
      headers: {
        "Content-Type": "application/json",
      },
      data: {
        username,
        password,
        host,
        ssl,
      },
      withCredentials: true,
    }).catch(function (error: any) {
      if (error.toJSON().message == "Network Error") {
        store.state.error.description = "network_error";
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
    if (!response.data.length) {
      store.state.error.description = "no_symbols_account";
      store.state.error.show = true;
      store.state.loading = false;
      return null;
    } else {
      store.state.logged_in = true;
      store.state.loading = false;
      return response;
    }
  },
  uonetplusUczenReqeust: async (
    host: string,
    symbol: string,
    school_id: string,
    ssl: boolean,
    request: string,
    headers: Record<string, unknown>,
    register_cookies: Record<string, unknown>,
    session_data: string,
    payload: Record<string, unknown>
  ) => {
    const response: any = await axios({
      method: "POST",
      url: `${baseURL}/api/v1/uonetplus-uczen/${request}`,
      headers: {
        "Content-Type": "application/json",
      },
      data: {
        host,
        symbol,
        school_id,
        ssl,
        headers,
        register_cookies,
        session_data,
        payload,
      },
      withCredentials: true,
    }).catch(function (error: any) {
      if (error.toJSON().message == "Network Error") {
        store.state.error.description = "network_error";
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
    store.state.loading = false;
    return response;
  },
  get_repo_info: async () => {
    const response: any = await axios({
      method: "GET",
      url: `${baseURL}/api/v1/github/frontend`,
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: false,
    }).catch(function (error: any) {
      if (error.toJSON().message == "Network Error") {
        store.state.error.description = "network_error";
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
    return response;
  },
};
