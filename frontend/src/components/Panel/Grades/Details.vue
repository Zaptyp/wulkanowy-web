<template>
  <div id="grades-details">
    {{ this.grades }}
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Api from "@/api";

export default Vue.extend({
  name: "GradesDetails",
  data: () => ({
    grades: []
  }),
  methods: {
    async getGrades() {
      this.$store.state.loading = true;
      const studentData = this.$store.state.selected_student;
      const response = await Api.get_grades(
        this.$store.state.loginData.host,
        this.$store.state.loginData.symbols[studentData.symbol].name,
        this.$store.state.loginData.symbols[studentData.symbol].schools[studentData.school].id,
        this.$store.state.loginData.ssl,
        this.$store.state.loginData.symbols[studentData.symbol].schools[studentData.school].headers,
        this.$store.state.loginData.symbols[studentData.symbol].schools[studentData.school].students[studentData.student].cookies,
        this.$store.state.loginData.symbols[studentData.symbol].session_data,
        { okres: this.$store.state.grades.semester }
      )
      if (response) {
        this.grades = response.data;
      }
    }
  },
  beforeMount() {
    this.$store.state.grades.semesterId =
      this.getSemesters[
        this.getSemesters.findIndex((item: any) => item.current === true)
      ].id;
    this.getGrades();
  },
  computed: {
    getSemesters() {
      const selectedStudent = this.$store.state.selected_student;
      return this.$store.state.loginData.symbols[selectedStudent.symbol]
        .schools[selectedStudent.school].students[selectedStudent.student]
        .semesters;
    },
  },
  watch: {
    "$store.state.selected_student": {
      handler() {
        this.$store.state.grades.semester =
          this.getSemesters[
            this.getSemesters.findIndex((item: any) => item.current === true)
          ].id;
        this.getGrades();
      },
    },
    "$store.state.grades.semesterId": {
      handler() {
        this.getGrades();
      },
    },
  },
});
</script>
