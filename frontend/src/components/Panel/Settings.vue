<template>
  <div id="settings">
    <v-container fluid>
      <v-row>
        <v-col>
          <v-subheader>{{ $t('settings.apperance_title') }}</v-subheader>
          <v-card>
            <v-list>
              <v-dialog scrollable width="300">
                <template #activator="{ on }">
                  <v-list-item v-on="on">
                    <v-list-item-content>
                      <v-list-item-title>{{ $t('settings.theme_header') }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </template>
                <template #default="dialog">
                  <v-card>
                    <v-card-title>{{ $t('settings.theme_header') }}</v-card-title>
                    <v-list-item-group v-model="$vuetify.theme.dark" mandatory color="primary">
                      <v-list class="overflow-y-auto">
                        <v-list-item :value="false">
                          <template #default="{ active }">
                            <v-list-item-action>
                              <v-icon
                                :color="active ? 'primary' : ''"
                                v-text="active ? 'mdi-radiobox-marked' : 'mdi-radiobox-blank'"
                              />
                            </v-list-item-action>
                            <v-list-item-content>
                              <v-list-item-title>{{ $t('settings.theme_light') }}</v-list-item-title>
                            </v-list-item-content>
                          </template>
                        </v-list-item>
                        <v-list-item :value="true">
                          <template #default="{ active }">
                            <v-list-item-action>
                              <v-icon
                                :color="active ? 'primary' : ''"
                                v-text="active ? 'mdi-radiobox-marked' : 'mdi-radiobox-blank'"
                              />
                            </v-list-item-action>
                            <v-list-item-content>
                              <v-list-item-title>{{ $t('settings.theme_dark') }}</v-list-item-title>
                            </v-list-item-content>
                          </template>
                        </v-list-item>
                      </v-list>
                    </v-list-item-group>
                    <v-card-actions>
                      <v-spacer />
                      <v-btn text color="primary" @click="dialog.value = false">{{ $t("close") }}</v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
              <v-dialog scrollable width="300">
                <template #activator="{ on }">
                  <v-list-item v-on="on">
                    <v-list-item-content>
                      <v-list-item-title>{{ $t('settings.app_language') }}</v-list-item-title>
                      <v-list-item-subtitle>{{ language_name }}</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </template>
                <template #default="dialog">
                  <v-card>
                    <v-card-title>{{ $t('settings.app_language') }}</v-card-title>
                    <v-list-item-group v-model="$i18n.locale" mandatory color="primary">
                      <v-list class="overflow-y-auto">
                        <v-list-item v-for="(language, i) in languages" :key="i" :value="language.value">
                          <template #default="{ active }">
                            <v-list-item-action>
                              <v-icon
                                :color="active ? 'primary' : ''"
                                v-text="active ? 'mdi-radiobox-marked' : 'mdi-radiobox-blank'"
                              />
                            </v-list-item-action>
                            <v-list-item-content>
                              <v-list-item-title>{{ language.name }}</v-list-item-title>
                            </v-list-item-content>
                          </template>
                        </v-list-item>
                      </v-list>
                    </v-list-item-group>
                    <v-card-actions>
                      <v-spacer />
                      <v-btn text color="primary" @click="dialog.value = false">{{ $t("close") }}</v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import languages from '@/assets/res/languages.json';
export default Vue.extend({
  name: 'Settings',
  data: () => ({
    languages: languages,
    language: '',
  }),
  computed: {
    language_name() {
      return languages[
        languages.findIndex(
          (item) => item.value === this.$i18n.locale
        )
      ].name;
    },
  },
})
</script>