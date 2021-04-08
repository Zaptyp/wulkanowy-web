<template>
  <div>
    <v-row align="center">
      <v-col cols="12"></v-col>
      <v-col cols="12">
        <v-text-field
          class="login-input"
          v-model="login"
          label="Login"
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
          label="Symbol"
          outlined></v-select>
      </v-col>
      <v-col cols="12">
        <v-btn
          class="login-button"
          depressed
          color="primary"
          v-on:click="this.loginUser()">
          Log in!</v-btn>
        <v-divider style="padding: 5px"></v-divider>
        <a style="">You forgot password click here!</a>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'UserLogin',
  data() {
    return {
      login: '',
      password: '',
      domains: [
        'Vulcan',
        'Fakelog',
      ],
      selectedDomain: '',
    };
  },
  methods: {
    loginUser() {
      this.$store.state.isLoading = true;
    },
  },
};
</script>

<style scoped>

</style>
