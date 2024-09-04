<script lang="ts">
	import { financesStore } from '$lib/stores/financesStore';
	import { storeUser } from '$lib/stores/user.svelte';
	import { onMount } from 'svelte';

	let description = '';
	let amount: number | null = null;

	const loadExpenses = () => {
		if (storeUser.id != null) {
			financesStore.resetExpenses();
			financesStore.loadExpenses(); // Chiama la funzione loadExpenses direttamente dal store
		}
	};

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

	const convertiCsv = () => {
		const headers = 'SPESA;IMPORTO\n';
		let rows = '';

		const spese = $financesStore;

		for (let i = 0; i < spese.length; i++) {
			const finanze = spese[i];
			const row = `${finanze.description};${finanze.amount}\n`;
			rows += row;
		}

		return headers + rows;
	};

	const scaricaCsv = () => {
		const spese = $financesStore;
		const csvData = convertiCsv();
		const blob = new Blob([csvData], { type: 'text/csv' });
		const url = URL.createObjectURL(blob);
		const link = document.createElement('a');
		link.href = url;
		link.download = `${storeUser.name}_spese(${spese.length}).csv`;
		link.click();
		console.log('fatto');
		URL.revokeObjectURL(url);
	};

	onMount(() => {
		loadExpenses();
	});
</script>

<br /><br />
<div class="container">
	{#if storeUser.id != ''}
		<h1>Gestione Finanze</h1>

		<div class="input-group">
			<input type="text" placeholder="Descrizione" bind:value={description} />
			<input type="number" placeholder="Importo" bind:value={amount} />
			<button onclick={addExpense}>Aggiungi Spesa</button>
			<button onclick={scaricaCsv}>Estrai csv</button>
		</div>

		<ul>
			{#each $financesStore as expense, index}
				<li>
					{expense.description} - {expense.amount.toFixed(2)}€
					<button onclick={() => removeExpense(index)}>Rimuovi</button>
				</li>
			{/each}
		</ul>
	{:else}
		<h1 class="error">ERRORE</h1>
		<p class="error">
			Non è possibile visualizzare e/o inserire le attività perché l'utente non ha effettuato il
			login
		</p>
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
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
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

	input[type='text'],
	input[type='number'] {
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
