<script setup lang="ts">
import useSearchStore from "@/stores/modules/search";

const searchStore = useSearchStore();

import capitalize from "@/utils/string_utils";

const props = defineProps({
  teacherId: { type: Number, required: false, default: null }
});
</script>

<template>
  <div class="teacher-info flex flex-column gap-4">
    <span class="type text-2xl font-light opacity-40 underline">Преподаватель</span>
    <div class="flex flex-row gap-5 align-items-center">
      <i class="pi pi-user text-4xl"/>
      <h1>{{ searchStore.selectedTeacher.fullname }}</h1>
    </div>
    <div class="info flex flex-column gap-5">
      <span class="text-2xl line-height-3 mr-2 font-semibold">Кафедра: </span>
      <router-link
          :to="{name: 'indexWithDepartmentId', params: {departmentId: searchStore.selectedTeacher.department.id}}">
        <div class="wrapper flex flex-row align-items-center gap-3">
              <i class="pi pi-briefcase text-2xl"/>
              <span class="department-name text-2xl line-height-3">
                {{ capitalize(searchStore.selectedTeacher.department.name.toLowerCase()) }}
              </span>
        </div>
      </router-link>
      <Divider class="my-2"/>
      <div class="ext-attributes flex flex-column">
        <div class="attribute flex flex-column" :key="index"
             v-for="(attribute, index) in searchStore.selectedTeacher.ext_attributes">
          <span class="text-2xl line-height-3 mr-2 font-semibold">{{ attribute.name }}: </span>
          <span class="department-name text-2xl line-height-3">
                {{ capitalize(attribute.value.toLowerCase()) }}
              </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="stylus">

</style>