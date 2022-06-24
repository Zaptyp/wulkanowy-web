<template>
  <div id="panel" class="fill-height">
    <AppBar />
    <Drawer />
    <v-main class="fill-height">
        <v-window v-model="$store.state.view" touchless class="fill-height">
          <v-window-item transition="false" value="dashboard">this is dashbaord</v-window-item>
          <v-window-item transition="false" value="grades">this is grades</v-window-item>
          <v-window-item transition="false" value="attedance">this is attedance</v-window-item>
          <v-window-item transition="false" value="timetable">this is timetable</v-window-item>
          <v-window-item transition="false" value="exams">this is exams</v-window-item>
          <v-window-item transition="false" value="homework">this is homework</v-window-item>
          <v-window-item transition="false" value="notes"
            >this is notes</v-window-item
          >
          <v-window-item transition="false" value="lucky_number"
            >this is lucky number</v-window-item
          >
          <v-window-item transition="false" value="conferences" class="fill-height"><Conferences/></v-window-item>
          <v-window-item transition="false" value="school_annocuments"
            >this is school annocuments</v-window-item
          >
          <v-window-item transition="false" value="student_data"
            >this is student data</v-window-item
          >
          <v-window-item transition="false" value="school_info"
            >this is school and teachers</v-window-item
          >
          <v-window-item transition="false" value="mobile_devices"
            >this is mobile devices</v-window-item
          >
          <v-window-item transition="false" value="messages">this is messages</v-window-item>
          <v-window-item transition="false" value="settings"><Settings/></v-window-item>
        </v-window>
    </v-main>
    <Snackbar/>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { AppBar, Drawer, Settings, Conferences, Snackbar } from "@/components";

export default Vue.extend({
  name: "Panel",

  components: {
    AppBar,
    Drawer,
    Snackbar,
    Settings,
    Conferences
  },

  beforeMount() {
    if (!this.$store.state.logged_in) {
      this.$router.push("/");
    }
  },
});
</script>

