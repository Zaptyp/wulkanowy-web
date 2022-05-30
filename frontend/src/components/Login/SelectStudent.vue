<template>
  <div id="select-student" class="fill-height">
    <v-form @submit.prevent="select_student" class="fill-height d-flex flex-column">
      <v-card-title class="d-flex justify-center">{{ $t("login.select_student_header") }}</v-card-title>
      <div id="login-students-list" class="overflow-y-auto">
        <v-list>
          <v-list-item-group color="primary" v-model="$store.state.selected_student" mandatory>
            <v-list-item
              v-for="(student, id) in this.$store.state.loginData.students"
              :key="id"
              :value="id"
            >
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
      <v-card-actions class="px-5 pb-5 pt-0 mt-auto">
        <v-spacer />
        <v-btn color="primary" type="submit">{{ $t("login.sign_in") }}</v-btn>
      </v-card-actions>
    </v-form>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "SelectStudent",

  methods: {
    select_student() {
      this.$router.push("/user");
    },
  },
});
</script>

<style lang="scss" scoped>
@media only screen and (min-width: 960px) {
  #login-students-list {
    max-height: 410px;
  }
}

.theme--dark.v-btn {
  color: #1e1e1e !important;
}
</style>
