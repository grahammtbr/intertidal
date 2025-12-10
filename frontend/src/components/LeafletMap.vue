<script setup>
import { ref, onMounted, provide } from 'vue'
import 'leaflet/dist/leaflet.css'
import '../assets/css/leaflet.css'
import * as L from 'leaflet'
import SidePanel from './SidePanel.vue'

const props = defineProps({
    center: {
        type: Array,
        default: () => [48.6505, -123.4495], // IOS
    },
    zoom: {
        type: Number,
        default: 9,
    },
    baseLayers: {
        type: Object,
        required: true,
    },
    overlays: {
        type: Object,
        default: () => ({}),
    },
    options: {
        type: Object,
        default: () => ({}),
    },
    height: {
        type: String,
        default: '400px',
    },
})

const map = ref(null)

onMounted(() => {
    map.value = L.map('map', {
        center: props.center,
        zoom: props.zoom,
        zoomControl: false,
        options: props.options,
    })

    const leafletBaseLayers = {}
    const leafletOverlays = {}
    let firstBaseLayer = null

    // Register one or more base layers
    for (const [name, config] of Object.entries(props.baseLayers)) {
        const layer = L.tileLayer(config.url, config.options || {})
        leafletBaseLayers[name] = layer

        // and load the first base layer by default
        if (!firstBaseLayer) {
            firstBaseLayer = layer
            layer.addTo(map.value)
        }
    }

    // Register one or more tile overlays on load
    for (const [name, config] of Object.entries(props.overlays)) {
        const layer = L.tileLayer(config.url, config.options || {})
        leafletOverlays[name] = layer
        layer.addTo(map.value)
    }

    L.control.layers(leafletBaseLayers, leafletOverlays).addTo(map.value)
    L.control.zoom({ position: 'bottomright' }).addTo(map.value)
})

provide('map', map)
</script>

<template>
    <div id="map" :style="{ height: props.height, width: '100%' }"></div>
    <SidePanel />
</template>
