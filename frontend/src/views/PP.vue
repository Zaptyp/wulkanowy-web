<template>
  <div id="App">
    <v-main style="width: 100%;">
      <img class="image" src="../assets/logo_login.svg" alt="Wulkanowy">
      <v-card
        elevation="24"
        id="form"
        class="mx-auto">
          <v-row align="center">
            <v-col cols="12">
              <div id="nag">Polityka Prywatności</div>
            </v-col>
          </v-row>
        <v-col cols="12">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Maecenas eget tempor nulla.Nam vulputate nisi ac magna pulvinar,
        vitae aliquam lorem consectetur. In egetnplacerat ex, et tempor elit.
        Donec ac volutpat orci. Integer sagittis eget mi a blandit. Nullam
        ac quam a nisl elementum pretium vel sit amet augue. Praesent
        sollicitudin aliquam mi, et condimentum elit vehicula id.
        Pellentesque dapibus dolor nec nulla cursus bibendum.
        Cras enim tortor, feugiat at bibendum ut, ultricies
        non quam. Nulla at lorem non lorem tincidunt tempus.
        Pellentesque habitant morbi tristique senectus et netus et
        malesuada fames ac turpis egestas. Suspendisse at rutrum lectus.
        Nunc aliquet commodo scelerisque. Ut euismod pellentesque diam
        eget accumsan. Fusce eget elementum leo, sed auctor erat.
        </v-col>
      </v-card>
    </v-main>
  </div>
</template>

<script>
export default {
  name: 'PP',
  methods: {
    getLoading() {
      return this.$store.state.isLoading;
    },
  },
};
</script>

<style>
::-webkit-scrollbar {
  display: none;
}

#App {
  text-align: center;
  background-position: center center;
  overflow: hidden;
  background-image: url("../assets/wallpaper.jpg");
  background-size: cover;
  height: 100%;
  width: 100%;
}

#form {
  top: 5%;
  margin-bottom: 50px;
  width: 750px;
  padding: 20px;
  text-align: justify;
}

.image{
  max-width: 500px;
}
</style>
