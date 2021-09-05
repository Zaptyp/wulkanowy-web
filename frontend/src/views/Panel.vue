<template>
<div id="App" style="margin: 0;">
    <div id="appbar">
      <Appbar></Appbar>
      <Drawer></Drawer>
    </div>
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

<style scoped>
</style>
