<template>
  <div id="grade">
    <v-dialog width="450">
      <template #activator="{ on }">
        <v-list-item v-on="on">
          <v-list-item-avatar
            rounded
            :color="
              grade.entry === '1-' ||
              grade.entry === '1' ||
              grade.entry === '1+'
                ? 'grade_material_one'
                : grade.entry === '2-' ||
                  grade.entry === '2' ||
                  grade.entry === '2+'
                ? 'grade_material_two'
                : grade.entry === '3-' ||
                  grade.entry === '3' ||
                  grade.entry === '3+'
                ? 'grade_material_three'
                : grade.entry === '4-' ||
                  grade.entry === '4' ||
                  grade.entry === '4+'
                ? 'grade_material_four'
                : grade.entry === '5-' ||
                  grade.entry === '5' ||
                  grade.entry === '5+'
                ? 'grade_material_five'
                : grade.entry === '6-' ||
                  grade.entry === '6' ||
                  grade.entry === '6+'
                ? 'grade_material_six'
                : 'grade_material_default'
            "
          >
            <span class="white--text text-h6">{{ grade.entry }}</span>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>
              <span v-if="grade.description">{{ grade.description }}</span>
              <span v-else-if="grade.symbol">{{ grade.symbol }}</span>
              <span v-else>No description</span>
            </v-list-item-title>
            <v-list-item-subtitle>
              {{ grade.date ? grade.date : "" }}
              {{
                grade.weight_value
                  ? `${$t("grades.details.weight")}: ${grade.weight_value}`
                  : ""
              }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
      <template #default="dialog">
        <v-card>
          <v-card-title>{{ subject }}</v-card-title>
          <v-card-subtitle v-if="grade.symbol || grade.description">
            <span v-if="grade.symbol && grade.description"
              >{{ grade.symbol }} - {{ grade.description }}</span
            >
            <span v-else-if="!grade.symbol && grade.description">{{
              grade.description
            }}</span>
            <span v-else>{{ grade.symbol }}</span>
          </v-card-subtitle>
          <v-card-text>
            <v-list class="grade-list">
              <v-list-item v-if="grade.entry">
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("grades.details.grade")
                  }}</v-list-item-subtitle>
                  <v-list-item-title>{{ grade.entry }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item v-if="grade.weight_value">
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("grades.details.weight")
                  }}</v-list-item-subtitle>
                  <v-list-item-title>{{
                    grade.weight_value
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item v-if="grade.date">
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("grades.details.date")
                  }}</v-list-item-subtitle>
                  <v-list-item-title>{{ grade.date }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item v-if="grade.comment">
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("grades.details.comment")
                  }}</v-list-item-subtitle>
                  <v-list-item-title>{{ grade.comment }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item v-if="grade.teacher">
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("grades.details.teacher")
                  }}</v-list-item-subtitle>
                  <v-list-item-title>{{ grade.teacher }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item v-if="grade.color">
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("grades.details.color")
                  }}</v-list-item-subtitle>
                  <v-list-item-title>{{
                    $t(`grades.details.colors.${grade.color}`)
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
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
  name: "Grade",
  props: ["grade", "subject"],
});
</script>

<style lang="scss" scoped>
.grade-list .v-list-item {
  padding: 0 !important;
}
</style>
