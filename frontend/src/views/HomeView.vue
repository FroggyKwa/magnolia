<template>
  <BaseComponentWithBorders>
    <div class="flex flex-row">
      <right-side-bar
          :building-id="props.buildingId"
          :department-id="props.departmentId"
          :teacher-id="props.teacherId"
      />
      <model-viewer
          disable-tap
          class="align-self-center"
          v-model:src="searchStore.scenePath"
          ar ar-modes="webxr scene-viewer quick-look"
          camera-controls
          tone-mapping="neutral"
          camera-orbit="0deg 60deg"
          camera-target="0m 0m 0m"
          min-camera-orbit='auto 0deg 10%'
          max-camera-orbit='auto 70deg 25%'
          min-field-of-view='0.5deg'
          max-field-of-view='15deg'
          shadow-intensity="0">
        <template v-slot:progress-bar>
          <div class="progress-bar hide">
            <div class="update-bar"></div>
          </div>
        </template>
      </model-viewer>
    </div>
  </BaseComponentWithBorders>
</template>
<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import useUserStore from "@/stores/modules/user";
import BaseComponentWithBorders from "@/components/BaseComponentWithBorders.vue";
import RightSideBar from "@/components/RightSideBar.vue";
import useSearchStore from "@/stores/modules/search";


const router = useRouter();
const userStore = useUserStore();
const searchStore = useSearchStore();

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
model-viewer
  width 100vw
  height 100vh
</style>