<template>
  <div>
    <v-col cols="12">
      <p class="justify-center text-center headline font-weight-light">
        Zaloguj się za pomocą konta ucznia lub rodzica
      </p>
    </v-col>
    <v-col cols="12">
      <v-text-field
        color="red"
        v-model="login"
        :disabled="inputDisabled"
        label="E-mail"
        outlined
      />
      <v-text-field
        color="red"
        v-model="password"
        :disabled="inputDisabled"
        label="Hasło"
        outlined
        type="password"
      />
      <v-text-field
        color="red"
        v-model="symbol"
        :disabled="inputDisabled"
        label="Symbol"
        outlined
      />
      <v-select
        color="red"
        :items="diaryNames"
        v-model="selectedDiary"
        item-value=""
        v-on:change="itemSelected()"
        label="Symbol"
        selection="index"
        :disabled="inputDisabled"
        outlined
        item-color="red"
      />
    </v-col>
    <v-col cols="12">
      <v-btn
        dark
        color="red"
        elevation="2"
        @click="loginUser()"
        class="justify-end"
      >Zaloguj się</v-btn>
    </v-col>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import login from '../../api/login';
import diary from '../../assets/data/diary.json';

interface Login {
  login: string
  password: string
  symbol: string
  diaryNames: Array<string>
  selectedDiary: string
  inputDisabled: boolean
}
export default Vue.extend({
  name: 'UserLogin',
  data: (): Login => ({
    login: '',
    password: '',
    symbol: '',
    diaryNames: [],
    selectedDiary: '',
    inputDisabled: false,
  }),
  created() {
    this.diaryNames = diary.diaries.map((item): string => item.name);
  },
  methods: {
    async loginUser() {
      Vue.set(this.$store.state, 'isLoading', true);
      const index = diary.diaries.findIndex((item) => item.name === this.selectedDiary);
      const response = await login.login(this.login, this.password,
        'powiatwulkanowy', diary.diaries[index].url);
      this.$store.state.loginData = response.data;
      if (this.$store.state.loginData.data.students.data.length > 1) {
        this.$store.state.isLoading = false;
        this.$store.state.showStudentsList = true;
      } else {
        alert('Dane logowania są nie prawidłowe!');
      }
    },
    itemSelected() {
      if (this.selectedDiary === 'Fakelog') {
        this.login = 'jan@fakelog.tk';
        this.password = 'jan123';
        this.symbol = 'powiatwulkanowy';
      }
    },
  },
});
</script>
