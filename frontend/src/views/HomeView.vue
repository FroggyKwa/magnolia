<template>
  <BaseComponentWithBorders>
    <right-side-bar
        :building-id="props.buildingId"
        :department-id="props.departmentId"
        :teacher-id="props.teacherId" />
  </BaseComponentWithBorders>
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import useUserStore from "@/stores/modules/user";
import BaseComponentWithBorders from "@/components/BaseComponentWithBorders.vue";
import RightSideBar from "@/components/RightSideBar.vue";


const router = useRouter();
const userStore = useUserStore()

const props = defineProps({
  teacherId: { type: Number, required: false, default: null },
  departmentId: { type: Number, required: false, default: null },
  buildingId: { type: Number, required: false, default: null },
})
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