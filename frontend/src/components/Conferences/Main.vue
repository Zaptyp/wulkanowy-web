<template>
  <div id="conferences">
    <v-container fluid :style="$store.state.small_ui ? 'padding: 0;' : ''">
      <v-row :no-gutters="$store.state.small_ui">
        <v-col>
          <v-card v-if="this.conferences" :flat="$store.state.small_ui">
            <v-list>
              <Conference
                v-for="(conference, index) in conferences"
                :key="index"
                :conference="conference"
              />
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Conference from "./Conference.vue";
import Api from "@/api";

export default Vue.extend({
  components: { Conference },
  data: () => ({
    conferences: undefined,
  }),
  methods: {
    async getConferences() {
      const selectedStudent = this.$store.state.selected_student;
      const response = await Api.getConferences(
        this.$store.state.loginData.host,
        this.$store.state.loginData.symbols[selectedStudent.symbol].name,
        this.$store.state.loginData.symbols[selectedStudent.symbol].schools[
          selectedStudent.school
        ].id,
        this.$store.state.loginData.ssl,
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
        this.conferences = response.data;
      }
    },
  },
  beforeMount() {
    this.getConferences();
  },
});
</script>
