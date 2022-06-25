<template>
  <div id="school">
    <v-card :flat="$store.state.small_ui">
      <v-list>
        <v-list-item v-for="(teacher, index) in teachers" :key="index">
          <v-list-item-content>
            <v-list-item-subtitle style="white-space: normal !important">{{ teacher.subject || $t('school_info.no_subject') }}</v-list-item-subtitle>
            <v-list-item-title style="white-space: normal !important">{{ teacher.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "School",
  props: ["teachers"]
})
</script>
