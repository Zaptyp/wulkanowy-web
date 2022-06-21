<template>
  <div id="register-switcher">
    <v-dialog width="450" scrollable>
      <template #activator="{ on }">
        <v-btn icon v-on="on">
          <v-icon>mdi-calendar-clock</v-icon>
        </v-btn>
      </template>
      <template #default="dialog">
        <v-card>
          <v-card-title>{{ $t("login.select_register_header") }}</v-card-title>
          <v-divider></v-divider>
          <div class="overflow-y-auto">
            <v-list>
              <v-list-item-group
                color="primary"
                v-model="$store.state.selected_student.register"
                mandatory
              >
                <v-list-item
                  v-for="(register, register_index) in $store.state.loginData
                    .symbols[$store.state.selected_student.symbol].schools[
                    $store.state.selected_student.school
                  ].students[$store.state.selected_student.student].registers"
                  :key="register_index"
                  :value="register_index"
                >
                  <template #default="{ active }">
                    <v-list-item-action>
                      <v-icon
                        :color="active ? 'primary' : ''"
                        v-text="
                          active ? 'mdi-radiobox-marked' : 'mdi-radiobox-blank'
                        "
                      />
                    </v-list-item-action>
                    <v-list-item-content>
                      <v-list-item-title>
                        {{ register.level }}{{ register.symbol }}
                        -
                        {{ register.year }}
                      </v-list-item-title>
                    </v-list-item-content>
                  </template>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </div>
          <v-divider></v-divider>
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
  name: "RegisterSwitchers",
});
</script>
