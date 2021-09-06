<template>
<div>
  <div id="appbar">
    <Appbar></Appbar>
    <Drawer></Drawer>
  </div>
  <v-main></v-main>
</div>
</template>

<script>
import Appbar from '../components/Panel/Appbar.vue';
import Drawer from '../components/Panel/Drawer.vue';

export default {
  name: 'Panel',
  components: {
    Appbar,
    Drawer,
  },
};
</script>
