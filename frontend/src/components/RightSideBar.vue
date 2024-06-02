<template>
  <div class="sidebar h-screen">
    <div class="sidebar-group w-full h-full flex flex-row gap-2">
      <div v-if="!isSidebarHidden"
           class="sidebar-content transition-all gap-5 p-5 flex flex-column overflow-scroll surface-0 shadow-4">
        <div v-if="!(route.params.teacherId || route.params.departmentId || route.params.buildingId)">
          <IconField iconPosition="left">
            <InputGroup class="h-3rem">
              <InputText @keydown.enter="updateSearchResults" @input="runWithTimeout" v-model="searchQuery"
                         placeholder="Найти помещение или человека"/>
              <Button @click="updateSearchResults" icon="pi pi-search" class="bg-primary"/>
            </InputGroup>
          </IconField>
          <route-input-component/>
          <div class="buttons">
            <div class="flex flex-column gap-2">
              <div class="flex flex-wrap gap-2 department-filters">
                <Button :class="{active: selectedButtonText === name}" class="border-round-lg"
                        @click="clickFilterButton($event) && updateSearchResults()"
                        v-for="name in departments"
                        :key="name">{{ name }}
                </Button>
              </div>
              <Divider>Дополнительные фильтры</Divider>
              <div class="flex flex-row gap-2 custom-filters">
                <Button :class="{active: selectedButtonText.trim() === 'Преподаватель'}" class="border-round-lg"
                        @click="clickFilterButton($event) && updateSearchResultsWithoutParams()">Преподаватель
                </Button>
                <Button :class="{active: selectedButtonText.trim() === 'Учебный корпус'}" class="border-round-lg"
                        @click="clickFilterButton($event) && updateSearchResultsWithoutParams()">Учебный корпус
                </Button>
              </div>
            </div>
          </div>
          <div class="flex-column results-block">
            <h2>Результаты поиска:</h2>
            <div class="search-results-list">
              <Divider align="left"><span class="text-lg font-semibold">Преподаватели</span></Divider>
              <section class="flex flex-column gap-4">
                <Skeleton height="4rem" class="w-full" v-if="searchStore.loading"/>
                <div v-else :hidden="selectedButtonText === 'Учебный корпус'" class="teachers" :key="index"
                     v-for="(teacher, index) in searchStore.searchResults.teachers">
                  <div>
                    <router-link :to="`/teachers/${teacher.id}`">
                      <div
                          class="search-result text-primary surface-50 shadow-1 border-round-lg p-3 result flex flex-row gap-3">
                        <i class="text-xl pi pi-user align-self-center"/>
                        <div class="flex flex-column gap-3">
                          <h4 class="result-name m-0 font-semibold text-lg">{{ teacher.fullname }}</h4>
                          <span
                              class="description text-color-secondary font-light text-sm">{{
                              capitalize(teacher.department?.name.toLowerCase())
                            }}
                          </span>
                        </div>
                      </div>
                    </router-link>
                  </div>
                </div>
              </section>
              <Divider align="left"><span class="text-lg font-semibold">Корпуса</span></Divider>
              <section class="flex flex-column gap-4">
                <Skeleton height="4rem" class="w-full" v-if="searchStore.loading"/>
                <div v-else :hidden="selectedButtonText === 'Преподаватель'" class="buildings" :key="index"
                     v-for="(building, index) in searchStore.searchResults.buildings">
                  <div>
                    <router-link :to="`/buildings/${building.id}`">
                      <div
                          class="search-result text-primary surface-50 shadow-1 border-round-lg p-3 result flex flex-row gap-3">
                        <i class="text-xl pi pi-building align-self-center"/>
                        <div class="flex flex-column gap-3">
                          <h4 class="result-name m-0 font-semibold text-lg">{{ building.name }}</h4>
                        </div>
                      </div>
                    </router-link>
                  </div>
                </div>
              </section>
              <Divider align="left"><span class="text-lg font-semibold">Кафедры</span></Divider>
              <section class="flex flex-column gap-4">
                <Skeleton height="4rem" class="w-full" v-if="searchStore.loading"/>
                <div v-else :hidden="selectedButtonText === 'Преподаватель' || selectedButtonText === 'Учебный корпус'"
                     class="departments" :key="index"
                     v-for="(department, index) in searchStore.searchResults.departments">
                  <div>
                    <router-link :to="`/departments/${department.id}`">
                      <div
                          class="search-result text-primary surface-50 shadow-1 border-round-lg p-3 result flex flex-row gap-3">
                        <i class="text-xl pi pi-briefcase align-self-center"/>
                        <div class="flex flex-column gap-3">
                          <h4 class="result-name m-0 font-semibold text-lg">{{
                              capitalize(department.name.toLowerCase())
                            }}</h4>
                          <span
                              class="description text-color-secondary font-light text-sm">{{
                              getFirstThreeTeachers(department.id)
                            }}
                          </span>
                        </div>
                      </div>
                    </router-link>
                  </div>
                </div>
              </section>
            </div>
          </div>
        </div>
        <div v-else-if="teacherId">
          <teacher-details-component :teacher-id="teacherId"/>
        </div>
        <div v-else-if="buildingId">
          <building-details-component :building-id="buildingId"/>
        </div>
        <div v-else-if="departmentId">
          <department-details-component :department-id="departmentId"/>
        </div>

      </div>
      <div class="h-full w-4rem flex flex-column justify-content-center">
        <div :class="{'rotate': isSidebarHidden }"
             class="flex align-items-center text-center justify-content-center w-3rem h-3rem origin-center transition-all transition-duration-300 transition-linear">
          <i @click="toggle"
             class="transition-colors transition-duration-300 hover:text-400 pi-arrow-circle-right cursor-pointer pi text-600"
             style="font-size: 2rem"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Route, useRoute, useRouter } from 'vue-router';
