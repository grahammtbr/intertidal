import { ref, watchEffect, toValue } from 'vue'

export function useFetch(url) {
    const data = ref(null)
    const error = ref(null)
    const baseUrl = import.meta.env.VITE_API_URL

    const fetchData = () => {
        // reset state before fetching..
        data.value = {}
        error.value = null

        fetch(baseUrl + toValue(url))
            .then((res) => res.json())
            .then((json) => (data.value = json))
            .catch((err) => (error.value = err))
    }

    watchEffect(() => {
        fetchData()
    })

    return { data, error }
}
