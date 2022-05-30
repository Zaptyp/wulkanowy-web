<template>
  <div id="account-manager">
    <v-dialog width="450" scrollable>
      <template #activator="{ on }">
        <v-btn icon v-on="on">
          <v-avatar color="primary" class="white--text">{{ initials }}</v-avatar>
        </v-btn>
      </template>
      <template #default="dialog">
        <v-card>
          <v-card-title>{{ $t("login.select_student_header") }}</v-card-title>
          <v-divider></v-divider>
          <div class="overflow-y-auto">
            <v-list>
              <v-list-item-group color="primary" v-model="$store.state.selected_student" mandatory>
                <v-list-item v-for="(student, id) in students" :key="id" :value="id">
                  <template #default="{ active }">
                    <v-list-item-action>
                      <v-icon
                        :color="active ? 'primary' : ''"
                        v-text="active ? 'mdi-radiobox-marked' : 'mdi-radiobox-blank'"
                      />
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>
                        {{ student.student_name }}
                        {{ student.student_second_name }}
                        {{ student.student_surname }}
                        {{ student.level }}{{ student.symbol }}
                      </v-list-item-title>
                      <v-list-item-subtitle>{{ student.school_name }}</v-list-item-subtitle>
                    </v-list-item-content>
                  </template>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </div>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer />
            <v-btn text color="primary" @click="$store.commit('log_out')">{{ $t("log_out") }}</v-btn>
            <v-btn text color="primary" @click="dialog.value = false">{{ $t("close") }}</v-btn>
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
      const index = this.$store.state.selected_student;
      return (
        this.$store.state.loginData.students[index].student_name.charAt(0) +
        this.$store.state.loginData.students[index].student_surname.charAt(0)
      );
    },
  },
});
</script>
