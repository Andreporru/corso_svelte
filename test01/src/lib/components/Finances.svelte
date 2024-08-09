<script lang="ts">
    import { financesStore } from '$lib/stores/financesStore';
	import { storeUser } from '$lib/stores/user.svelte';
    import { onMount } from 'svelte';
    const loadExpenses = () => {
        const savedExpenses = localStorage.getItem(`expenses_${storeUser.id}`);
        if (savedExpenses) {
            new Set(JSON.parse(savedExpenses));
        }
    };

    let description = '';
    let amount: number | null = null;

    // Funzione per aggiungere una nuova spesa
    const addExpense = () => {
        if (description.trim() && amount !== null && amount > 0) {
            financesStore.addExpense(description, amount);
            description = '';
            amount = null;
        }
    };

    // Funzione per rimuovere una spesa
    const removeExpense = (index: number) => {
        financesStore.removeExpense(index);
    };
    onMount(() => {
        loadExpenses();
    });
    
</script>

<!-- Interfaccia utente -->
<div class="container" style="margin-top:100px;">
    {#if storeUser.id>0}
        <h1>Gestione Finanze</h1>

        <div class="input-group">
            <input
                type="text"
                placeholder="Descrizione"
                bind:value={description}
            />
            <input
                type="number"
                placeholder="Importo"
                bind:value={amount}
            />
            <button on:click={addExpense}>Aggiungi Spesa</button>
        </div>

        <ul>
            {#each $financesStore as expense, index}
                <li>
                    {expense.description} - {expense.amount.toFixed(2)}€
                    <button on:click={() => removeExpense(index)}>Rimuovi</button>
                </li>
            {/each}
        </ul>
    {:else}
        <h1 class="error">ERRORE</h1>
        <p class="error">Non è possibile visualizzare e/o inserire le attività perché l'utente non ha effettuato il login</p>
    {/if}
</div>


<style>
      .error::-moz-progress-bar {
       font-size: 18px;
   }
   .error {
       color: red;
       text-align: center;
   }
    .container {
        font-family: Arial, sans-serif;
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f4f4f9;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: blueviolet;
        font-size: 24px;
        margin-bottom: 20px;
        text-align: center;
    }

    .input-group {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }

    input[type="text"],
    input[type="number"] {
        flex: 1;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    button {
        padding: 10px 20px;
        background-color: blueviolet;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: rgb(78, 0, 78);
    }

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        background-color: #f2f2f2;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    li:hover {
        transform: translateY(-2px);
    }
</style>