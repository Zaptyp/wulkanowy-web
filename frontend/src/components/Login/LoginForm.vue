<template>
  <div id="login-form" class="fill-height">
    <v-form @submit.prevent="login" class="d-flex fill-height flex-column">
      <v-card-title class="d-flex justify-center text-center"
        >Sign in with the student or parent account</v-card-title
      >
      <div class="px-5">
        <v-text-field outlined label="Email" v-model="loginData.username" :rules="[rules.required]" />
        <v-text-field
          outlined
          label="Password"
          v-model="loginData.password"
          :rules="[rules.required]"
          :type="showPassword ? 'text' : 'password'"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="showPassword = !showPassword"
        />
        <v-autocomplete
          outlined
          label="Symbol"
          v-model="loginData.symbol"
          :rules="[rules.required]"
          :items="
            loginData.selectedRegisterVariantName == 'Fakelog'
              ? ['powiatwulkanowy', 'adsf']
              : symbols
          "
        />
        <v-select
          outlined
          label="UONET+ register variant"
          v-model="loginData.selectedRegisterVariantName"
          :rules="[rules.required]"
          :items="registerVariantsNames"
          @change="registerVariantSelected()"
        />
      </div>
      <v-card-actions class="px-5 pb-5 pt-0 mt-auto">
        <v-spacer />
        <v-btn color="primary" type="submit">Sign in</v-btn>
      </v-card-actions>
    </v-form>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Api from "@/api";
import RegisterVariants from "@/assets/res/registers.json";
import Symbols from "@/assets/res/symbols.json";

interface LoginFormData {
  loginData: {
    username: string;
    password: string;
    symbol: string;
    selectedRegisterVariantName: string;
  };
  registerVariantsNames: Array<string>;
  symbols: Array<string>;
  showPassword: boolean;
  rules: any;
}

export default Vue.extend({
  data: (): LoginFormData => ({
    loginData: {
      username: "",
      password: "",
      symbol: "",
      selectedRegisterVariantName: "Vulcan",
    },
    registerVariantsNames: [],
    symbols: [],
    showPassword: false,
    rules: {
      required: (value: string) => !!value || "This field are required.",
    },
  }),

  created() {
    this.registerVariantsNames = RegisterVariants.map((item): string => item.name);
    this.symbols = Symbols;
  },

  computed: {
    host() {
      return RegisterVariants[
        RegisterVariants.findIndex(
          (item) => item.name === this.loginData.selectedRegisterVariantName
        )
      ].host;
    },
    ssl() {
      return RegisterVariants[
        RegisterVariants.findIndex(
          (item) => item.name === this.loginData.selectedRegisterVariantName
        )
      ].ssl;
    },
  },

  methods: {
    registerVariantSelected() {
      if (this.loginData.selectedRegisterVariantName == "Fakelog") {
        this.loginData.username = "jan@fakelog.cf";
        this.loginData.password = "jan123";
        this.loginData.symbol = "powiatwulkanowy";
      }
    },
    async login() {
      const state = this.$store.state;
      state.loading = true;
      state.error.show = false;
      state.error.description = "";
      state.logged_in = false;
      state.selected_student = undefined;

      if (!this.loginData.username || !this.loginData.password || !this.loginData.symbol) {
        state.error.description = "All fields are required!";
        state.error.show = true;
        state.loading = false;
      } else {
        let response: any = await Api.login(
          this.loginData.username,
          this.loginData.password,
          this.loginData.symbol,
          this.host,
          this.ssl
        );
        if (response) {
          this.$store.state.loginData = response.data;
        }
      }
    },
  },
});
</script>

<style lang="scss" scoped>
.theme--dark.v-btn {
  color: #1e1e1e !important;
}
</style>
