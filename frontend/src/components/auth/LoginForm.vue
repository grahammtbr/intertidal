<script setup>
import { reactive, onMounted } from "vue"
//import { useRouter } from 'vue-router'
import { useAuthStore } from "@/stores/auth"
import {
    Field,
    FieldDescription,
    FieldGroup,
    FieldLabel,
    FieldSet,
} from '@/components/ui/field'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'

const auth = useAuthStore()

const formData = reactive({
    username: null,
    password: null,
})

const submitHandler = () => {
    auth.login(formData)
}

// onMounted(() => {
//     auth.getSession()
// })
</script>

<template>
    <div v-if="auth.isAuthenticated">
        <div v-if="auth.message">
            {{ auth.message }}
        </div>
    </div>
    <div v-else>
        <form @submit.prevent="submitHandler">
            <FieldSet>
                <FieldGroup>
                    <Field>
                        <FieldLabel for="username">
                            Username
                        </FieldLabel>
                        <Input id="username" type="text" placeholder="username" v-model="formData.username" />
                        <!-- <FieldDescription></FieldDescription> -->
                    </Field>
                    <Field>
                        <FieldLabel for="password">
                            Password
                        </FieldLabel>
                        <!-- <FieldDescription></FieldDescription> -->
                        <Input id="password" type="password" placeholder="********" v-model="formData.password" />
                    </Field>
                    <div v-if="auth.message" class="text-sm text-red-600">
                        {{ auth.message }}
                    </div>
                    <Field orientation="horizontal">
                        <Button type="submit">
                            Log in
                        </Button>
                    </Field>
                </FieldGroup>
            </FieldSet>
        </form>
    </div>
</template>
