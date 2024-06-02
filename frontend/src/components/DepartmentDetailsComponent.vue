<script setup lang="ts">
import useSearchStore from "@/stores/modules/search";
import { onMounted, ref } from "vue";
import capitalize from "@/utils/string_utils";
import type { BuildingModel, TeacherModel } from "@/models/SearchModel";
import search from "@/stores/modules/search";


const searchStore = useSearchStore();
const buildingsByDepartment = ref(new Array<BuildingModel>);
const teachersByDepartment = ref(new Array<TeacherModel>);

const props = defineProps({
  departmentId: { type: Number, required: false, default: null }
});

onMounted(async () => {
  searchStore.selectedDepartment.value = searchStore.getDepartmentById(props.departmentId)
  buildingsByDepartment.value = await searchStore.getBuildingsByDepartmentId(props.departmentId);
  teachersByDepartment.value = await searchStore.getTeachersByDepartmentId(props.departmentId)
  console.log(teachersByDepartment.value)
})

</script>

<template>
  <div class="teacher-info flex flex-column gap-4">
    <span class="type text-2xl font-light opacity-40 underline">Кафедра</span>
    <div class="flex flex-row gap-5 align-items-center">
      <i class="pi pi-user text-4xl"/>
      <h1>{{ capitalize(searchStore.selectedDepartment.name.toLowerCase()) }}</h1>
    </div>
    <div class="info flex flex-column gap-5">
      <div class="teachers-list flex flex-column gap-4">
        <span class="text-2xl line-height-3 mr-2 font-semibold">Преподаватели:</span>
        <Skeleton class="w-full h-30rem" v-if="searchStore.loading"/>
        <div v-else :key="index" v-for="(teacher, index) in teachersByDepartment"
             class="teacher flex flex-column">
          <router-link
              :to="{name: 'indexWithTeacherId', params: {teacherId: teacher.id}}">
            <div class="wrapper flex flex-row align-items-center gap-3">
              <i class="pi pi-briefcase text-2xl"/>
              <span class="department-name text-2xl line-height-3">
                {{ teacher.fullname }}
              </span>
            </div>
          </router-link>
          <Divider/>
        </div>
      </div>

      <div class="buildings-list flex flex-column gap-4">
        <span class="text-2xl line-height-3 mr-2 font-semibold">Учебные корпуса:</span>
        <Skeleton class="w-full h-30rem" v-if="searchStore.loading"/>
        <div v-else :key="index" v-for="(building, index) in buildingsByDepartment"
             class="building flex flex-column">
          <router-link
              :to="{name: 'indexWithBuildingId', params: {buildingId: building.id}}">
            <div class="wrapper flex flex-row align-items-center gap-3">
              <i class="pi pi-briefcase text-2xl"/>
              <span class="department-name text-2xl line-height-3">
                {{ building.name }}
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