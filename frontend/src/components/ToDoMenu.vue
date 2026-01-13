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
            <ul class="list-disc pl-4 max-w-80 text-sm">
                <li><s>Fix type-ahead search</s></li>
                    <ul class="list-disc pl-4">
                        <li>Switch to fuse.js for fuzzy search</li>
                        <li>Pre-populate datalist from custom endpoint (autoloaded and cached)</li>
                    </ul>
                <li>
                    (partially done) Move survey/deployments into new state so above will work and set parent(s)
                    (override existing current$)
                    <ul class="list-disc pl-4">
                        <li>Copy into session cookie (or localstorage) for logged in users?</li>
                        <li>Save session for non-logged in?</li>
                    </ul>
                </li>
                <li>What info to add to survey point popup?</li>
                <li>Control to zoom out to bounds of all open images/points</li>
                <li>Auth, share auth/session cookies with Django, <a href="https://tinyurl.com/yc27b2vh">https://tinyurl.com/yc27b2vh</a></li>
                <li>What level of data needs to be hidden under auth?</li>
            </ul>
        </DropdownMenuContent>
    </DropdownMenu>
</template>