import { onMounted, ref, watch } from 'vue';
import RouteInputComponent from "@/components/RouteInputComponent.vue";
import { departments } from "@/stores/services/departments";
import useSearchStore from "@/stores/modules/search";
import capitalize from "@/utils/string_utils";
import TeacherDetailsComponent from "@/components/TeacherDetailsComponent.vue";
import BuildingDetailsComponent from "@/components/BuildingDetailsComponent.vue";
import DepartmentDetailsComponent from "@/components/DepartmentDetailsComponent.vue";
import useUserStore from "@/stores/modules/user";

const router = useRouter()
const route = useRoute();
const searchStore = useSearchStore();
const props = defineProps({
  teacherId: { type: Number, required: false, default: null },
  departmentId: { type: Number, required: false, default: null },
  buildingId: { type: Number, required: false, default: null },
});

const searchQuery = ref('');
const isSidebarHidden = ref(false);
const selectedButtonText = ref('');

watch(props, async (newProps) => {
  if (newProps.teacherId)
    searchStore.selectedTeacher = await searchStore.getTeacherById(newProps.teacherId);
  if (newProps.departmentId) {
    searchStore.selectedDepartment = await searchStore.getDepartmentById(newProps.departmentId);
  }  if (newProps.buildingId)
    searchStore.selectedBuilding = await searchStore.getBuildingById(newProps.buildingId);
})

let selectedButton: EventTarget | null = null;

function toggle() {
  isSidebarHidden.value = !isSidebarHidden.value;
}

function clickFilterButton(event: Event,) {
  selectedButtonText.value = '';
  if (selectedButton !== event.target) {
    if (selectedButton)
      (selectedButton as HTMLInputElement).classList.toggle('active');
    selectedButton = event.target;
    selectedButtonText.value = ((event.target as HTMLInputElement).textContent as string).trim();
    (selectedButton as HTMLInputElement).classList.toggle('active');
  } else {
    (selectedButton as HTMLInputElement).classList.toggle('active');
    selectedButton = null;
  }
  return true;
}

function getFirstThreeTeachers(department_id: number): string {
  const departmentTeachers = searchStore.searchResults.teachers
      .filter(element => element.department?.id === department_id)
      .map(el => el.fullname);
  if (departmentTeachers.length > 0)
    return departmentTeachers.slice(0, 3).join('; ') + '  ...';
  return '';
}

async function updateSearchResults() {
  searchStore.receiveSearchResults(await searchStore.searchByQuery(searchQuery.value, selectedButtonText.value));
}

async function updateSearchResultsWithoutParams() {
  searchStore.receiveSearchResults(await searchStore.searchByQuery());
}

function runWithTimeout() {
  searchStore.loading.value = true;

  setTimeout(() => {
    updateSearchResults();
  }, 800)
}

onMounted(async () => {
  if (await useUserStore().fetchCurrentUser().id === -1)
    return
  if (props.teacherId)
    searchStore.selectedTeacher = await searchStore.getTeacherById(props.teacherId);
  if (props.departmentId)
    searchStore.selectedDepartment = await searchStore.getDepartmentById(props.departmentId);
  if (props.buildingId)
    searchStore.selectedBuilding = await searchStore.getBuildingById(props.buildingId);


  await updateSearchResults();
})

</script>

<style scoped lang="stylus">
.sidebar
  max-width 45rem
  padding-bottom 3rem
  padding-top 5rem

.sidebar-content
  width 85%

.rotate
  transform rotate(-180deg)

.active
  color: var(--primary-color)
  background-color: var(--primary-color-text)

.search-result
  min-height 5rem

</style>

<style lang="stylus">
a
  color var(--primary-color)
</style>