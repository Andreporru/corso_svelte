// src/stores/financesStore.ts
import { writable } from 'svelte/store';
import { storeUser } from './user.svelte';


// Tipo per una spesa
interface Expense {
    description: string;
    amount: number;
}

// Store per la gestione delle spese
export const financesStore = (() => {
    const { subscribe, set, update } = writable<Expense[]>([]);

    // Carica le spese dal localStorage
    const loadExpenses = () => {
        const savedExpenses = localStorage.getItem(`expenses_${storeUser.id}`);
        if (savedExpenses) {
            set(JSON.parse(savedExpenses));
        }
    };

    // Salva le spese nel localStorage
    const saveExpenses = (expenses: Expense[]) => {
        localStorage.setItem(`expenses_${storeUser.id}`, JSON.stringify(expenses));
    };

    // Aggiunge una nuova spesa
    const addExpense = (description: string, amount: number) => {
        update(expenses => {
            const newExpenses = [...expenses, { description, amount }];
            saveExpenses(newExpenses);
            return newExpenses;
        });
    };

    // Rimuove una spesa
    const removeExpense = (index: number) => {
        update(expenses => {
            const newExpenses = expenses.filter((_, i) => i !== index);
            saveExpenses(newExpenses);
            return newExpenses;
        });
    };

    // Inizializza caricando le spese esistenti
  

        


    loadExpenses();
    return {
        subscribe,
        addExpense,
        removeExpense
    };
})();