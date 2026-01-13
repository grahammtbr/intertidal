<script setup>
import { useSurveyStore } from '@/stores/survey'
import { ArrowLeft, NotebookText } from 'lucide-vue-next'
import { Input } from '@/components/ui/input'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip'
import { Search } from 'lucide-vue-next'
import { Button } from '@/components/ui/button'
import {
    Dialog,
    DialogClose,
    DialogScrollContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from '@/components/ui/dialog'
import IconQuestion from '../icons/IconQuestion.vue'
import Surveys from './Surveys.vue'
import Deployments from './Deployments.vue'
import BaseDeployments from './BaseDeployments.vue'

const store = useSurveyStore()
</script>

<template>
    <div class="flex justify-start items-center gap-x-1.5 mb-6">
        <Input type="text" disabled placeholder="Search by location &hellip;" class="rounded-xl" />
        <Search class="absolute right-15 opacity-50" />

        <TooltipProvider>
            <Tooltip>
                <TooltipTrigger>
                    <IconQuestion class="text-sky-900 size-5" />
                </TooltipTrigger>
                <TooltipContent>
                    <p class="font-medium text-center">
                        Survey name, beach name,<br />
                        inlet name, etc.
                    </p>
                </TooltipContent>
            </Tooltip>
        </TooltipProvider>
    </div>
    <div class="relative">
        <div class="flex gap-x-2.5 mb-2">
            <div class="pt-0.5">
                <button
                    @click="store.activePanel--"
                    :class="[store.activePanel == 1 ? 'invisible' : '']"
                >
                    <ArrowLeft :size="24" class="text-slate-600 hover:text-slate-900"/>
                </button>
            </div>
            <Transition name="fade" mode="out-in">
                <div v-if="store.activePanel == 1">
                    <h2 class="text-lg font-medium" v-text="'Surveys'"></h2>
                </div>
                <div v-else-if="store.activePanel == 2" class="w-full flex justify-between gap-x-3">
                    <Dialog>
                        <h2 class="text-lg font-medium" v-text="store.currentSurvey.name"></h2>
                        <DialogTrigger>
                            <Button title="notes" size="icon" class="bg-sky-900">
                                <NotebookText />
                            </Button>
                        </DialogTrigger>
                        <DialogScrollContent>
                            <DialogHeader>
                                <DialogTitle class="pr-8">
                                    {{ store.currentSurvey.name }}
                                </DialogTitle>
                            </DialogHeader>
                            <div v-if="store.currentSurvey.note">
                                <pre class="text-sm font-sans text-wrap">{{
                                    store.currentSurvey.note
                                }}</pre>
                            </div>
                            <div v-else>No notes!</div>
                        </DialogScrollContent>
                    </Dialog>
                </div>
                <div v-else-if="store.activePanel == 3" class="w-full flex justify-between gap-x-3">
                    <Dialog>
                        <h2 class="text-lg font-medium" v-text="store.currentDeployment.name"></h2>
                        <DialogTrigger>
                            <Button title="notes" size="icon" class="bg-sky-900">
                                <NotebookText />
                            </Button>
                        </DialogTrigger>
                        <DialogScrollContent>
                            <DialogHeader>
                                <DialogTitle class="pr-8">
                                    {{ store.currentDeployment.name }}
                                </DialogTitle>
                            </DialogHeader>
                            <div v-if="store.currentDeployment.note">
                                <pre class="text-sm font-sans text-wrap">{{
                                    store.currentDeployment.note
                                }}</pre>
                            </div>
                            <div v-else>No notes!</div>
                        </DialogScrollContent>
                    </Dialog>
                </div>
            </Transition>
        </div>
        <Transition name="slide-fade">
            <div v-if="store.activePanel == 1" id="surveys" class="absolute w-full">
                <Surveys />
            </div>

            <div v-else-if="store.activePanel == 2" id="surveyDeployments" class="absolute w-full">
                <Deployments :survey="store.currentSurvey" />
            </div>

            <div v-else-if="store.activePanel == 3" id="baseDeployments" class="absolute w-full">
                <BaseDeployments :deployment="store.currentDeployment" />
            </div>
        </Transition>
    </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
    transition: all 0.05s;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
    transition: all 0.3s ease-out;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
    transform: translateX(-400px);
    opacity: 0;
}
</style>
