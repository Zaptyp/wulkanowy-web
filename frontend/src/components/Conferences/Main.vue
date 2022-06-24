<template>
  <div id="conferences">
    <v-container fluid :style="$store.state.small_ui ? 'padding: 0;' : ''">
      <v-row :no-gutters="$store.state.small_ui">
        <v-col cols="12" v-if="!$store.state.tableView && conferences">
          <v-card :flat="$store.state.small_ui">
            <v-list>
              <Conference
                v-for="(conference, index) in conferences"
                :key="index"
                :conference="conference"
              />
            </v-list>
          </v-card>
        </v-col>
        <v-col cols="12" v-if="$store.state.tableView && conferences">
          <v-card>
            <v-simple-table class="table">
              <thead>
                  <tr>
                  <th>{{$t('conferences.subject')}}</th>
                  <th>{{$t('conferences.date')}}</th>
                  <th>{{ $t('conferences.place') }}</th>
                  <th>{{$t('conferences.present_on_conference')}}</th>
                  <th>{{$t('conferences.agenda')}}</th>
                  <th>{{$t('conferences.conference_link')}}</th>
                  </tr>
              </thead>
              <tbody>
                <tr v-for="(conference, index) in conferences" :key="index">
                  <td>{{ conference.subject || '-' }}</td>
                  <td>{{ conference.date || '-' }}</td>
                  <td>{{ conference.place || '-' }}</td>
                  <td>{{ conference.present_on_conference || '-' }}</td>
                  <td>{{ conference.agenda || '-' }}</td>
                  <td>{{ conference.conference_link || '-' }}</td>
                </tr>
              </tbody>
            </v-simple-table>
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
