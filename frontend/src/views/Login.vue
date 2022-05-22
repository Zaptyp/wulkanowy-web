<template>
  <div id="login" class="d-flex fill-hieght justify-center align-center">
    <v-card id="login-card" elevation="15">
      <v-row no-gutters class="d-flex fill-height">
        <v-col cols="12" md="5" class="primary rounded-l d-md-flex d-none">
          <Baner />
        </v-col>
        <v-col cols="12" md="7">
          <LoginForm v-if="!this.$store.state.logged_in & !this.$store.state.loading" />
          <Loading v-if="this.$store.state.loading" />
          <SelectStudent v-if="this.$store.state.logged_in & !this.$store.state.loading" />
        </v-col>
      </v-row>
    </v-card>
    <Snackbar />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { LoginForm, SelectStudent, Loading, Baner, Snackbar } from "@/components";

export default Vue.extend({
  name: "Login",

  components: {
    LoginForm,
    Loading,
    SelectStudent,
    Baner,
    Snackbar,
  },
  beforeMount() {
    if (this.$store.state.logged_in) {
      this.$router.push("/user");
    }
  },
});
</script>

<style lang="scss" scoped>
#login {
  background: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)),
    url("../assets/img/login_wallpaper.jpg");
  background-size: cover;
  height: 100%;
  width: 100%;
}

@media only screen and (max-width: 959px) {
  #login-card {
    width: 100vw;
    min-height: 100vh;
    border-radius: 0;

    .row {
      min-height: 100vh;
    }
  }
}

@media only screen and (min-width: 960px) {
  #login-card {
    width: 750px;

    .row {
      align-items: stretch;
    }
  }
}
</style>
