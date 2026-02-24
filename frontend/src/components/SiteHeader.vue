<script setup>
import AccountMenu from './AccountMenu.vue'
import ToDoMenu from './ToDoMenu.vue'
import { Menu, Home } from 'lucide-vue-next';
</script>

<template>
    <header class="fixed z-999 w-full">
        <div
            class="h-15 flex items-center px-6 py-2 bg-slate-50/70 backdrop-blur-2xl shadow-md"
        >
            <div class="w-full flex justify-between">

                <div class="flex items-center gap-x-5">
                    <div class="">
                        <Menu />
                    </div>

                    <a href="/intertidal/">
                        <img
                            alt="MSEA logo"
                            class=""
                            src="@/assets/images/MSEA_logo_FullColour.svg"
                            width="80"
                        />
                    </a>
                    <span class="h-full border-l border-slate-900/20"></span>
                    <div class="flex items-center">
                        <Home size="16" class="mr-1 stroke-slate-900"/>
                        <h1 class="text-base font-medium m-0 text-slate-900">Intertidal Database</h1>
                        <!-- <h2 class="text-[13px] leading-2 m-0">Marine Spatial Ecology & Analysis, DFO/MPO Canada</h2> -->
                    </div>
                </div>

                <div class="flex gap-x-5">
                    <to-do-menu />
                    <span class="border-l border-slate-900/20"></span>
                    <account-menu />
                </div>
            </div>
        </div>
        <!-- <div class="w-full h-8 px-5 bg-slate-100/50 backdrop-blur-2xl shadow-md">
            <div class="h-full flex items-center">
                <Home size="14" class="mr-1 stroke-slate-900"/>
                <h1 class="text-sm font-medium m-0 text-slate-900">Intertidal Surveys</h1>
            </div>
        </div> -->
    </header>
</template>
