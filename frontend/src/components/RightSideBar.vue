<template>
  <div class="sidebar h-screen">
    <div class="sidebar-group w-full h-full flex flex-row gap-2">
      <div v-if="!hidden"
           class="sidebar-content transition-all gap-5 p-5 flex flex-column overflow-scroll surface-0 shadow-4">
        <IconField iconPosition="left">
          <InputGroup class="h-3rem">
            <InputText v-model="searchQuery" placeholder="Найти помещение или человека"/>
            <Button @click="searchStore.searchByQuery()" icon="pi pi-search" class="bg-primary"/>
          </InputGroup>
        </IconField>
        <route-input-component/>
        <div class="buttons">
          <div class="flex flex-column gap-2">
            <div class="flex flex-wrap gap-2 department-filters">
              <Button class="border-round-lg" @click="clickFilterButton($event)" v-for="building in buildings"
                      :key="building">{{ building }}
              </Button>
            </div>
            <Divider>Дополнительные фильтры</Divider>
            <div class="flex flex-row gap-2 custom-filters">
              <Button class="border-round-lg" @click="clickFilterButton($event)">Преподаватель</Button>
              <Button class="border-round-lg" @click="clickFilterButton($event)">Учебный корпус</Button>
            </div>
          </div>
        </div>
        <div class="flex-column results-block">
          <h2>Результаты поиска:</h2>
          <div class="flex flex-column gap-4 search-results-list">
            <Divider align="left"><span class="text-lg font-semibold">Преподаватели</span></Divider>
            <Skeleton height="4rem" class="w-full" v-if="loading"/>
            <section v-else class="teachers" :key="index"
                     v-for="(teacher, index) in searchStore.searchResults.teachers">
              <div>
                <router-link :to="`teachers/${teacher.id}`">
                  <div class="search-result text-primary surface-50 shadow-1 border-round-lg p-3 result flex flex-row gap-3">
                    <i class="text-xl pi pi-user align-self-center"/>
                    <div class="flex flex-column gap-3">
                      <h4 class="result-name m-0 font-semibold text-lg">{{ teacher.fullname }}</h4>
                      <span
                          class="description text-color-secondary font-light text-sm">{{ teacher.department.name }}
                      </span>
                    </div>
                  </div>
                </router-link>
              </div>
            </section>
            <Divider align="left"><span class="text-lg font-semibold">Корпуса</span></Divider>
            <Skeleton height="4rem" class="w-full" v-if="loading"/>
            <section v-else class="buildings" :key="index"
                     v-for="(building, index) in searchStore.searchResults.buildings">
              <div>
                <router-link :to="`buildings/${building.id}`">
                  <div class="search-result text-primary surface-50 shadow-1 border-round-lg p-3 result flex flex-row gap-3">
                    <i class="text-xl pi pi-user align-self-center"/>
                    <div class="flex flex-column gap-3">
                      <h4 class="result-name m-0 font-semibold text-lg">{{ building.name }}</h4>
                    </div>
                  </div>
                </router-link>
              </div>
            </section>
            <Divider align="left"><span class="text-lg font-semibold">Преподаватели</span></Divider>
            <Skeleton height="4rem" class="w-full" v-if="loading"/>
            <section v-else class="departments" :key="index"
                     v-for="(department, index) in searchStore.searchResults.departments">
              <div>
                <router-link :to="`departments/${department.id}`">
                  <div class="search-result text-primary surface-50 shadow-1 border-round-lg p-3 result flex flex-row gap-3">
                    <i class="text-xl pi pi-user align-self-center"/>
                    <div class="flex flex-column gap-3">
                      <h4 class="result-name m-0 font-semibold text-lg">{{ department.name }}</h4>
                      <span
                          class="description text-color-secondary font-light text-sm">{{
                          getFirstThreeTeachers(department.id)
                        }}
                      </span>
                    </div>
                  </div>
                </router-link>
              </div>
            </section>
          </div>
        </div>
      </div>
      <div class="h-full w-4rem flex flex-column justify-content-center">
        <div :class="{'rotate': hidden }"
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
import { onMounted, ref } from 'vue';
import RouteInputComponent from "@/components/RouteInputComponent.vue";
import { buildings } from "@/stores/services/buildings";
import useSearchStore from "@/stores/modules/search";

const searchStore = useSearchStore();
const searchQuery = ref('');
const loading = ref(true);
const hidden = ref(false);
let selectedButton: EventTarget | null = null;

function toggle() {
  hidden.value = !hidden.value;
}

function clickFilterButton(event: Event,) {
  if (selectedButton !== event.target) {
    if (selectedButton)
      (selectedButton as HTMLInputElement).classList.toggle('active');
    selectedButton = event.target;
    (selectedButton as HTMLInputElement).classList.toggle('active');
  } else {
    (selectedButton as HTMLInputElement).classList.toggle('active');
    selectedButton = null;
  }
}

function getFirstThreeTeachers(department_id: number): string {
  const departmentTeachers = searchStore.searchResults.teachers
      .filter(element => element.department.id === department_id)
      .map(el => el.fullname);
  if (departmentTeachers.length > 0)
    return departmentTeachers.slice(0, 3).join('; ') + '  ...';
  return '';
}

onMounted(async () => {
  searchStore.receiveSearchResults(await searchStore.searchByQuery(null));
  loading.value = false;
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