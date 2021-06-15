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
          :items="diaryNames"
          v-model="selectedDiary"
          item-value=""
          v-on:change="itemSelected()"
          label="Symbol"
          selection="index"
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

<script lang="ts">
import Vue from 'vue';
import login from '../../api/login';
import diary from '../../assets/data/diary.json';

interface Login {
  login: string
  password: string
  diaryNames: Array<string>
  selectedDiary: string
}

export default Vue.extend({
  name: 'UserLogin',
  data: (): Login => ({
    login: '',
    password: '',
    diaryNames: [],
    selectedDiary: '',
  }),
  created() {
    this.diaryNames = diary.diaries.map((item): string => item.name);
  },
  methods: {
    async loginUser() {
      Vue.set(this.$store.state, 'isLoading', true);
      const index = diary.diaries.findIndex((item) => item.name === this.selectedDiary);
      console.log(index);
      const response = await login.login(this.login, this.password,
        diary.diaries[index].name, diary.diaries[index].url);
      this.$store.state.loginData = response.data;
      console.log(this.$store.state.loginData);

      if (this.$store.state.loginData.data.students.data.length > 1) {
        this.$store.state.isLoading = false;
        this.$store.state.showStudentsList = true;
      }
    },
    itemSelected() {
      if (this.selectedDiary === 'Fakelog') {
        this.login = 'jan@fakelog.cf';
        this.password = 'jan123';
      }
    },
  },
});
</script>

<style scoped>

</style>
