<template>
  <div id="schoolInfo">
    <v-container fluid :style="$store.state.small_ui ? 'padding: 0;' : ''" class="fill-height">
      <v-row :no-gutters="$store.state.small_ui" class="fill-height" v-if="!$store.state.tableView && !$store.state.small_ui">
        <v-col cols="12">
          <v-subheader>{{ $t('school_info.school') }}</v-subheader>
          <School :school="schoolInfo.school"/>
        </v-col>
        <v-col cols="12">
          <v-subheader>{{ $t('school_info.teachers') }}</v-subheader>
          <Teachers :teachers="schoolInfo.teachers" v-if="schoolInfo.teachers.length"/>
        </v-col>
      </v-row>
      <v-tabs-items v-model="$store.state.schoolInfoTabs" v-if="$store.state.small_ui && !$store.state.tableView" style="width: 100%;">
        <v-tab-item :value="0"><School :school="schoolInfo.school"/></v-tab-item>
        <v-tab-item :value="1"><Teachers :teachers="schoolInfo.teachers" v-if="schoolInfo.teachers.length"/></v-tab-item>
      </v-tabs-items>
      <TableView :schoolInfo="schoolInfo" v-if="$store.state.tableView"/>
    </v-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import School from "./School.vue";
import Teachers from "./Teachers.vue";
import TableView from "./TableView.vue";
import Api from "@/api";

export default Vue.extend({
  name: "SchoolInfo",
  components: { School, Teachers, TableView },
  data: () => ({
    schoolInfo: {},
  }),
  methods: {
    async getSchoolInfo() {
      this.$store.state.loading = true;
      const selectedStudent = this.$store.state.selected_student;
      const response = await Api.uonetplusUczenReqeust(
        this.$store.state.loginData.host,
        this.$store.state.loginData.symbols[selectedStudent.symbol].name,
        this.$store.state.loginData.symbols[selectedStudent.symbol].schools[
          selectedStudent.school
        ].id,
        this.$store.state.loginData.ssl,
        "school-info",
        this.$store.state.loginData.symbols[selectedStudent.symbol].schools[
          selectedStudent.school
        ].headers,
        this.$store.state.loginData.symbols[selectedStudent.symbol].schools[
          selectedStudent.school
        ].students[selectedStudent.student].registers[selectedStudent.register]
          .cookies,
        this.$store.state.loginData.symbols[selectedStudent.symbol]
          .session_data,
        {}
      );
      if (response) {
          this.schoolInfo = response.data;
      } else {
        this.schoolInfo = {};
      }
      this.$store.state.loading = false;
    },
  },
  watch: {
    '$store.state.selected_student': {
      handler() {
        this.getSchoolInfo();
      },
    },
    '$store.state.selected_student.register': {
      handler() {
        this.getSchoolInfo();
      },
    },
  },
  beforeMount() {
    this.getSchoolInfo();
  },
});
</script>
