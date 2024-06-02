<script setup lang="ts">

import capitalize from "@/utils/string_utils";
import useSearchStore from "@/stores/modules/search";

const searchStore = useSearchStore();

const props = defineProps({
  buildingId: { type: Number, required: false, default: null }
});
</script>

<template>
  <div class="teacher-info flex flex-column gap-4">
    <span class="type text-2xl font-light opacity-40 underline">Учебный корпус</span>
    <div class="flex flex-row gap-5 align-items-center">
      <i class="pi pi-building text-4xl"/>
      <h1>{{ searchStore.selectedBuilding.name }}</h1>
    </div>
    <div class="info flex flex-column gap-5">
      <div class="address flex flex-column">
        <span class="text-2xl line-height-3 mr-2 font-semibold">Адрес:</span>
        <span class="address-text text-2xl line-height-3">{{searchStore.selectedBuilding.address}}</span>
      </div>
        <span class="text-2xl line-height-3 mr-2 font-semibold">
            Кафедры в здании:
        </span>
      <div class="departments flex flex-column gap-3">
        <div class="department" :key="index" v-for="(department, index) in searchStore.selectedBuilding.departments">
          <router-link
              :to="{name: 'indexWithDepartmentId', params: {departmentId: department.id}}">
            <div class="wrapper flex flex-row align-items-center gap-3">
              <i class="pi pi-briefcase text-2xl"/>
              <span class="department-name text-2xl line-height-3">
                {{ capitalize(department.name.toLowerCase()) }}
              </span>
            </div>
          </router-link>
          <Divider/>
        </div>
      </div>
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