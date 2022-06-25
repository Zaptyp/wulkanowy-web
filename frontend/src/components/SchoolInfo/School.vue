<template>
  <div id="school">
    <v-card :flat="$store.state.small_ui">
      <v-list>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle>{{ $t('school_info.school_name') }}</v-list-item-subtitle>
            <v-list-item-title style="white-space: normal !important">{{ school.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle>{{ $t('school_info.school_address') }}</v-list-item-subtitle>
            <v-list-item-title style="white-space: normal !important">{{ school.address }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle>{{ $t('school_info.telephone') }}</v-list-item-subtitle>
            <v-list-item-title style="white-space: normal !important">{{ school.contact }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle>{{ $t('school_info.name_of_headmaster') }}</v-list-item-subtitle>
            <v-list-item-title style="white-space: normal !important">{{ school.headmaster }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle>{{ $t('school_info.name_of_pedagouge') }}</v-list-item-subtitle>
            <v-list-item-title style="white-space: normal !important">{{ school.pedagogue }}</v-list-item-title>
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
  props: ["school"]
})
</script>
