<template>
  <div id="baner" class="d-flex justify-center align-center fill-height flex-column">
    <img
      :src="`${
        this.$vuetify.theme.dark
          ? require('../../assets/img/black_icon.svg')
          : require('../../assets/img/white_icon.svg')
      }`"
      width="140"
    />
    <v-card-title
      :class="`text-center justify-center pa-2 headline ${
        this.$vuetify.theme.dark ? 'black--text' : 'white--text'
      }`"
    >
      {{ $t("app_name") }}
    </v-card-title>
    <v-card-text
      :class="`${this.$vuetify.theme.dark ? 'black--text' : 'white--text'} text-center pa-2`"
    >
      {{ $t("app_description") }}
    </v-card-text>
    <v-card-subtitle
      :class="`text-center justify-center mt-6 ${
        this.$vuetify.theme.dark ? 'black--text' : 'white--text'
      }`"
    >
      <v-btn
        icon
        v-for="(item, i) in social"
        :key="i"
        :href="item.link"
        target="_blank"
        :light="$vuetify.theme.dark"
        :dark="!$vuetify.theme.dark"
      >
        <v-icon>{{ item.icon }}</v-icon>
      </v-btn>
    </v-card-subtitle>
    <v-card-subtitle
      class="text-center justify-center"
    >
      <a
        :class="`${this.$vuetify.theme.dark ? 'black--text' : 'white--text'} text-center pa-2`"
        :href="this.$store.state.repo_info.branch_info[0].active_branch_url"
      >
        {{ this.$store.state.repo_info.branch_info[0].active_branch }}
      </a>
    </v-card-subtitle>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

interface BanerData {
  social: any;
}

export default Vue.extend({
  name: "Baner",
  data: (): BanerData => ({
    social: [
      {
        icon: "mdi-web",
        link: "https://wulkanowy.github.io",
      },
      {
        icon: "mdi-github",
        link: "https://github.com/wulkanowy",
      },
      {
        icon: "mdi-twitter",
        link: "https://twitter.com/wulkanowy",
      },
      {
        icon: "mdi-facebook",
        link: "https://facebook.com/wulkanowy",
      },
      {
        icon: "mdi-discord",
        link: "https://discord.gg/vccAQBr",
      },
    ],
  }),
});
</script>
