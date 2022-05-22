<template>
  <div id="app-bar">
    <v-app-bar app clipped-left>
      <v-btn icon @click="$store.commit('drawer_show')">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
      <v-btn icon @click="$store.commit('drawer_mini')" v-if="!$store.state.small_ui">
        <v-icon v-if="$store.state.drawer.mini">mdi-chevron-right</v-icon>
        <v-icon v-else>mdi-chevron-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{ this.$store.state.view }}</v-toolbar-title>
      <v-spacer />
      <AccountManager />
    </v-app-bar>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import AccountManager from "../../components/Panel/AccountManager.vue";

export default Vue.extend({
  name: "AppBar",
  components: { AccountManager },
});
</script>
