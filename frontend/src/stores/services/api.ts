import axios from "axios";

const BASE_URL = (process.env.NODE_ENV === "production")
    ? process.env.APPLICATION_URL : 'http://localhost:8000'
// ? process.env.APPLICATION_URL : import.meta.env.VITE_BACKEND_URL;

axios.defaults.baseURL = BASE_URL + '/api/';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

const api = axios.create({
    headers: {"Content-Type": "application/json"},
    withCredentials: true,
});


export default api;