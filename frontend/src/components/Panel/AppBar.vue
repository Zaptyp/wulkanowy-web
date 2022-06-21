<template>
  <div id="app-bar">
    <v-app-bar app clipped-left>
      <v-btn icon @click="$store.commit('drawer_show')">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
      <v-btn
        icon
        @click="$store.commit('drawer_mini')"
        v-if="!$store.state.small_ui"
      >
        <v-icon v-if="$store.state.drawer.mini">mdi-chevron-right</v-icon>
        <v-icon v-else>mdi-chevron-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{
        $t("nav_items." + this.$store.state.view)
      }}</v-toolbar-title>
      <v-spacer />
      <RegistersSwitcher
        v-if="
          $store.state.loginData.symbols[$store.state.selected_student.symbol]
            .schools[$store.state.selected_student.school].students[
            $store.state.selected_student.student
          ].registers.length > 1
        "
      />
      <AccountManager />
    </v-app-bar>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import AccountManager from "../../components/Panel/AccountManager.vue";
import RegistersSwitcher from "./RegistersSwitcher.vue";

export default Vue.extend({
  name: "AppBar",
  components: { AccountManager, RegistersSwitcher },
});
</script>
