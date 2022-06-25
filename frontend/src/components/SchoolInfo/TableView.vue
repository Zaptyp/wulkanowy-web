<template>
  <div id="tableView" style="width: 100%;">
    <v-row :no-gutters="$store.state.small_ui" class="fill-height" >
        <v-col cols="12">
          <v-subheader>{{ $t('school_info.school') }}</v-subheader>
          <v-card :flat="$store.state.small_ui">
          <v-simple-table>
            <tbody>
              <tr>
                <td>{{ $t('school_info.school_name') }}</td>
                <td>{{ schoolInfo.school.name || '-' }}</td>
              </tr>
              <tr>
                <td>{{ $t('school_info.school_address') }}</td>
                <td>{{ schoolInfo.school.address || '-' }}</td>
              </tr>
              <tr>
                <td>{{ $t('school_info.telephone') }}</td>
                <td>{{ schoolInfo.school.contact || '-' }}</td>
              </tr>
              <tr>
                <td>{{ $t('school_info.name_of_headmaster') }}</td>
                <td>{{ schoolInfo.school.headmaster || '-' }}</td>
              </tr>
              <tr>
                <td>{{ $t('school_info.name_of_pedagogue') }}</td>
                <td>{{ schoolInfo.school.pedagogue || '-' }}</td>
              </tr>
            </tbody>
          </v-simple-table>
          </v-card>
        </v-col>
        <v-col cols="12">
          <v-subheader>{{ $t('school_info.teachers') }}</v-subheader>
          <v-card :flat="$store.state.small_ui">
          <v-simple-table>
            <thead>
              <tr>
                <th>{{ $t('school_info.subject') }}</th>
                <th>{{ $t('school_info.teacher') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(teacher, index) in schoolInfo.teachers" :key="index">
                <td>{{ teacher.subject }}</td>
                <td>{{ teacher.name }}</td>
              </tr>
            </tbody>
          </v-simple-table>
          </v-card>
        </v-col>
      </v-row>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "TableView",
  props: ["schoolInfo"]
})
</script>
