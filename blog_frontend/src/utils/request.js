import axios from 'axios'

const service = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 5000
});

service.interceptors.request.use(
    config => {
        const token = localStorage.getItem('token')
        if (token) {
            config.headers['Authorization'] = 'Bearer ' + token
        }
        return config
    },
    error => {
        console.log(error);
        return Promise.reject(error);
    }
);

service.interceptors.response.use(
    response => {
        return response.data
    },
    error => {
        console.log('err'+ error);
        if (error.response.status) {
            switch (error.response.status) {
                case 401:
                    localStorage.removeItem('token')
                    router.push('/login')
                    break;
                case 403:
                    localStorage.removeItem('token')
                    router.push('/login')
                    break;
                case 404:
                    alert('资源不存在')
                    break;
                case 500:
                    alert
                    break;
            }
        }
        return Promise.reject(error);
    }
);

export default service;
