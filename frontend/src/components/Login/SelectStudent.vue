<template>
<div>
  <v-row align="center">
    <v-col cols="12">
      <p class="justify-center text-center headline font-weight-light">Wybierz Ucznia</p>
    </v-col>
    <v-col cols="12">
      <v-radio-group>
        <v-radio
          v-model="selectedStudent"
          v-for="student in this.$store.state.loginData.data.students.data"
          :key="student.UczenPelnaNazwa"
          :label="student.UczenPelnaNazwa">
        </v-radio>
      </v-radio-group>
    </v-col>
    <v-col cols="12">
      <v-btn
        dark
        color="red"
        elevation="2"
        @click="chooseClicked()"
        :disabled="inputDisabled"
      >Wybierz</v-btn>
    </v-col>
  </v-row>
</div>
</template>

<script>
export default {
  name: 'SelectStudent',
  data() {
    return {
      itemSelected: '',
      radioGroup: 1,
      selectedStudent: '',
      studentList: {
        type: Array,
      },
    };
  },
  beforeMount() {
    console.log(this.$store.state.loginData.data.students.data[0]);
  },
  methods: {
    async chooseClicked() {
      this.$store.state.selectedUser = this.selectedStudent;
      this.$store.state.showStudentsList = true;
      await this.$router.push('/user');
    },
    back() {
      this.$store.state.showStudentsList = false;
    },
  },
};
</script>
