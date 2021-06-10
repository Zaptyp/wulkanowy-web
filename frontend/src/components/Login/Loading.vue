<template>
<div id="App" style="height: 476px; margin: 0;">
  <v-row align="center">
    <v-col cols="12">
      <v-progress-circular
      indeterminate
      color="red"
      style="margin-top: 200px;"
      ></v-progress-circular>
    </v-col>
  </v-row>
</div>
</template>

<script>
export default {
  name: 'Loading',
};
</script>
