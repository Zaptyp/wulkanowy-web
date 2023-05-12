<template>
  <div id="grades-view">
    <v-tabs-items v-model="$store.state.grades.view">
      <v-tab-item value="details">
        <GradesDetails />
      </v-tab-item>
      <v-tab-item value="summary">
        <GradesSummary />
      </v-tab-item>
      <v-tab-item value="class">
        <GradesClass />
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { GradesDetails, GradesSummary, GradesClass } from "@/components";

export default Vue.extend({
  components: { GradesDetails, GradesSummary, GradesClass }
})
</script>

<style lang="scss" scoped>
.theme--dark.v-tabs-items {
  background-color: #00000000 !important;
}
</style>
