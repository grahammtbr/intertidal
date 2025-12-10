<script setup>
import LeafletMap from '../components/LeafletMap.vue'
import SidePanel from '@/components/SidePanel.vue'

const baseUrl = import.meta.env.VITE_TILES_URL

const baseLayers = {
    'Google Earth': {
        url: 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        options: {
            maxZoom: 21,
            attribution: '© Google',
        },
    },
    'ArcGIS World Imagery': {
        url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        options: {
            maxZoom: 18,
            attribution: '© Esri, Maxar, Earthstar Geographics, and the GIS User Community',
        },
    },
    // 'MSEA Titles': {
    //     url: `${baseUrl}/calvert_2023_5_d1_f1_rgb/{z}/{x}/{y}.png`,
    //     options: {
    //         maxZoom: 16,
    //         attribution: '© Fisheries and Oceans, Canada',
    //     },
    // },
}

// Optional overlays on load, maybe to be used later for default flight rasters?
// const overlays = {
//     Label: {
//         url: 'https://{s}.somedomain.com/{foo}/{z}/{x}/{y}.png',
//         options: {
//             opacity: 0.7,
//         },
//     },
// }
</script>

<template>
    <main>
        <LeafletMap :baseLayers="baseLayers" height="100vh" />
    </main>
</template>
