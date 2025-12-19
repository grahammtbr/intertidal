<script setup>
import { ChevronRight, EllipsisVertical, NotebookText, CalendarDays } from 'lucide-vue-next'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
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
import { Button } from '@/components/ui/button'
import { formatDateTime } from '@/lib/utils'

defineEmits(['selectedItem'])

const props = defineProps({
    item: {
        type: Object,
        default: () => ({}),
    },
})
</script>

<template>
    <div class="relative flex items-center gap-x-3 w-full">
        <Dialog>
            <Popover>
                <PopoverTrigger>
                    <EllipsisVertical :size="20" />
                </PopoverTrigger>
                <PopoverContent align="start" class="flex flex-col w-fit gap-y-3">
                    <div class="flex justify-center items-center gap-x-2 text-[13px] text-gray-500">
                        <CalendarDays :size="20" />
                        <div v-if="props.item.start_date">
                            {{ formatDateTime(props.item.start_date) }} -<br />
                            {{ formatDateTime(props.item.end_date) }}
                        </div>
                        <div v-else>
                            {{ formatDateTime(props.item.start_time, true) }} -<br />
                            {{ formatDateTime(props.item.end_time, true) }}
                        </div>
                    </div>

                    <DialogTrigger>
                        <Button> <NotebookText :size="20" />Notes </Button>
                    </DialogTrigger>
                </PopoverContent>
            </Popover>
            <DialogScrollContent>
                <DialogHeader>
                    <DialogTitle class="pr-8">{{ props.item.name }}</DialogTitle>
                </DialogHeader>
                <div v-if="props.item.note">
                    <pre class="text-sm font-sans text-wrap">{{ props.item.note }}</pre>
                </div>
                <div v-else>No notes!</div>
            </DialogScrollContent>
        </Dialog>

        <button @click="$emit('selectedItem', props.item)" class="item-button flex justify-between items-center text-left w-full hover:text-slate-900">
            {{ props.item.name }}<ChevronRight :size="26" class="item-icon text-slate-600 flex-none ml-4" />
        </button>
    </div>
</template>

<style>
.item-button:hover > .item-icon {
    color: var(--color-slate-900);
}
</style>
