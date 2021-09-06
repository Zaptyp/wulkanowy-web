<template>
  <div id="login">
    <v-main style="width: 100%;">
      <v-card
        elevation="10"
        id="login-form"
        class="mx-auto"
        :tile="window.width < 900"
        >
        <v-row no-gutters>
          <v-col
            class="red darken-2 rounded-l-sm"
            cols="12"
            md="5"
            style="min-height: 500px;"
            v-if="window.width > 900"
          ><Baner v-if="window.width > 900"></Baner></v-col>
          <v-col cols="12" md="7">
            <form>
              <v-container>
                <UserLogin
                v-if="!this.$store.state.showStudentsList && !this.$store.state.isLoading">
                </UserLogin>
                <SelectStudent
                v-if="this.$store.state.showStudentsList && !this.$store.state.isLoading">
                </SelectStudent>
                <Loading v-if="this.$store.state.isLoading"></Loading>
              </v-container>
            </form>
          </v-col>
        </v-row>
      </v-card>
    </v-main>
  </div>
</template>

<script>
import UserLogin from '../components/Login/UserLogin.vue';
import SelectStudent from '../components/Login/SelectStudent.vue';
import Baner from '../components/Login/Baner.vue';
import Loading from '../components/Login/Loading.vue';

export default {
  name: 'Login',
  components: {
    SelectStudent,
    UserLogin,
    Baner,
    Loading,
  },
  data() {
    return {
      windowWidth: '',
      window: {
        width: 0,
        height: 0,
      },
    };
  },
  created() {
    window.addEventListener('resize', this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    getLoading() {
      return this.$store.state.isLoading;
    },
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
    },
  },
};
</script>

<style>
::-webkit-scrollbar {
  display: none;
}
#login {
  text-align: center;
  background-position: center center;
  overflow: hidden;
  background-image: url("../assets/wallpaper.jpg");
  background-size: cover;
  min-height: 100vh;
  width: 100%;
}
#login-form {
  top: 15%;
  width: 850px;
  margin-bottom: 200px;
  min-height: 500px;
}
.login-input {
  margin: 10px;
}
.login-button {
  margin: 10px;
}

@media only screen and (max-width: 900px) {
  #login-form {
    top: 0%;
    margin: 0;
    width: 100vw;
    min-height: 100vh;
  }
}
</style>
