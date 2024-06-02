import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from "@/views/LoginView.vue";
import ConfirmOtpView from "@/views/ConfirmOtpView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'index',
            component: HomeView
        },

        {
            path: '/teachers/:teacherId',
            name: 'indexWithTeacherId',
            component: HomeView,
            props: (route: any) => {
                const teacherId = Number.parseInt(route.params.teacherId as string, 10);
                return { ...route.params, teacherId  };
            },
        },
        {
            path: '/departments/:departmentId',
            name: 'indexWithDepartmentId',
            component: HomeView,
            props: (route: any) => {
                const departmentId = Number.parseInt(route.params.departmentId as string, 10);
                return { ...route.params, departmentId };
            },
        },
        {
            path: '/buildings/:buildingId',
            name: 'indexWithBuildingId',
            component: HomeView,
            props: (route: any) => {
                const buildingId = Number.parseInt(route.params.buildingId as string, 10);
                return { ...route.params, buildingId};
            },
        },

        {
            path: '/login',
            name: 'login',
            component: LoginView
        },
        {
            path: '/confirm',
            name: 'confirm_otp_view',
            component: ConfirmOtpView
        },
    ]
})

export default router
