<template>
  <header class="header w-screen h-3rem surface-100 flex flex-row fixed bottom-0 align-items-center justify-content-center">
    <div class="text-center ">
      <p>© Magnolia <span id="year">{{ new Date().getFullYear() }}</span></p>
    </div>
  </header>
</template>

<script setup lang="ts">

</script>

<style scoped lang="stylus">
header
  z-index 1000
</style>