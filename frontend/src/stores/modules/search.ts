import { defineStore } from "pinia";
import type { Ref } from "vue";
import { ref } from "vue";
import api from "@/stores/services/api";
import type { BuildingModel, DepartmentModel, SearchModel, TeacherModel } from "@/models/SearchModel";

const useSearchStore = defineStore('search', () => {
    const searchResults = ref({
        teachers: {} as Array<TeacherModel>,
        departments: {} as Array<DepartmentModel>,
        buildings: {} as Array<BuildingModel>
    })
    const selectedTeacher: Ref<TeacherModel> = ref({
        id: -1,
        fullname: '',
        department: {
            id: -1,
            name: ''
        },
        ext_attributes: []
    });

    const selectedDepartment: Ref<DepartmentModel> = ref({
        id: -1,
        name: '',
        buildings: [],
        teachers: [],
        ext_attributes: []
    })
    const selectedBuilding: Ref<BuildingModel> = ref({
        id: -1,
        name: '',
        address: '',
        departments: [],
        ext_attributes: []
    })

    const PATH_TO_SCENES: string = "/scene_models/";
    const DEFAULT_SCENE_PATH: string = PATH_TO_SCENES + "main_scene.glb";
    const scenePath = ref(DEFAULT_SCENE_PATH);
    const from = ref('');
    const to = ref('');

    const loading: Ref<Boolean> = ref(false);

    async function getTeacherById(id: number): Promise<TeacherModel> {
        loading.value = true;
        let data = {};
        await api.get(`teachers/${id}/`)
            .then((response) => data = response.data)
            .catch(error => console.log(error));
        loading.value = false;
        return data as TeacherModel;
    }

    async function getDepartmentById(id: number): Promise<DepartmentModel> {
        loading.value = true;
        let data = {};
        await api.get(`departments/${id}/`)
            .then((response) => data = response.data)
            .catch(error => console.log(error));
        loading.value = false;
        return data as DepartmentModel;
    }

    async function getBuildingById(id: number): Promise<BuildingModel> {
        loading.value = true;
        let data = {};
        await api.get(`buildings/${id}/`)
            .then((response) => data = response.data)
            .catch(error => console.log(error));
        loading.value = false;
        return data as BuildingModel;
    }

    async function searchByQuery(query?: string, department__name?: string): Promise<SearchModel> {
        loading.value = true;
        let data = {};
        await api.get(`search/`, { params: { query, department__name } })
            .then((response) => data = response.data)
            .catch(error => {
                console.log(error)
            });
        loading.value = false;
        return data as SearchModel;
    }

    async function getBuildingsByDepartmentId(departmentId: Number): Promise<Array<BuildingModel>> {
        loading.value = true;
        let data = {};
        await api.get(`buildings/`, { params: { department__id: departmentId } })
            .then(response => data = response.data)
            .catch(error => console.log(error))
        loading.value = false;
        return data as Array<BuildingModel>;
    }

    async function getTeachersByDepartmentId(departmentId: Number): Promise<Array<TeacherModel>> {
        loading.value = true;
        let data = {};
        await api.get(`teachers/`, { params: { department__id: departmentId } })
            .then(response => data = response.data)
            .catch(error => console.log(error))
        loading.value = false;
        return data as Array<TeacherModel>;
    }

    function receiveSearchResults(received_results: SearchModel) {
        searchResults.value = received_results
    }

    function updateScenePath(path: string) {
        scenePath.value = PATH_TO_SCENES + path;
    }

    function updateScenePathToDefault() {
        scenePath.value = DEFAULT_SCENE_PATH;
    }



    return {
        selectedDepartment,
        selectedBuilding,
        selectedTeacher,
        searchResults,
        from,
        to,
        loading,
        scenePath,
        getBuildingById,
        getDepartmentById,
        getTeacherById,
        receiveSearchResults,
        searchByQuery,
        getBuildingsByDepartmentId,
        getTeachersByDepartmentId,
        updateScenePath,
        updateScenePathToDefault
    }
})

export default useSearchStore;