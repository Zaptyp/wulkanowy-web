<template>
  <div class="conference">
    <v-dialog width="450">
      <template #activator="{ on }">
        <v-list-item lines="four" v-on="on">
          <v-list-item-content>
            <p class="d-flex">
              <span>{{ conference.date || $t("conferences.no_date") }}</span>
              <v-spacer />
              <span>{{ conference.place || $t("conferences.no_place") }}</span>
            </p>
            <v-list-item-title>{{
              conference.subject || $t("conferences.no_subject")
            }}</v-list-item-title>
            <v-list-item-subtitle style="white-space: pre-wrap !important">{{
              conference.agenda
            }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
      <template #default="dialog">
        <v-card>
          <v-card-title>
            {{ $t("details") }}
          </v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item
                style="padding: 0 !important"
                v-if="conference.subject"
              >
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("conferences.subject")
                  }}</v-list-item-subtitle>
                  <v-list-item-title style="white-space: normal !important">{{
                    conference.subject
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item style="padding: 0 !important" v-if="conference.date">
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("conferences.date")
                  }}</v-list-item-subtitle>
                  <v-list-item-title style="white-space: normal !important">{{
                    conference.date
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item
                style="padding: 0 !important"
                v-if="conference.place"
              >
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("conferences.place")
                  }}</v-list-item-subtitle>
                  <v-list-item-title style="white-space: normal !important">{{
                    conference.place
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item
                style="padding: 0 !important"
                v-if="conference.present_at_conference"
              >
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("conferences.present_at_conference")
                  }}</v-list-item-subtitle>
                  <v-list-item-title style="white-space: normal !important">{{
                    conference.present_at_conference
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item
                style="padding: 0 !important"
                v-if="conference.agenda"
              >
                <v-list-item-content>
                  <v-list-item-subtitle>{{
                    $t("conferences.agenda")
                  }}</v-list-item-subtitle>
                  <v-list-item-title style="white-space: pre-wrap !important">{{
                    conference.agenda
                  }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions>
            <v-btn
              text
              color="primary"
              :href="conference.online"
              v-if="conference.online"
              >{{ $t("conferences.join_to_online_conference") }}</v-btn
            >
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
  props: ["conference"],
});
</script>
