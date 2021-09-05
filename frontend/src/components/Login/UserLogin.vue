<template>
  <div id="App" style="height: 476px; margin: 0;">
    <v-row align="center">
      <v-col cols="12">
              <div id="nag">Zaloguj się za pomocą konta ucznia lub rodzica</div>
              <v-text-field color="red" v-model="login" :disabled="inputDisabled"
              label="E-mail" outlined></v-text-field>
              <v-text-field color="red" v-model="password" :disabled="inputDisabled"
              label="Hasło" outlined type="password"></v-text-field>
              <v-text-field color="red" v-model="symbol" :disabled="inputDisabled"
              label="Symbol" outlined></v-text-field>
              <v-select color="red" v-model="selectedSymbol" :disabled="inputDisabled"
              label="Wybierz odmianę dziennika UONET+" outlined :items="item"
              v-on:change="fakelog()"
              item-color="red"></v-select>
              <v-btn id="buttonTwo" dark color="red" elevation="2"
              @click="loginUser()">Zaloguj się</v-btn>
      </v-col>
    </v-row>
  </div>
</template>
<script>
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
  data() {
    return {
      inputDisabled: false,
      login: '',
      password: '',
      selectedSymbols: '',
      symbols: '',
      item: [
        'Vulcan',
        'Fakelog',
      ],
    };
  },
  methods: {
    async loginUser() {
      this.inputDisabled = true;
      Vue.set(this.$store.state, 'isLoading', true);
      const index = diary.diaries.findIndex((item) => item.name === this.selectedDiary);
      const response = await login.login(this.login, this.password,
        'powiatwulkanowy', diary.diaries[index].url);
      this.$store.state.loginData = response.data;

      if (this.$store.state.loginData.data.students.data.length > 1) {
        this.$store.state.showStudentsList = true;
        this.$store.state.isLoading = false;
      }
    },

    fakelog() {
      if (this.selectedSymbol === 'Fakelog') {
        this.login = 'jan@fakelog.cf';
        this.password = 'jan123';
        this.symbol = 'powiatwulkanowy';
      }
    },
  },
});
</script>
<style>
  #App{
    padding: 10px;
  }
  #nag{
    text-align: center;
    font-weight: 300;
    font-size: 1.3pc;
    margin-bottom: 1pc;
  }

  #buttonOne{
    margin-right: auto;
    display: block;
    float: left;
  }
</style>
