import service from '@/utils/request'

export function getArticles() {
    return service.get('/api/article/')
}

export function getArticle(id) {
    return service.get('/api/article/${id}')
}

export function postArticle(data) {
    return service.post('/api/article/', data)
}
