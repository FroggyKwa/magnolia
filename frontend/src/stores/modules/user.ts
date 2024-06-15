import { defineStore } from "pinia";
import type { Ref } from 'vue';
import type { UserModel } from "@/models/UserModel";
import { ref } from "vue";
import api from "@/stores/services/api";

const useUserStore = defineStore('user', () => {
    const user: Ref<UserModel> = ref({
        id: -1,
        fullname: '',
        email: '',
        usertype: '',
    });
    const authenticated: Ref<boolean> = ref(false);
    const fetching: Ref<boolean> = ref(true);
    const email_sent = ref(new Date(-8640000000000000));


    function receiveUser(received_user: UserModel) {
        user.value = received_user
    }

    function updateUserMutation(payload: {}) {
        user.value = { ...user.value, ...payload }
    }

    async function fetchCurrentUser(): Promise<UserModel> {
        let data = {}
        await api.get(`whoami`)
            .then(response => data = response.data)
            .catch((error) => {
                if (error.response.status === 401)
                    data = {
                        id: -1,
                        fullname: '',
                        email: '',
                        usertype: '',
                    }
            });
        fetching.value = false;
        return data as UserModel;
    }

    async function get_otp(payload: { email: string }) {
        await api.post(`sign_in`, { email: payload.email })
            .then(() => {
                email_sent.value = new Date();
            })
            .catch(error => console.log(error));
    }

    async function login(payload: { email: string, code: string }): Promise<boolean> {
        await api.post(`sign_in_with_token`, { email: payload.email, code: payload.code })
            .then(() => {
                authenticated.value = true;
            })
            .catch(error => {
                console.log(error)
            });
        return authenticated.value;
    }

    return { user, email_sent, authenticated, fetching, fetchCurrentUser, receiveUser, get_otp, login, updateUserMutation }
})

export default useUserStore;