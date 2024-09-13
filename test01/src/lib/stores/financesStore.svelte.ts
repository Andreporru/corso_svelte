import { writable } from 'svelte/store';
import { storeUser } from './user.svelte';

interface Spesa {
    descrizione: string;
    importo: number;
}


export const financesStore = (() => {
    const { subscribe, set, update } = writable<Spesa[]>([]);

  
    const loadExpenses = (id: string) => {
        if (storeUser.id !=null) {
            const savedExpenses = localStorage.getItem(`expenses_${id}`);
            if (savedExpenses) {
                set(JSON.parse(savedExpenses));
            }
        }
    };

    const saveExpenses = (expenses: Spesa[]) => {
        if (storeUser.id !=null) {
            localStorage.setItem(`expenses_${storeUser.id}`, JSON.stringify(expenses));
        }
    };

   
    const addExpense = (descrizione: string, importo: number) => {
        update((expenses: never) => {
            const newExpenses = [...expenses, { descrizione, importo }];
            saveExpenses(newExpenses);
            return newExpenses;
        });
    };

 
    const removeExpense = (index: number) => {
        update((expenses: never[]) => {
            const newExpenses = expenses.filter((_: never, i: number) => i !== index);
            saveExpenses(newExpenses);
            return newExpenses;
        });
    };

    const resetExpenses = () => {
        set([]);

    };

    return {
        subscribe,
        loadExpenses,
        addExpense,
        removeExpense,
        resetExpenses
    };
})();