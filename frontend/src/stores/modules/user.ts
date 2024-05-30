import { defineStore } from "pinia";
import type { Ref } from 'vue';
import type { UserModel } from "@/models/UserModel";
import { ref } from "vue";
import api from "@/stores/services/api";

const useUserStore = defineStore('user', () => {
    const user: Ref<UserModel> = ref({
        id: -1,
        fullname: '',
        email: ''
    });
    const authenticated: Ref<boolean> = ref(false);
    const email_sent = ref(new Date(-8640000000000000));


    function receiveUser(received_user: UserModel) {
        user.value = received_user
    }

    async function fetchCurrentUser(user_id: number): Promise<UserModel> {
        let data = { data: {} }
        await api.get(`users/whoami}`)
            .then(response => data = response)
            .catch(error => console.log(error));
        return data.data as UserModel;
    }

    async function get_otp(payload: { email: string }) {
        await api.post(`sign_in`, { email: payload.email })
            .then(() => {
                email_sent.value = new Date();
            })
            .catch(error => console.log(error));
    }

    async function login(payload: { email: string, code: string }) {
        await api.post(`sign_in_with_token`, { email: payload.email, code: payload.code })
            .then(() => {
                authenticated.value = true;
            })
            .catch(error => console.log(error));
    }

    return { user, email_sent, authenticated,fetchCurrentUser, receiveUser, get_otp }
})

export default useUserStore;