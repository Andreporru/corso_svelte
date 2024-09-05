<script lang="ts">
	import { financesStore } from '$lib/stores/financesStore';
	import { storeUser } from '$lib/stores/user.svelte';
	import { onMount } from 'svelte';

	let description = '';
	let amount: number | null = null;

	const loadExpenses = () => {
		if (storeUser.id != null) {
			financesStore.resetExpenses();
			financesStore.loadExpenses(); 
		}
	};


	const addExpense = () => {
		if (description.trim() && amount !== null && amount > 0) {
			financesStore.addExpense(description, amount);
			description = '';
			amount = null;
		}
	};

	
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
	const stampa = () => {
		let c:number=0;
		const printEL = window.open('', '_blank');
		if (printEL) {
			const spese = $financesStore;
			let speseHtml = '';

			spese.forEach((finanze) => {
				c=c+1;
				speseHtml += `
					<tr>
						<td>${c}</td>
						<td>${finanze.description}</td>
						<td>${finanze.amount.toFixed(2)}€</td>
					</tr>
				`;
			});

			printEL.document.open();
			printEL.document.write(`
				<html>
					<head>
						<title>stampa_spese_${storeUser.name}_${storeUser.surname}</title>
						<style>
							table {
								width: 100%;
								border-collapse: collapse;
								margin-top: 20px;
								font-family: Arial, sans-serif;
							}
							th, td {
								border: 1px solid #ddd;
								padding: 8px;
								text-align: left;
							}
							th {
								background-color: #f4f4f4;
								color: #333;
								font-weight: bold;
							}
							tr:nth-child(even) {
								background-color: #f9f9f9;
							}
							tr:hover {
								background-color: #f1f1f1;
							}
							td {
								color: #555;
							}
							table {
								box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
							}
						</style>
					</head>
					<body>
						<h1>Spese di ${storeUser.name} ${storeUser.surname}</h1>
						<table>
							<thead>
								<tr>
									<th>N°</th>
									<th>Descrizione</th>
									<th>Totale</th>
								</tr>
							</thead>
							<tbody>
								${speseHtml}
							</tbody>
						</table>
					</body>
				</html>
			`);
			printEL.document.close();

			
			printEL.focus();
			printEL.onload = () => {
				printEL.print(); 
				printEL.close(); 
			};
		} else {
			console.error('La finestra non può essere aperta');
		}
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
			
		</div>

		<ul>
			{#each $financesStore as expense, index}
				<li>
					{expense.description} - {expense.amount.toFixed(2)}€
					<button class="rimuovi" onclick={() => removeExpense(index)}>Rimuovi</button>
				</li>
			{/each}
		</ul>
		<button class="funz" onclick={scaricaCsv}>Estrai csv</button>
		<button class="funz" onclick={stampa}>stampa</button>
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
	.rimuovi {
		border-radius: 5px;
		margin-left: auto;
		padding: 3px 6px;
		background-color: #dc3545;
		color: white;
		border: none;
		cursor: pointer;
	}

	.rimuovi:hover {
		background-color: #c82333;
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
	.funz {
		margin-top: 10px;
		border-radius: 5px;
		padding: 5px 10px;
		font-size: 14px;
		background-color: rgb(255, 255, 255);
		color: blueviolet;
		border: none;
		cursor: pointer;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
	}

	.funz:hover {
		background-color: blueviolet;
		color:white

	}
	.funz:active {
		transform: translateY(2px);
	}
</style>
