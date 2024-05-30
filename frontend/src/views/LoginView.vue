<template>
  <Toast position="top-right"/>
  <div
      class="surface-50 flex flex-column align-items-center justify-content-center min-h-screen min-w-screen overflow-hidden">
    <div class="surface-0 border-round-lg shadow-3 w-30rem h-30rem">
      <div class="flex flex-column align-items-center justify-content-center h-full w-full m-0 py-5 px-5">
        <div class="text-center mb-5">
          <img src="@/assets/logo.png" alt="İmage" class="mb-3 logo"/>
          <div class="text-900 text-3xl font-medium mb-3">
            Добро пожаловать!
          </div>
          <span class="text-400 text-sm">
              Войдите, чтобы продолжить
          </span>
        </div>
        <form class="flex flex-column gap-4 justify-content-center align-items-center h-full">
          <InputText v-model="email" @update:model-value="() => validateEmail()"
                     :class="{'p-invalid': isEmailFieldInvalid && email}" placeholder="Email"
                     class="mb-3 mt-7text-xl" id="email-field"/>
          <Button
              class="min-w-max px-5 border-round-3xl transition-colors transition-duration- bg-primary hover:bg-primary-reverse"
              @submit.prevent=""
              @click="sign_in()"
              label="Войти"/>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Toast from "primevue/toast";
import {useToast} from "primevue/usetoast";
import {ref} from "vue";

let email = ref('')
let isEmailFieldInvalid = ref(true);
const toast = useToast();

function validateEmail() {
  const regex: RegExp = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w*)+$/
  isEmailFieldInvalid = ref(!regex.test(ref(email).value));
}

function sign_in() {
  if (isEmailFieldInvalid.value)
    toast.add({severity: 'error', closable: true, summary: 'Ошибка!', detail: "Введён некорректный адрес эл. почты", life: 5000})
}
</script>


<style scoped lang="stylus">
.logo
  width 3.5rem
  height 3.5rem
</style>