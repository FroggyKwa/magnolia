<template>
  <Toast position="top-right"/>
  <ModalComponent heading="Добро пожаловать!" tip="Войдите, чтобы продолжить">
    <Skeleton v-if="loading" height="10rem"></Skeleton>
    <form v-else @submit.prevent="get_otp" class="flex flex-column gap-5 justify-content-center align-items-center h-full">
      <div class="flex flex-row">
        <SelectButton
            :allow-empty="false"
            v-model="usertype"
            optionLabel="name"
            option-value="value"
            dataKey="value"
            :options="[{value :'ST', name: 'Студент'}, {value: 'EN', name: 'Абитурент'}]">
        </SelectButton>
      </div>
      <InputText v-model="email" @update:model-value="() => validateEmail()"
                 :class="{'p-invalid': isEmailFieldInvalid && email}" placeholder="Email"
                 id="email-field"/>
      <Button
          class="min-w-max my-3 px-5 border-round-3xl transition-colors transition-duration- bg-primary hover:bg-primary-reverse"
          @click="get_otp"
          label="Отправить код"/>
    </form>
  </ModalComponent>
</template>

<script setup lang="ts">
import Toast from "primevue/toast";
import { useToast } from "primevue/usetoast";
import { onMounted, ref } from "vue";
import useUserStore from "@/stores/modules/user";
import { useRouter } from "vue-router";
import ModalComponent from "@/components/ModalWithLogoComponent.vue";

let email = ref('')
let isEmailFieldInvalid = ref(true);
const toast = useToast();
const userStore = useUserStore();
const router = useRouter();
const usertype = ref('EN');


const loading = ref(true);

function validateEmail() {
  const regex: RegExp = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w*)+$/
  isEmailFieldInvalid = ref(!regex.test(ref(email).value));
}

function get_otp() {
  if (isEmailFieldInvalid.value || !email.value) {
    toast.add({
      severity: 'error',
      closable: true,
      summary: 'Ошибка!',
      detail: "Введён некорректный адрес эл. почты",
      life: 5000
    })
    return;
  }
  const payload = { email: email.value, usertype: usertype.value };
  userStore.get_otp(payload);
  userStore.updateUserMutation(payload)
  router.push({ name: "confirm_otp_view" })
}

onMounted(async () => {
  userStore.receiveUser(await userStore.fetchCurrentUser());
  console.log(userStore.user.id)
  if (userStore.user.id !== -1)
    await router.push({ name: 'index' })
  loading.value = false;
})
</script>


<style lang="stylus">
.logo
  width 3.5rem
  height 3.5rem
</style>