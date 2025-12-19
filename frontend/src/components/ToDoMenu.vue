<script setup>
import { ChevronDown } from 'lucide-vue-next'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuPortal,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuSub,
    DropdownMenuSubContent,
    DropdownMenuSubTrigger,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
</script>

<template>
    <DropdownMenu>
        <DropdownMenuTrigger as-child>
            <div class="font-semibold flex items-center gap-x-1 cursor-default">
                <span>To Do</span>
                <ChevronDown :size="16" :stroke-width="2" class="mt-0.5" />
            </div>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end" class="z-1001 py-3 px-4">
            <ul class="list-disc pl-4 max-w-72 text-sm">
                <li>Fix type-ahead search</li>
                <li>
                    Move survey/deployments into new state so above will work and set parent(s)
                    (override existing current$)
                </li>
                <li>Fix Leaflet layer control - may need custom</li>
                    <ul class="list-disc pl-4"><li class="inde">Not broken, ARC base map is - remove or find replacement?</li></ul>
                <li>What info to add to survey point popup?</li>
                <li>Control to zoom out to bounds of all open images/points</li>
            </ul>
        </DropdownMenuContent>
    </DropdownMenu>
</template>
