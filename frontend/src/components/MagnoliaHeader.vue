<template>
  <div class="w-screen h-5rem surface-100 shadow-2 flex flex-row justify-content-between">
    <router-link :to="{name: 'index'}">
      <div class="ml-3 text-center align-items-center mt-3 flex flex-row gap-0">
        <img src="@/assets/logo.png" alt="İmage" class="mb-3 logo"/>
        <div class="text-900 text-2xl font-semibold mb-3">
          Magnolia
        </div>
      </div>
    </router-link>
    <div class="my-5 mx-8 w-fit">
      {{ userStore.user.email }}
    </div>
  </div>
</template>

<script setup lang="ts">
import useUserStore from "@/stores/modules/user";

const userStore = useUserStore();

</script>