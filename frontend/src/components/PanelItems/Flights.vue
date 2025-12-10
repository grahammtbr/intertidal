<script setup>
import { ref, watch, inject } from 'vue'
import { useFetch } from '@/assets/js/fetch'
import { Switch } from '@/components/ui/switch'
import * as L from 'leaflet'

const props = defineProps({
    deploymentId: {
        type: Number,
        default: 0,
    },
})

const url = `/api/v1/deployments/${props.deploymentId}/rpas_flights/`
const { data, error } = useFetch(url)
</script>

<template>
    <div v-if="error">Oh no! Error encountered: {{ error.message }}</div>
    <div v-else-if="data">Disabled, pending tile server reemergence.</div>
    <div v-else>Loading Base Deployments...</div>
</template>
