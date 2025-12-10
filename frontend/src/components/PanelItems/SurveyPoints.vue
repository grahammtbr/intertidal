<script setup>
import { ref, watch, inject } from 'vue'
import { useFetch } from '@/assets/js/fetch'
import { Switch } from '@/components/ui/switch'
import * as L from 'leaflet'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip'
import { CircleQuestionMark } from 'lucide-vue-next'
import IconQuestion from '../icons/IconQuestion.vue'
import IconInfo from '../icons/IconInfo.vue'
import { mapPadding } from '@/lib/utils'

// This section should be rewritten to format the objects into the GeoJSON format. It will make the further
// addition of survey features easier, and better formatted, as well as extracting many functions into generics
// for future layers, as formatting would be consistent.
// Another possibility is creating a custom API endpoint that returns the GeoJSON format, but this may require DB changes...

const props = defineProps({
    baseDeploymentId: {
        type: Number,
        default: 0,
    },
})

const url = `/api/v1/base_deployments/${props.baseDeploymentId}/survey_points/`
const { data, error } = useFetch(url)

const map = inject('map')
const surveyPointTypes = ref({})
const iconSvg =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6"><path fill-rule="evenodd" d="m11.54 22.351.07.04.028.016a.76.76 0 0 0 .723 0l.028-.015.071-.041a16.975 16.975 0 0 0 1.144-.742 19.58 19.58 0 0 0 2.683-2.282c1.944-1.99 3.963-4.98 3.963-8.827a8.25 8.25 0 0 0-16.5 0c0 3.846 2.02 6.837 3.963 8.827a19.58 19.58 0 0 0 2.682 2.282 16.975 16.975 0 0 0 1.145.742ZM12 13.5a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" clip-rule="evenodd" /></svg>'
const mapBounds = []

// Groups the base deployment survey points by survey_point_type on tab load.
// The watch function waits until the API returns, and only runs if there's valid data.
watch(
    () => data.value,
    (surveyPoints) => {
        if (!surveyPoints) return

        const grouped = {}

        for (const surveyPoint of Object.values(surveyPoints)) {
            const spt = surveyPoint.survey_point_type
            const idName = props.baseDeploymentId + '_' + spt.name

            if (!grouped[idName]) {
                grouped[idName] = {
                    name: spt.name,
                    color: spt.marker_color,
                    note: spt.note,
                    count: 0,
                    isEnabled: false,
                    points: [],
                    markers: [],
                    group: {},
                }
            }

            // Extract the z, y, z coors from the format provided in the database,
            // and add to the grouped object in an array format that is used by Leaflet's LayerGroup
            const coors = surveyPoint.point

            // Regex for three numbers inside parentheses, regex expression provided by ChatGPT
            const match = coors.match(/POINT Z\s*\(\s*([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*\)/)

            if (match) {
                const [_, x, y, z] = match
                const surveyIcon = L.divIcon({
                    className: '',
                    html: `<span class="drop-shadow-sm/50" style="color: ${grouped[idName].color}">${iconSvg}</span>`,
                })

                // add to object for later reference if needed
                // Array.prototype.push.call(grouped[idName].points, {
                //     x: Number(x),
                //     y: Number(y),
                //     z: Number(z),
                // })
                grouped[idName].points.push([Number(y), Number(x)])
                mapBounds.push([Number(y), Number(x)])

                // and build an array of marker objects for Leaflet's layer groups
                grouped[idName].markers.push(
                    L.marker(L.latLng(Number(y), Number(x)), { icon: surveyIcon }).bindPopup(
                        `<strong>Name:</strong> ${surveyPoint.name}<br />
                        <strong>Start Time:</strong> ${surveyPoint.start_time}<br />
                        <strong>End Time:</strong> ${surveyPoint.end_time}<br />
                        <strong>Notes:</strong> ${surveyPoint.note}`,
                    ),
                )
            }

            // TODO: There's a better way to do this, but I'm tired and this works...
            grouped[idName].group = L.layerGroup(grouped[idName].markers)

            grouped[idName].count++
        }

        surveyPointTypes.value = grouped
    },
    { immediate: true },
)

function switchHandler(name, value) {
    let sptName = surveyPointTypes.value[name]
    sptName.isEnabled = value
    if (value) {
        sptName.group.addTo(map.value)
        map.value.flyToBounds(mapBounds, mapPadding)
    } else if (!value) {
        sptName.group.remove()
    }
}
</script>

<template>
    <div v-if="error">Oh no! Error encountered: {{ error.message }}</div>
    <div v-else-if="Object.entries(data).length == 0">No survey points found.</div>
    <div v-else-if="data" class="px-2">
        <div v-for="(attributes, pointType) in surveyPointTypes" :key="pointType" class="flex pb-1">
            <div class="flex items-center gap-x-2 w-22">
                <Switch
                    :id="pointType"
                    :model-value="attributes.isEnabled"
                    @update:model-value="(value) => switchHandler(pointType, value)"
                    :class="`data-[state=unchecked]:bg-[${attributes.color}]/40 data-[state=checked]:bg-[${attributes.color}] shadow-black/20`"
                />
                <!-- <span>{{ attributes.isEnabled }}</span> -->
                <span
                    class="text-sm"
                    :class="[attributes.isEnabled ? 'text-black' : 'text-gray-500']"
                    >({{ attributes.count }})</span
                >
            </div>
            <div class="flex items-center gap-x-2">
                <div>{{ attributes.name }}</div>
                <TooltipProvider>
                    <Tooltip>
                        <TooltipTrigger>
                            <IconInfo class="text-sky-900" />
                        </TooltipTrigger>
                        <TooltipContent class="max-w-64">
                            <p class="font-medium text-center">
                                {{ attributes.note }}
                            </p>
                        </TooltipContent>
                    </Tooltip>
                </TooltipProvider>
            </div>
        </div>
    </div>
    <div v-else>Loading Survey Points...</div>
</template>
