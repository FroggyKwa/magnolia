export interface TeacherModel {
    id: number,
    fullname: string,
    department?: {
        id: number,
        name: string
    }
    ext_attributes?: Array<{
        name: String,
        value: String
    }>
}

export interface DepartmentModel {
    id: number,
    name: string,
    buildings: Array<number>,
    teachers: Array<number>,
    ext_attributes?: Array<{
        name: String,
        value: String
    }>
}

export interface BuildingModel {
    id: number,
    name: string,
    address: string,
    departments?: Array<DepartmentModel>,
    ext_attributes?: Array<{
        name: String,
        value: String
    }>
}

export interface SearchModel {
    teachers: Array<TeacherModel>,
    departments: Array<DepartmentModel>,
    buildings: Array<BuildingModel>
}