<template>
  <v-row align="center">
    <v-col cols="12">
      <a>Select student to login!</a>
    </v-col>
    <v-col cols="12">
      <v-radio-group>
        <v-radio
          v-model="selectedStudent"
          v-for="student in this.$store.data.data"
          :key="student.UczenPelnaNazwa">
        </v-radio>
      </v-radio-group>
    </v-col>
    <v-col cols="12">
      <v-btn
        class="login-button"
        depressed
        color="primary"
        @click="chooseClicked()">
        Choose</v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'SelectStudent',
  data() {
    return {
      radioGroup: 1,
      selectedStudent: '',
      studentList: {
        type: Array,
      },
    };
  },
  methods: {
    async chooseClicked() {
      this.$store.state.selectedUser = this.selectedStudent;
      this.$store.state.showStudentsList = true;
    },
  },
};
</script>

<style scoped>

</style>
