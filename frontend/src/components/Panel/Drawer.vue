<template>
  <div>
    <v-navigation-drawer
      app
      v-model="this.$store.state.drawer"
      :mini-variant.sync="mini"
      pernament>
      <v-list>
        <v-list-item class="px-2">
          <v-list-item-avatar>
            <v-icon>mdi-account</v-icon>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="title">
              {{ nameSurname }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ className }}</v-list-item-subtitle>
          </v-list-item-content>
          <v-btn
            icon
            @click.stop="mini = !mini">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list
        nav
        dense>
        <v-list-item-group
          v-model="this.$store.state.group">
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-numeric-6-box-multiple-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Grades</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-table</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Attendance</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-table-clock</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Timetable</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-email-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Messages</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-notebook-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Homework</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-devices</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Mobile Devices</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-domain</v-icon>
            </v-list-item-icon>
            <v-list-item-title>School</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: 'Drawer',
  data: () => ({
    mini: false,
    nameSurname: '',
    className: '',
  }),
  beforeMount() {
    const index = this.$store.state.selectedStudent;
    this.nameSurname = `${this.getName(index)} ${this.getSurname(index)}`;
    this.className = this.getClassName(index);
  },
  methods: {
    getName(index) {
      return this.$store.state.loginData.data.students.data[index].UczenImie;
    },
    getSurname(index) {
      return this.$store.state.loginData.data.students.data[index].UczenNazwisko;
    },
    getClassName(index) {
      return this.$store.state.loginData.data.students.data[index].Poziom.toString()
        + this.$store.state.loginData.data.students.data[index].Symbol;
    },
  },
};
</script>

<style scoped>

</style>
