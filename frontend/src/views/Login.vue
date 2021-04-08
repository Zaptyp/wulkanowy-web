<template>
  <div id="login">
    <img class="image" src="../assets/logo_login.svg" width="500">
    <v-content style="width: 100%;">
      <v-card loading="isLoading" id="login-form" class="mx-auto mt-9">
        <form>
          <v-container>
            <UserLogin></UserLogin>
          </v-container>
        </form>
      </v-card>
    </v-content>
  </div>
</template>

<script>
import UserLogin from '../components/Login/UserLogin.vue';

export default {
  name: 'Login',
  components: {
    UserLogin,
  },
  data() {
    return {
      login: '',
      password: '',
      domains: [
        'Vulcan Uonet',
        'Fakelog',
      ],
      isLoading: false,
    };
  },
  methods: {
  },
};
</script>

<style>
::-webkit-scrollbar {
  display: none;
}

#login {
  text-align: center;
  overflow: hidden;
  background-image: url("../assets/wallpaper.jpg");
  background-size: cover;
  height: 100%;
  width: 100%;
}

#login-form {
  width: 500px;
  top: 15%;
  bottom: 50%;
}

.login-input {
  margin: 10px;
}

.login-button {
  margin: 10px;
}
</style>
