<template>
  <Toast position="top-right"/>
  <ModalComponent heading="Введите код" :tip="`Мы отправили его на email ${user.email}`">
    <form @keydown.enter.prevent="confirm_otp" @submit.prevent="confirm_otp" class="flex flex-column gap-8 justify-content-center align-items-center h-full">
      <Skeleton v-if="loading" height="2rem"></Skeleton>
      <InputOtp v-else :length="6" v-model="otp"/>
      <Button
          class="min-w-max px-5 border-round-3xl transition-colors transition-duration- bg-primary hover:bg-primary-reverse"
          @click="confirm_otp"
          label="Войти"/>
    </form>
  </ModalComponent>
</template>

<script setup lang="ts">
import ModalComponent from "@/components/ModalWithLogoComponent.vue";
import { ref, onMounted } from "vue";

import useUserStore from "@/stores/modules/user";
import { useRouter } from "vue-router";
import { useToast } from "primevue/usetoast";
import Toast from "primevue/toast";


const router = useRouter();
const toast = useToast();
const userStore = useUserStore();

const user = userStore.user;

const loading = ref(true);

async function confirm_otp() {
  if (await userStore.login({ email: user.email, code: otp.value }))
    await router.push({ name: 'index' })
  else
    toast.add({
      summary: "Ошибка",
      severity: 'error',
      life: 5000,
      closable: true,
      detail: "Неверный код, попробуйте снова"
    })
}

const otp = ref('');

onMounted(async () => {
  console.log(userStore.user.email)
  if (!userStore.user.email)
    await router.push({ name: 'login' });
  else
    loading.value = false;
  if (userStore.user.id !== -1)
    await router.push({ name: 'index' })
})

</script>

<style scoped lang="stylus">

</style>