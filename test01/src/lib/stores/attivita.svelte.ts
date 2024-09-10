import { writable } from "svelte/store";
export const userActivities = writable<{ nome: string; data: string; completata: boolean }[]>([]);