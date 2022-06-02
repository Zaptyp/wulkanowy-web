<template>
  <div id="grades-semester-switch">
    <v-dialog width="350">
      <template #activator="{ on }">
        <v-btn icon v-on="on">
          <v-icon>mdi-calendar-multiple</v-icon>
        </v-btn>
      </template>
      <template #default="dialog">
        <v-card>
          <v-card-title>{{ $t("grades.switch_semester") }}</v-card-title>
          <v-list>
            <v-list-item-group
              v-model="$store.state.grades.semester"
              color="primary"
            >
              <v-list-item
                v-for="(semester, i) in getSemesters"
                :key="i"
                :value="semester.id"
              >
                <template #default="{ active }">
                  <v-list-item-icon>
                    <v-icon
                      :color="active ? 'primary' : ''"
                      v-text="
                        active ? 'mdi-radiobox-marked' : 'mdi-radiobox-blank'
                      "
                    />
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ $t("grades.semester") }}
                      {{ semester.number }}
                    </v-list-item-title>
                  </v-list-item-content>
                </template>
              </v-list-item>
            </v-list-item-group>
          </v-list>
          <v-card-actions>
            <v-spacer />
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
  name: "SemesterSwitch",
  computed: {
    getSemesters() {
      const selectedStudent = this.$store.state.selected_student;
      return this.$store.state.loginData.symbols[selectedStudent.symbol]
        .schools[selectedStudent.school].students[selectedStudent.student]
        .semesters;
    },
  },
  created() {
    this.$store.state.grades.semester =
      this.getSemesters[
        this.getSemesters.findIndex((item: any) => item.current === true)
      ].id;
  },
});
</script>
