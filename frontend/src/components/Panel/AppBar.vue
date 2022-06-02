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
      <v-window v-model="$store.state.view" touchless>
        <v-window-item transition="false" value="dashboard"></v-window-item>
        <v-window-item transition="false" value="grades">
          <GradesSemesterSwitch />
        </v-window-item>
        <v-window-item transition="false" value="attedance"></v-window-item>
        <v-window-item transition="false" value="timetable"></v-window-item>
        <v-window-item transition="false" value="exams"></v-window-item>
        <v-window-item transition="false" value="homework"></v-window-item>
        <v-window-item transition="false" value="notes"></v-window-item>
        <v-window-item transition="false" value="lucky_number"></v-window-item>
        <v-window-item transition="false" value="conferences"></v-window-item>
        <v-window-item
          transition="false"
          value="school_annocuments"
        ></v-window-item>
        <v-window-item transition="false" value="student_data"></v-window-item>
        <v-window-item transition="false" value="school_info"></v-window-item>
        <v-window-item
          transition="false"
          value="mobile_devices"
        ></v-window-item>
        <v-window-item transition="false" value="messages"></v-window-item>
        <v-window-item transition="false" value="settings"></v-window-item>
      </v-window>
      <AccountManager />
      <template #extension v-if="$store.state.view == 'grades' && !$store.state.loading">
        <v-tabs grow v-model="$store.state.grades.view">
          <v-tab href="#details">{{ $t("grades.tabs.details") }}</v-tab>
          <v-tab href="#summary">{{ $t("grades.tabs.summary") }}</v-tab>
          <v-tab href="#class">{{ $t("grades.tabs.class") }}</v-tab>
        </v-tabs>
      </template>
      <v-progress-linear
        :active="$store.state.loading"
        indeterminate
        absolute
        bottom
        color="primary"
      />
    </v-app-bar>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import AccountManager from "@/components/Panel/AccountManager.vue";
import GradesSemesterSwitch from "@/components/Panel/Grades/SemesterSwitch.vue"

export default Vue.extend({
  name: "AppBar",
  components: { AccountManager, GradesSemesterSwitch },
});
</script>
