<template>
  <div>
    <v-row align="center">
      <v-col cols="12"></v-col>
      <v-col cols="12">
        <v-text-field
          class="login-input"
          v-model="login"
          label="E-mail"
          outlined
          clearable>
        </v-text-field>
        <v-text-field
          class="login-input"
          v-model="password"
          label="Password"
          outlined
          clearable>
        </v-text-field>
      </v-col>
      <v-col cols="12">
        <v-select
          :items="domains"
          v-model="selectedSymbol"
          item-value="Fakelog"
          v-on:change="itemSelected()"
          label="Symbol"
          outlined></v-select>
      </v-col>
      <v-col cols="12">
        <v-btn
          class="login-button"
          depressed
          color="primary"
          @click="loginUser()">
          Log in!</v-btn>
        <v-divider style="padding: 5px"></v-divider>
        <a style="">You forgot password click here!</a>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Vue from 'vue';
import login from '../../api/login';

export default {
  name: 'UserLogin',
  data() {
    return {
      login: '',
      password: '',
      selectedSymbol: '',
      domains: [
        'Vulcan',
        'Fakelog',
      ],
    };
  },
  methods: {
    async loginUser() {
      Vue.set(this.$store.state, 'isLoading', true);
      const response = await login.register(this.login, this.password, this.selectedSymbol);
      this.$store.state.loginData = response.data;

      console.log(this.$store.state.loginData);

      if (this.$store.state.loginData.data.students.data.length > 1) {
        this.$store.state.isLoading = false;
        this.$store.state.showStudentsList = true;
      }
    },
    itemSelected() {
      if (this.selectedSymbol === 'Fakelog') {
        this.login = 'jan@fakelog.cf';
        this.password = 'jan123';
      }
    },
  },
};
</script>

<style scoped>

</style>
