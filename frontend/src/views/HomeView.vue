<template>
  smth
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import useUserStore from "@/stores/modules/user";


const router = useRouter();
const userStore = useUserStore()
const loading = ref(true);


onMounted(async () => {
  if (!userStore.user.email) {
    userStore.receiveUser(await userStore.fetchCurrentUser());
  }
  if (!userStore.user.email) {
    await router.push({ name: 'login' });
  } else
    loading.value = false;
})

</script>

<style lang="stylus">

</style>