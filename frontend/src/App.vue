<script setup lang="ts">
import { RouterView } from 'vue-router'
import useUserStore from "@/stores/modules/user";
import { onMounted } from "vue";

const userStore = useUserStore();


</script>

<template>
  <Toast position="top-right"/>
  <RouterView/>
</template>

<style lang="stylus" scoped>

</style>
