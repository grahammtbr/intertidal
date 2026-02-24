import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {

    const username = ref(null)
    const csrfToken = ref(null)
    const isAuthenticated = ref(false)
    const message = ref(null)

    async function getCsrf() {
        await fetch("/intertidal/api/v1/csrf/", {
            credentials: "same-origin",
        })
        .then((res) => {
            csrfToken.value = res.headers.get("X-CSRFToken");
            //console.log(authState.value.csrfToken);
        })
        .catch((err) => {
            console.log(err);
        });
    }

    async function getUsername() {
        fetch('/intertidal/api/v1/whoami/', {
            credentials: "same-origin",
        })
        .then((res) => res.json())
        .then((data) => {
            username.value = data.username
        })
        .catch((err) => {
            console.log(err)
        });
    }

    async function getSession() {
        await fetch('/intertidal/api/v1/session/', {
            credentials: "same-origin",
        })
        .then((res) => res.json())
        .then((data) => {
            if (data.isAuthenticated) {
                isAuthenticated.value = true
                getUsername()
            } else {
                getCsrf();
            }
        })
        .catch((err) => {
            console.log(err)
        });
    }

    async function login(formData) {
        await fetch('/intertidal/api/v1/login/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken.value,
            },
            credentials: "same-origin",
            body: JSON.stringify(formData),
        })
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
            if (data.success) {
                isAuthenticated.value = true
                username.value = data.username
                message.value = data.detail
            } else {
                message.value = data.detail
            }
        })
        .catch((err) => {
            console.error(err);
        })
    }

    async function logout() {
        fetch('/intertidal/api/v1/logout/', {
            credentials: "same-origin",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            isAuthenticated.value = false
            message.value = null
            getCsrf();
        })
        .catch((err) => {
            console.log(err);
        })
    }

    return {
        username,
        csrfToken,
        isAuthenticated,
        message,
        getCsrf,
        getSession,
        login,
        logout
    }
})
