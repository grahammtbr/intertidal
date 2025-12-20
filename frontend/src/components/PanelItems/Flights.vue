<script setup>
import { ref, watch, inject } from 'vue'
import { useFetch } from '@/assets/js/fetch'
import { Drone } from 'lucide-vue-next'
import { Switch } from '@/components/ui/switch'
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger, } from '@/components/ui/accordion'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip'
import IconInfo from '../icons/IconInfo.vue'
import { Button } from '@/components/ui/button'
import {
    Dialog,
    DialogClose,
    DialogScrollContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from '@/components/ui/dialog'
import * as L from 'leaflet'
import { mapPadding } from '@/lib/utils'

const props = defineProps({
    deploymentId: {
        type: Number,
        default: 0,
    },
})
const map = inject('map')
const mapBounds = []
const tilesBaseUrl = import.meta.env.VITE_TILES_URL
const tilesAttribution = import.meta.env.VITE_TILES_ATTRIBUTION
const tilesMaxZoom = import.meta.env.VITE_TILES_MAX_ZOOM
const rasterTileLayers = ref({})

const url = `/api/v1/deployments/${props.deploymentId}/rpas_flights/`
const { data, error } = useFetch(url)

watch(
    () => data.value,
    (flights) => {
        if (!flights) return

        const layers = {}

        for (const flight of Object.values(flights)) {
            for (const rasters of Object.values(flight.rasters)) {
                const rr = rasters.raster
                const url = `${tilesBaseUrl}/${rr.tile_dir}/{z}/{x}/{y}.png`

                const match = rr.extent.match(/POLYGON\s*\(\(\s*(.*?)\s*\)\)/);
                const coors = match[1]
                    .split(',')
                    .map(pair => {
                        const [y, x] = pair.trim().split(/\s+/).map(Number);
                        return [ x, y ];
                    });

                layers[rr.tile_dir] = {
                    tileLayer: L.tileLayer(url, { maxZoom: tilesMaxZoom, attribution: tilesAttribution }),
                    extent: coors,
                }
                rr.tileLayer = L.tileLayer(url, { maxZoom: tilesMaxZoom, attribution: tilesAttribution })
                rr.extentCoors = coors
                rr.isEnabled = false
            }
        }
        //console.log(flights)
        rasterTileLayers.value = layers
    },
    { immediate: true },
)

function switchHandler(raster, value) {
    raster.isEnabled = value
    if (value) {
        raster.tileLayer.addTo(map.value)
        map.value.flyToBounds(raster.extentCoors, mapPadding)
    } else if (!value) {
        raster.tileLayer.removeFrom(map.value)
    }
}
</script>

<template>
    <h3 class="font-medium mb-4">Flight Raster Images</h3>
    <div v-if="error">Oh no! Error encountered: {{ error.message }}</div>
    <div v-else-if="Object.entries(data).length == 0">No flight images found.</div>
    <div v-else-if="data">
        <Accordion type="single" collapsible class="w-full border-t border-t-slate-400" :default-value="'item-' + data[0].id">
            <div v-for="flight in data" :key="flight.id">
                <AccordionItem :value="'item-' + flight.id" class="border-b-slate-400">
                    <AccordionTrigger class="py-3">
                        {{ flight.plan_name }}
                    </AccordionTrigger>
                    <AccordionContent>
                        <div class="flex justify-between">
                            <div>
                                <div v-for="(rasterType, rasters) in flight.rasters" :key="rasters" class="flex items-center gap-3 pb-2">
                                    <!-- <Switch
                                        :id="rasterType.raster.id"
                                        :model-value="attributes.isEnabled"
                                        @update:model-value="(value) => switchHandler(pointType, value)"
                                        :class="`data-[state=unchecked]:bg-[${attributes.color}]/40 data-[state=checked]:bg-[${attributes.color}] shadow-black/20`"
                                    /> -->
                                    <Switch
                                        :id="'raster-' + rasterType.raster.id"
                                        :model-value="rasterType.raster.isEnabled"
                                        @update:model-value="(value) => switchHandler(rasterType.raster, value)"
                                        class="shadow-black/20"
                                    />
                                    <div class="flex items-center gap-x-2">
                                        <span>{{ rasterType.raster.type.name }}</span>
                                        <TooltipProvider>
                                            <Tooltip>
                                                <TooltipTrigger>
                                                    <IconInfo class="text-sky-900" />
                                                </TooltipTrigger>
                                                <TooltipContent class="max-w-64">
                                                    <p v-if="rasterType.raster.type.id == 1" class="font-medium mb-1">
                                                        High-resolution full-colour surface image
                                                    </p>
                                                    <p v-else-if="rasterType.raster.type.id == 2" class="font-medium mb-1">
                                                        High-resolution near-infrared/ultraviolet/RBG surface imagery
                                                    </p>
                                                    <p v-else-if="rasterType.raster.type.id == 3" class="font-medium mb-1">
                                                        High-resolution 3D digital surface model
                                                    </p>
                                                    Units?
                                                    <ul class="font-medium">
                                                        <li>Size: {{rasterType.raster.size}}</li>
                                                        <li>Resolution: {{rasterType.raster.resolution}}</li>
                                                        <li>Width: {{rasterType.raster.width}}</li>
                                                        <li>Height: {{rasterType.raster.height}}</li>
                                                        <li>SRID: {{rasterType.raster.srid}}</li>
                                                        <li>Bands: {{rasterType.raster.bands}}</li>
                                                    </ul>
                                                </TooltipContent>
                                            </Tooltip>
                                        </TooltipProvider>
                                    </div>
                                </div>
                            </div>
                            <div class="flex gap-2 mb-6">
                                <!-- <TooltipProvider>
                                    <Tooltip>
                                        <TooltipTrigger class="cursor-pointer">
                                            <Button>
                                                <Drone :size="20" />Flight Info
                                            </Button>
                                        </TooltipTrigger>
                                        <TooltipContent>
                                            <pre class="font-sans font-medium text-wrap">{{ flight.note }}</pre>
                                        </TooltipContent>
                                    </Tooltip>
                                </TooltipProvider> -->
                                <Dialog>
                                    <DialogTrigger>
                                        <Button title="flight" class="bg-sky-900">
                                            <Drone />Details
                                        </Button>
                                    </DialogTrigger>
                                    <DialogScrollContent>
                                        <DialogHeader>
                                            <DialogTitle class="text-xl pr-8">
                                                {{ flight.plan_name }}
                                            </DialogTitle>
                                        </DialogHeader>
                                        <div>
                                            <h3 class="text-base font-semibold mb-1">RPAS (Drone)</h3>
                                            <div class="text-sm">{{ flight.rpas.brand }} {{ flight.rpas.model }}</div>
                                            <span>{{ flight.rpas.note }}</span>
                                        </div>
                                        <div>
                                            <h3 class="text-base font-semibold mb-1">Flight Details</h3>
                                            <ul class="text-sm">
                                                <li>Flight Altitude: <span class="font-medium">{{ flight.altitude }}m</span></li>
                                                <li>Flight Velocity: <span class="font-medium">{{ flight.velocity }} km/h</span></li>
                                                <li>Camera Aperture: <span class="font-medium">{{ flight.aperture }}</span></li>
                                                <li>Camera Shutter Speed: <span class="font-medium">{{ flight.shutter_speed }}</span></li>
                                                <li>Camera ISO: <span class="font-medium">{{ flight.iso }}</span></li>
                                            </ul>
                                        </div>
                                        <div>
                                            <h3 class="text-base font-semibold mb-1">Personal</h3>
                                            <span class="text-sm"></span>
                                        </div>
                                        <div>
                                            <h3 class="text-base font-semibold mb-1">Notes</h3>
                                            <div v-if="flight.note">
                                                <pre class="text-sm font-sans text-wrap">{{
                                                    flight.note
                                                }}</pre>
                                            </div>
                                            <div v-else>No notes!</div>
                                        </div>
                                    </DialogScrollContent>
                                </Dialog>
                            </div>
                        </div>
                    </AccordionContent>
                </AccordionItem>
            </div>
        </Accordion>
    </div>
    <div v-else>Loading Base Deployments...</div>
</template>
