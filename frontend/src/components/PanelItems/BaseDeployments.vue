<script setup>
import { useFetch } from '@/assets/js/fetch'
import { useSurveyStore } from '@/stores/survey'
import { MapPin, Send, FileDown, Antenna, UserRound } from 'lucide-vue-next'
import { TabsContent, TabsIndicator, TabsList, TabsRoot, TabsTrigger } from 'reka-ui'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip'
import { Button } from '@/components/ui/button'
import { ButtonGroup } from '@/components/ui/button-group'
import { formatDateTime } from '@/lib/utils'
import SurveyPoints from './SurveyPoints.vue'
import Flights from './Flights.vue'

const store = useSurveyStore()

const props = defineProps({
    deployment: {
        type: Object,
        required: true,
    },
})

const url = `/api/v1/deployments/${props.deployment.id}/base_deployments/`
const { data, error } = useFetch(url)
</script>

<template>
    <div class="flex flex-col gap-y-1 mb-4 px-2 text-sm">
        <div class="flex justify-between">
            <span class="text-gray-500 font-semibold">Start Time:</span>
            <span class="font-medium">{{ formatDateTime(props.deployment.start_time, true) }}</span>
        </div>
        <div class="flex justify-between">
            <span class="text-gray-500 font-semibold">End Time:</span>
            <span class="font-medium">{{ formatDateTime(props.deployment.end_time, true) }}</span>
        </div>
    </div>

    <TabsRoot class="flex flex-col w-full" default-value="tab1">
        <TabsList
            class="relative shrink-0 flex border-b border-slate-400"
            aria-label="Manage your account"
        >
            <TabsIndicator
                class="absolute px-8 left-0 h-[3px] bottom-0 w-[var(--reka-tabs-indicator-size)] translate-x-[var(--reka-tabs-indicator-position)] translate-y-[1px] rounded-full transition-all duration-300"
            >
                <div class="bg-sky-600 w-full h-full"></div>
            </TabsIndicator>

            <TabsTrigger
                class="px-5 h-[40px] flex-1 flex items-center justify-center text-sm leading-none text-mauve11 select-none rounded-tl-md hover:text-grass11 data-[state=active]:text-grass11 outline-none cursor-default focus-visible:relative focus-visible:shadow-[0_0_0_2px] focus-visible:shadow-black"
                value="tab1"
            >
                <span class="flex items-center gap-x-1"><MapPin :size="16" /> Survey Points</span>
            </TabsTrigger>
            <TabsTrigger
                class="px-5 h-[40px] flex-1 flex items-center justify-center text-sm leading-none text-mauve11 select-none rounded-tr-md hover:text-grass11 data-[state=active]:text-grass11 outline-none cursor-default focus-visible:relative focus-visible:shadow-[0_0_0_2px] focus-visible:shadow-black"
                value="tab2"
            >
                <span class="flex items-center gap-x-1"><Send :size="16" /> Flights</span>
            </TabsTrigger>
        </TabsList>
        <TabsContent
            class="grow py-4 rounded-b-md outline-none focus:shadow-[0_0_0_2px] focus:shadow-transparent"
            value="tab1"
        >
            <div v-for="baseDeployment in data" :key="baseDeployment.id">
                <div v-if="error">Oh no! Error encountered: {{ error.message }}</div>
                <div v-else-if="data">
                    <div class="flex justify-between items-center gap-x-2 mb-2.5">
                        <h2 class="mr-2">Base Deployment</h2>
                        <TooltipProvider>
                            <ButtonGroup>
                                <Button size="icon" class="border-r border-black cursor-pointer">
                                    <Tooltip>
                                        <TooltipTrigger class="cursor-pointer">
                                            <FileDown :size="18" />
                                        </TooltipTrigger>
                                        <TooltipContent>
                                            <p class="font-medium">Download base deployment file</p>
                                        </TooltipContent>
                                    </Tooltip>
                                </Button>

                                <Button size="icon" class="border-r border-black">
                                    <Tooltip>
                                        <TooltipTrigger>
                                            <Antenna :size="18" />
                                        </TooltipTrigger>
                                        <TooltipContent>
                                            <p class="font-medium mb-2">
                                                Brand: {{ baseDeployment.gps.brand }}<br />
                                                Model: {{ baseDeployment.gps.model }}
                                            </p>
                                            <p class="font-medium">{{ baseDeployment.gps.note }}</p>
                                        </TooltipContent>
                                    </Tooltip>
                                </Button>

                                <Button size="icon">
                                    <Tooltip>
                                        <TooltipTrigger>
                                            <UserRound :size="18" />
                                        </TooltipTrigger>
                                        <TooltipContent>
                                            <p class="font-medium">
                                                Manager: {{ baseDeployment.manager.first_name }}
                                                {{ baseDeployment.manager.last_name }}
                                            </p>
                                            <p class="font-medium">
                                                Email:
                                                <a :href="`mailto:${baseDeployment.manager.email}`">
                                                    {{ baseDeployment.manager.email }}
                                                </a>
                                            </p>
                                        </TooltipContent>
                                    </Tooltip>
                                </Button>
                            </ButtonGroup>
                        </TooltipProvider>
                    </div>
                    <div class="flex flex-col gap-y-1 mb-4 px-2 text-sm">
                        <div class="flex justify-between">
                            <span class="text-gray-500 font-medium">Start Time:</span>
                            <span class="font-medium">{{
                                formatDateTime(baseDeployment.start_time, true)
                            }}</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-500 font-medium">End Time:</span>
                            <span class="font-medium">{{
                                formatDateTime(baseDeployment.end_time, true)
                            }}</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-500 font-medium">Base Height:</span>
                            <span class="font-medium">{{ baseDeployment.base_height }}</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-500 font-medium">Antenna Height:</span>
                            <span class="font-medium">{{ baseDeployment.antenna_height }}</span>
                        </div>
                    </div>
                    <SurveyPoints :baseDeploymentId="baseDeployment.id" />
                </div>
                <div v-else>Loading Base Deployments...</div>
            </div>
        </TabsContent>
        <TabsContent
            class="grow py-4 rounded-b-md outline-none focus:shadow-[0_0_0_2px] focus:shadow-transparent"
            value="tab2"
        >
            <Flights :deploymentId="props.deployment.id" />
        </TabsContent>
    </TabsRoot>
</template>
