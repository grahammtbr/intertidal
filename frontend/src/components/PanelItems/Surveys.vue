<script setup>
import { useFetch } from '@/assets/js/fetch'
import { useSurveyStore } from '@/stores/survey'
import ListItems from './ListItems.vue'

const store = useSurveyStore()

const url = '/api/v1/surveys/'
const { data, error } = useFetch(url)
</script>

<template>
    <div v-if="error">Oh no! Error encountered: {{ error.message }}</div>
    <div v-else-if="data">
        <div
            v-for="survey in data"
            :key="survey.id"
            class="flex justify-between items-center gap-x-4 py-1.5 first:pt-1 text-base"
        >
            <ListItems :item="survey" @selectedItem="store.setCurrentSurvey(survey)" />
        </div>
    </div>
    <div v-else>Loading Deployments...</div>
</template>
