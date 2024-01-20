import axiosInstance from 'axios'

const axios = axiosInstance.create({
    baseURL: 'http://127.0.0.1:8000/'
})

export default axios;
