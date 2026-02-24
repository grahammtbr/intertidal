<script setup>
import { useAuthStore } from '@/stores/auth';
import { ChevronDown } from 'lucide-vue-next'
//import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
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
import {
    Dialog,
    DialogContent,
    DialogClose,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from '@/components/ui/dialog'
import { Button } from '@/components/ui/button'
import LoginForm from './auth/LoginForm.vue';

const user = useAuthStore()
</script>

<template>
    <Dialog>
        <DropdownMenu>
            <DropdownMenuTrigger as-child>
                <div class="flex items-center gap-x-2 px-0.5 border border-slate-900/30 rounded-full">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="currentColor"
                        class="size-8 fill-slate-700"
                    >
                        <path
                            fill-rule="evenodd"
                            d="M18.685 19.097A9.723 9.723 0 0 0 21.75 12c0-5.385-4.365-9.75-9.75-9.75S2.25 6.615 2.25 12a9.723 9.723 0 0 0 3.065 7.097A9.716 9.716 0 0 0 12 21.75a9.716 9.716 0 0 0 6.685-2.653Zm-12.54-1.285A7.486 7.486 0 0 1 12 15a7.486 7.486 0 0 1 5.855 2.812A8.224 8.224 0 0 1 12 20.25a8.224 8.224 0 0 1-5.855-2.438ZM15.75 9a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z"
                            clip-rule="evenodd"
                        />
                    </svg>
                    <div class="font-semibold flex items-center gap-x-1 cursor-default">
                        <div v-if="user.isAuthenticated">
                            <span>{{ user.username }}</span>
                        </div>
                        <div v-else>
                            <span>Guest</span>
                        </div>
                        <ChevronDown :size="16" :stroke-width="2" class="mt-0.5" />
                    </div>
                </div>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" class="z-1001 min-w-32">
                <div v-if="user.isAuthenticated">
                    <DropdownMenuItem @click="user.logout()">
                        <span>Logout</span>
                    </DropdownMenuItem>
                </div>
                <div v-else>
                    <DialogTrigger as-child>
                        <DropdownMenuItem>
                            <span>Log in</span>
                        </DropdownMenuItem>
                    </DialogTrigger>
                    <DropdownMenuItem>
                        <span>Request Account</span>
                    </DropdownMenuItem>
                </div>
            </DropdownMenuContent>
        </DropdownMenu>
        <DialogContent>
            <DialogHeader>
                <div v-if="!user.isAuthenticated">
                    <DialogTitle>Account Login</DialogTitle>
                    <DialogDescription class="mt-1">
                        If you do not have an account and require one, you can request one <a href="#" class="text-sky-800 hover:text-sky-600 underline transition-colors">here</a>.
                    </DialogDescription>
                </div>
                <div v-else>
                    <DialogTitle>Welcome, {{ user.username }}</DialogTitle>
                </div>
            </DialogHeader>
            <LoginForm />
            <div v-if="user.isAuthenticated">
                <DialogFooter class="sm:justify-start">
                    <DialogClose as-child>
                        <Button type="button" variant="secondary">
                            Close
                        </Button>
                    </DialogClose>
                </DialogFooter>
            </div>
        </DialogContent>
    </Dialog>
</template>
