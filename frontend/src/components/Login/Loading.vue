<template>
  <div id="loading" class="d-flex fill-height justify-center align-center">
    <v-progress-circular indeterminate color="primary" />
  </div>
</template>
<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Loading",
});
</script>
