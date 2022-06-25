<template>
  <div id="account-manager">
    <v-dialog width="450" scrollable>
      <template #activator="{ on }">
        <v-btn icon v-on="on">
          <v-avatar color="primary" class="white--text">{{
            initials
          }}</v-avatar>
        </v-btn>
      </template>
      <template #default="dialog">
        <v-card>
          <v-card-title>{{ $t("login.select_student_header") }}</v-card-title>
          <v-divider></v-divider>
          <div id="login-students-list" class="overflow-y-auto">
            <v-list>
              <v-list-item-group
                color="primary"
                v-model="$store.state.selected_student"
                mandatory
              >
                <div
                  class="symbol"
                  v-for="(symbol, symbol_index) in $store.state.loginData
                    .symbols"
                  :key="symbol_index"
                >
                  <div
                    class="school"
                    v-for="(school, school_index) in symbol.schools"
                    :key="school_index"
                  >
                    <v-list-item
                      v-for="(student, student_index) in school.students"
                      :key="student_index"
                      :value="{
                        symbol: symbol_index,
                        school: school_index,
                        student: student_index,
                        register: 0,
                      }"
                    >
                      <template #default="{ active }">
                        <v-list-item-action>
                          <v-icon
                            :color="active ? 'primary' : ''"
                            v-text="
                              active
                                ? 'mdi-radiobox-marked'
                                : 'mdi-radiobox-blank'
                            "
                          />
                        </v-list-item-action>
                        <v-list-item-content>
                          <v-list-item-title>
                            {{ student.student_name }}
                            {{ student.student_second_name }}
                            {{ student.student_surname }}
                          </v-list-item-title>
                          <v-list-item-subtitle>{{
                            school.name
                          }}</v-list-item-subtitle>
                        </v-list-item-content>
                      </template>
                    </v-list-item>
                  </div>
                </div>
              </v-list-item-group>
            </v-list>
          </div>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer />
            <v-btn text color="primary" @click="$store.commit('log_out')">{{
              $t("log_out")
            }}</v-btn>
            <v-btn text color="primary" @click="dialog.value = false">{{
              $t("close")
            }}</v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "AccountManager",
  computed: {
    students() {
      return this.$store.state.loginData.students;
    },
    initials() {
      const studentData = this.$store.state.selected_student;
      return (
        this.$store.state.loginData.symbols[studentData.symbol].schools[
          studentData.school
        ].students[studentData.student].student_name.charAt(0) +
        this.$store.state.loginData.symbols[studentData.symbol].schools[
          studentData.school
        ].students[studentData.student].student_surname.charAt(0)
      );
    },
  },
});
</script>
