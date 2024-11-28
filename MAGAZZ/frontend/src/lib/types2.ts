import { writable } from 'svelte/store';
import type { Item } from './types';

export const articoliStore = writable<Item[]>([]);
export const valore=writable<number>();
