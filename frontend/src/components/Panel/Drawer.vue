<template>
  <div id="drawer">
    <v-navigation-drawer
      :mini-variant="$store.state.drawer.mini && !$store.state.small_ui"
      v-model="$store.state.drawer.show"
      clipped
      app
    >
      {{ $store.state.view }}
      <v-list nav dense>
        <v-list-item-group v-model="$store.state.view" mandatory color="primary">
          <v-list-item v-for="(item, i) in nav" :key="i" :value="item.name">
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ $t("nav_items." + item.name) }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

interface DrawerData {
  nav: any;
}

export default Vue.extend({
  name: "Drawer",

  data: (): DrawerData => ({
    nav: [
      {
        icon: "mdi-view-dashboard-outline",
        name: "dashboard",
      },
      {
        icon: "mdi-numeric-6-box-multiple-outline",
        name: "grades",
      },
      {
        icon: "mdi-table-edit",
        name: "attedance",
      },
      {
        icon: "mdi-timetable",
        name: "timetable",
      },
      {
        icon: "mdi-calendar",
        name: "exams",
      },
      {
        icon: "mdi-notebook-outline",
        name: "homework",
      },
      {
        icon: "mdi-trophy-outline",
        name: "notes",
      },
      {
        icon: "mdi-clover",
        name: "lucky_number",
      },
      {
        icon: "mdi-account-multiple-outline",
        name: "conferences",
      },
      {
        icon: "mdi-alert-circle-outline",
        name: "school_annocuments",
      },
      {
        icon: "mdi-domain",
        name: "school_info",
      },
      {
        icon: "mdi-card-account-details-outline",
        name: "student_data",
      },
      {
        icon: "mdi-devices",
        name: "mobile_devices",
      },
      {
        icon: "mdi-email-outline",
        name: "messages",
      },
      {
        icon: "mdi-cog-outline",
        name: "settings",
      },
    ],
  }),
});
</script>
