<template>
  <div id="schoolInfo">
    {{ schoolInfo }}
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Api from "@/api";

export default Vue.extend({
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
