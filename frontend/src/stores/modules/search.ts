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


    async function getTeacherById(id: number): Promise<TeacherModel> {
        let data = {};
        await api.get(`teachers/${id}`)
            .then((response) => data = response.data)
            .catch(error => console.log(error));
        return data as TeacherModel;
    }

    async function getDepartmentById(id: number): Promise<DepartmentModel> {
        let data = {};
        await api.get(`departments/${id}`)
            .then((response) => data = response.data)
            .catch(error => console.log(error));
        return data as DepartmentModel;
    }

    async function getBuildingById(id: number): Promise<BuildingModel> {
        let data = {};
        await api.get(`building/${id}`)
            .then((response) => data = response.data)
            .catch(error => console.log(error));
        return data as BuildingModel;
    }

    async function searchByQuery(params: {
        teachers: [],
        departments: [],
        buildings: []
    } | null): Promise<SearchModel> {
        let data = {};
        await api.get(`search/`, { params: { params } })
            .then((response) => data = response.data)
            .catch(error => {
                console.log(error)
            });
        return data as SearchModel;
    }

    function receiveSearchResults(received_results: SearchModel) {
        searchResults.value = received_results
    }

    return {
        selectedDepartment,
        selectedBuilding,
        selectedTeacher,
        searchResults,
        getBuildingById,
        getDepartmentById,
        getTeacherById,
        receiveSearchResults,
        searchByQuery,
    }
})

export default useSearchStore;