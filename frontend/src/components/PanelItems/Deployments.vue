<script setup>
import { useFetch } from '@/assets/js/fetch'
import { useSurveyStore } from '@/stores/survey'
import { formatDateTime } from '@/lib/utils'
import ListItems from './ListItems.vue'

const store = useSurveyStore()

const props = defineProps({
    survey: {
        type: Object,
        required: true,
    },
})

const url = `/api/v1/surveys/${props.survey.id}/deployments/`
const { data, error } = useFetch(url)
</script>

<template>
    <div v-if="error">Oh no! Error encountered: {{ error.message }}</div>
    <div v-else-if="data">
        <div class="flex flex-col gap-y-1 mb-4 px-2 text-sm">
            <div class="flex justify-between">
                <span class="text-gray-500 font-medium">Start Date:</span>
                <span class="font-medium">{{ formatDateTime(props.survey.start_date) }}</span>
            </div>
            <div class="flex justify-between">
                <span class="text-gray-500 font-medium">End Date:</span>
                <span class="font-medium">{{ formatDateTime(props.survey.end_date) }}</span>
            </div>
        </div>
        <div
            v-for="deployment in data"
            :key="deployment.id"
            class="flex justify-between items-center gap-x-4 py-1 first:pt-1 text-base"
        >
            <ListItems :item="deployment" @selectedItem="store.setCurrentDeployment(deployment)" />
        </div>
    </div>
    <div v-else>Loading Deployments...</div>
</template>
