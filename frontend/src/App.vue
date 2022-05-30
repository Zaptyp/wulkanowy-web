<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "App",

  beforeMount() {
    const dark = localStorage.getItem("dark");
    if (dark) {
      if (dark == "true") {
        this.$vuetify.theme.dark = true;
      } else {
        this.$vuetify.theme.dark = false;
      }
    } else {
      localStorage.setItem("dark", "false");
    }
    const language = localStorage.getItem("language");
    if (language) {
      this.$i18n.locale = language;
    }
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      const screen_width = window.innerWidth;
      this.$store.state.small_ui = screen_width < 1264;
    },
  },
  watch: {
    '$vuetify.theme.dark': {
      handler (value: boolean) {
        localStorage.setItem("dark", String(value))
      }
    },
    '$i18n.locale': {
      handler (value: string) {
        localStorage.setItem("language", value)
      }
    },
  }
});
</script>

<style lang="scss">
.v-card__text,
.v-card__title {
  word-break: normal !important;
}
</style>

