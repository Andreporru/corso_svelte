import { writable } from 'svelte/store';
export const userLogs = writable<{ nlog: string; data: string }[]>([]);

