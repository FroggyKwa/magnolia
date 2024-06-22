<template>
  <div class="route-input">
    <div class="py-5 flex flex-row gap-4 start align-items-center">
      <div class="flex w-full gap-4 flex-column">
        <InputGroup class="w-full">
          <InputGroupAddon class="text-3xl">
            <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                 aria-hidden="true" role="img" class="iconify iconify--emojione-monotone"
                 preserveAspectRatio="xMidYMid meet">
              <path d="M28.216 35.543h7.431l-3.666-11.418z" fill="#000000"></path>
              <path
                  d="M32 2C15.432 2 2 15.431 2 32c0 16.569 13.432 30 30 30s30-13.432 30-30C62 15.431 48.568 2 32 2m7.167 44.508l-1.914-5.965H26.567L24.6 46.508h-6.342l10.358-29.016h6.859l10.266 29.016h-6.574"
                  fill="#000000"></path>
            </svg>
          </InputGroupAddon>
          <Dropdown @change="runWithTimeout" placeholder="Выберите корпус начала пути" editable :options="buildings"
                    v-model="searchStore.from"></Dropdown>
        </InputGroup>
        <InputGroup class="w-full">
          <InputGroupAddon class="text-3xl">
            <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                 aria-hidden="true" role="img" class="iconify iconify--emojione-monotone"
                 preserveAspectRatio="xMidYMid meet">
              <path
                  d="M36.929 34.225c-.688-.315-1.654-.479-2.899-.492h-7.143v7.736h7.045c1.258 0 2.238-.171 2.938-.512c1.271-.631 1.907-1.838 1.907-3.623c0-1.509-.616-2.545-1.848-3.109"
                  fill="#000000"></path>
              <path
                  d="M37.008 28.211c.785-.479 1.179-1.329 1.179-2.55c0-1.352-.52-2.244-1.558-2.677c-.896-.303-2.04-.453-3.43-.453h-6.313v6.397h7.053c1.26.001 2.284-.239 3.069-.717"
                  fill="#000000"></path>
              <path
                  d="M32 2C15.432 2 2 15.432 2 32s13.432 30 30 30s30-13.432 30-30S48.568 2 32 2m11.607 40.374a7.996 7.996 0 0 1-2.055 2.283c-.927.709-2.02 1.194-3.279 1.457c-1.259.263-2.625.394-4.1.394H21.1V17.492h14.023c3.537.052 6.044 1.082 7.52 3.09c.888 1.234 1.332 2.71 1.332 4.43c0 1.771-.449 3.195-1.344 4.271c-.502.604-1.238 1.154-2.214 1.653c1.481.538 2.599 1.392 3.353 2.56c.753 1.168 1.13 2.585 1.13 4.252c-.001 1.719-.431 3.261-1.293 4.626"
                  fill="#000000"></path>
            </svg>
          </InputGroupAddon>
          <Dropdown @change="runWithTimeout" placeholder="Выберите корпус назначения" editable :options="buildings"
                    v-model="searchStore.to"></Dropdown>
        </InputGroup>

      </div>
      <i @click="[searchStore.from, searchStore.to] = [searchStore.to, searchStore.from]"
         class="cursor-pointer pi pi-arrows-v text-primary-200"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import useSearchStore from "@/stores/modules/search";
import { buildings, RouteKey, routesWithFilenames } from "@/stores/services/buildingRoutes";

const searchStore = useSearchStore();

function updateScene() {
  const routeKey = new RouteKey(searchStore.from, searchStore.to);
  const foundRouteSceneFilename = routesWithFilenames.get(routeKey)
  console.log(routeKey)
  console.log(foundRouteSceneFilename)
  if (foundRouteSceneFilename)
    searchStore.updateScenePath(foundRouteSceneFilename);
  else
    searchStore.updateScenePathToDefault();
}

function runWithTimeout() {
  if (searchStore.to && searchStore.from) {
    searchStore.loading = true;
    setTimeout(() => {
      updateScene();
    }, 800)
    searchStore.loading = false;
  }
  else {
    searchStore.updateScenePathToDefault();
  }
}

</script>

<style scoped lang="stylus">

</style>