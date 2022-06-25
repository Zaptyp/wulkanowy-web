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
      <v-btn v-if="$store.state.view == 'conferences' || $store.state.view == 'school_info'" @click="$store.commit('tableView')" icon>
        <v-icon v-if="!$store.state.tableView">mdi-table-eye</v-icon>
        <v-icon v-if="$store.state.tableView">mdi-table-eye-off</v-icon>
      </v-btn>
      <RegistersSwitcher
        v-if="
          $store.state.loginData.symbols[$store.state.selected_student.symbol]
            .schools[$store.state.selected_student.school].students[
            $store.state.selected_student.student
          ].registers.length > 1
        "
      />
      <AccountManager />
      <v-progress-linear
        :active="$store.state.loading"
        indeterminate
        absolute
        bottom
        color="primary"
      />
      <template #extension v-if="$store.state.small_ui && $store.state.view == 'school_info' && !$store.state.tableView && !$store.state.loading">
        <v-tabs grow v-model="$store.state.schoolInfoTabs">
          <v-tab>{{ $t('school_info.school') }}</v-tab>
          <v-tab>{{ $t('school_info.teachers') }}</v-tab>
        </v-tabs>
      </template>
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
