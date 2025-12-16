<script setup>
import AccountMenu from './AccountMenu.vue'
import ToDoMenu from './ToDoMenu.vue'
</script>

<template>
    <header class="fixed z-999 w-full h-16">
        <div
            class="h-full flex justify-between items-center px-4 bg-slate-100/70 backdrop-blur-2xl shadow-md"
        >
            <div class="flex items-end gap-x-6">
                <img
                    alt="Vue logo"
                    class="logo"
                    src="@/assets/images/MSEA_logo_FullColour.svg"
                    width="120"
                />
                <h1 class="text-2xl font-bold mb-0.5 text-slate-800">Intertidal Surveys Database</h1>
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
