<template>
  <footer class="fixed top-0 w-screen h-5rem surface-100 shadow-2 flex flex-row justify-content-between">
    <router-link :to="{name: 'index'}">
      <div class="ml-3 text-center align-items-center mt-3 flex flex-row gap-0">
        <img src="@/assets/logo.png" alt="İmage" class="mb-3 logo"/>
        <div class="text-900 text-2xl font-semibold mb-3">
          Виртуальный помощник КамчатГТУ
        </div>
      </div>
    </router-link>
    <div class="my-auto mr-8">
      <Dropdown v-model="sign_out" :options="[{name: 'Выход', code: 'sign_out'}]" optionLabel="name"
                :placeholder="userStore.user.email" class="flex justify-content-center w-full md:w-15rem">
      </Dropdown>
    </div>
  </footer>
</template>

<script setup lang="ts">
import useUserStore from "@/stores/modules/user";
import { ref, watch } from 'vue';
import api from "@/stores/services/api";
import { useRouter } from "vue-router";


const sign_out = ref(false);
const userStore = useUserStore();
const router = useRouter()

watch(sign_out, () => {
  api.post('logout/')
  router.push({ name: 'login' });
  document.cookie = 'sessionid=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
})

</script>

<style lang="stylus">
footer
  z-index 10000
</style>