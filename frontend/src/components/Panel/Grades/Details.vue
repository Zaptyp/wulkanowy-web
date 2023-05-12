<template>
  <div id="grades-details">
    <v-container fluid :style="$store.state.small_ui ? 'padding: 0;' : ''">
      <v-row :no-gutters="$store.state.small_ui">
        <v-col>
          <v-card v-if="this.grades" :flat="$store.state.small_ui">
            <v-list>
              <v-list-group
                v-for="subject in grades.subjects"
                :key="subject.position"
                append-icon="mdi-menu-down"
                :disabled="!subject.grades.length"
              >
                <template #activator>
                  <v-list-item-content>
                    <v-list-item-title>{{ subject.name }}</v-list-item-title>
                    <v-list-item-subtitle>
                      {{
                        subject.average
                          ? `${$t("grades.average")}: ${subject.average}`
                          : $t("grades.no_average")
                      }}
                      {{
                        subject.points
                          ? `${$t("grades.details.points")}: ${subject.points}`
                          : ""
                      }}
                      {{
                        $tc("grades.details.grades", subject.grades.length, {
                          count: subject.grades.length,
                        })
                      }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </template>
                <Grade
                  v-for="(grade, grade_index) in subject.grades"
                  :key="grade_index"
                  :subject="subject.name"
                  :grade="grade"
                />
              </v-list-group>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Api from "@/api";
import Grade from "./Grade.vue";

export default Vue.extend({
  name: "GradesDetails",
  components: { Grade },
  data: () => ({
    grades: [],
  }),
  methods: {
    async getGrades() {
      this.$store.state.loading = true;
      const studentData = this.$store.state.selected_student;
      const response = await Api.get_grades(
        this.$store.state.loginData.host,
        this.$store.state.loginData.symbols[studentData.symbol].name,
        this.$store.state.loginData.symbols[studentData.symbol].schools[
          studentData.school
        ].id,
        this.$store.state.loginData.ssl,
        this.$store.state.loginData.symbols[studentData.symbol].schools[
          studentData.school
        ].headers,
        this.$store.state.loginData.symbols[studentData.symbol].schools[
          studentData.school
        ].students[studentData.student].cookies,
        this.$store.state.loginData.symbols[studentData.symbol].session_data,
        { okres: this.$store.state.grades.semesterId }
      );
      response.data.subjects = response.data.subjects.sort((a: any, b: any) =>
        a.name < b.name ? -1 : 1
      );
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
        this.$store.state.grades.semesterId =
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
