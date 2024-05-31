<template>
  <div
      class="surface-50 flex flex-column align-items-center justify-content-center min-h-screen min-w-screen overflow-hidden">
    <div class="surface-0 border-round-lg shadow-3 w-30rem h-30rem">
      <div class="flex flex-column align-items-center justify-content-center h-full w-full m-0 py-5 px-5">
        <div class="text-center mb-5">
          <img src="@/assets/logo.png" alt="İmage" class="mb-3 logo"/>
          <div class="text-900 text-3xl font-medium mb-3">
            {{ heading }}
          </div>
          <span class="text-400 text-sm">
              {{ tip }}
          </span>
          <slot>

          </slot>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
const props = defineProps({
  heading: String,
  tip: String
})
</script>