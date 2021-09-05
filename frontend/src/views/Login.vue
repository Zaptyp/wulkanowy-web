<template>
  <div id="login">
    <v-main style="width: 100%;">
      <div style="clear: both;"></div>
      <v-card
        elevation="10"
        id="login-form"
        class="mx-auto"
        >
        <Baner v-if="window.width > 900"></Baner>
        <div class="card">
          <v-col>
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
        </div>
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
  height: 100%;
  width: 100%;
}
#login-form {
  top: 15%;
  width: 850px;
  margin-bottom: 200px;
}
.login-input {
  margin: 10px;
}
.login-button {
  margin: 10px;
}
</style>
