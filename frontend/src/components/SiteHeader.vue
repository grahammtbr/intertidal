<script setup>
import AccountMenu from './AccountMenu.vue'
import ToDoMenu from './ToDoMenu.vue'
</script>

<template>
    <header class="fixed z-999 w-full h-16">
        <div
            class="h-full flex justify-between items-center px-4 bg-slate-100/70 backdrop-blur-2xl shadow-md"
        >
            <div class="flex items-center gap-x-6">
                <a href="/intertidal/">
                    <img
                        alt="Vue logo"
                        class="logo"
                        src="@/assets/images/MSEA_logo_FullColour.svg"
                        width="100"
                    />
                </a>
                <div class="">
                    <h1 class="text-2xl font-bold m-0 text-slate-900">Intertidal Surveys Database</h1>
                    <h2 class="text-[13px] leading-4 m-0">Marine Sciences Division, Fisheries and Oceans Canada</h2>
                </div>
            </div>
            <div class="flex gap-x-8">
                <to-do-menu />
                <span class="border-l border-slate-900/20"></span>
                <account-menu />
            </div>
        </div>
        <!-- <div class="w-full h-10 bg-white/50 backdrop-blur-2xl"></div> -->
    </header>
</template>
