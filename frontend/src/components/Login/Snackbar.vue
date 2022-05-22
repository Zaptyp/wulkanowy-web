<template>
  <div id="snackbar">
    <v-snackbar v-model="$store.state.error.show">
      {{ this.$store.state.error.description }}
      <template #action="{ attrs }">
        <v-dialog width="650" v-if="$store.state.error.details">
          <template #activator="{ on }">
            <v-btn color="snackbar" text v-on="on">Details</v-btn>
          </template>
          <template #default="dialog">
            <v-card>
              <v-card-title>Details</v-card-title>
              <v-card-text>
                <v-alert text type="error">
                  {{ $store.state.error.description }}
                  <code class="d-block mt-3 py-2 px-sm-3">
                    {{ $store.state.error.details }}
                  </code>
                </v-alert>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn text color="primary" @click="dialog.value = false">Close</v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </v-dialog>
        <v-btn color="snackbar" text v-bind="attrs" @click="$store.state.error.show = false"
          >Close</v-btn
        >
      </template>
    </v-snackbar>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Snackbar",
});
</script>
