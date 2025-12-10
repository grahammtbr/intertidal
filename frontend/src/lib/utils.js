import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs) {
    return twMerge(clsx(inputs))
}

export const mapPadding = { paddingTopLeft: [400, 64] }

export function formatDateTime(dateTime, time = false) {
    const dt = new Date(dateTime)
    const options = {
        month: 'long',
        day: 'numeric',
        year: 'numeric',
    }
    let addTime = {}

    if (time) addTime = { hour: 'numeric', minute: 'numeric', second: 'numeric' }

    const formatted = new Intl.DateTimeFormat('en-US', { ...options, ...addTime })

    return formatted.format(dt)
}
