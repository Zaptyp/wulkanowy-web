import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#9a0007",
        error: "#ff5722",
        snackbar: "#e57373",
        
        grade_material_six: "#3dbbf5",
        grade_material_five: "#4caf50",
        grade_material_four: "#a0c431",
        grade_material_three: "#ffb940",
        grade_material_two: "#ff774d",
        grade_material_one: "#d43f3f",
        grade_material_default: "#607d8b",
      },
      dark: {
        primary: "#e57373",
        error: "#ff5722",
        snackbar: "#9a0007",
        
        grade_material_six: "#3dbbf5",
        grade_material_five: "#4caf50",
        grade_material_four: "#a0c431",
        grade_material_three: "#ffb940",
        grade_material_two: "#ff774d",
        grade_material_one: "#d43f3f",
        grade_material_default: "#607d8b",
      },
    },
  },
});
