<script lang="ts">
	import { onMount } from 'svelte';
	import { storeUser } from '$lib/stores/user.svelte';
	import { writable } from 'svelte/store';
	import { fade, fly } from 'svelte/transition';

	export const userActivities = writable<{ nome: string; data: string; completata: boolean }[]>([]);

	interface Attivita {
		nome: string;
		data: string;
		completata: boolean;
	}

	let frase: string = '';
	let data: string = '';

	const loadAttivita = () => {
		const savedAttivita = localStorage.getItem(`activities_${storeUser.id}`);
		if (savedAttivita) {
			userActivities.set(JSON.parse(savedAttivita));
		} else {
			userActivities.set([]);
		}
	};

	const saveAttivita = (attivita: Attivita[]) => {
		localStorage.setItem(`activities_${storeUser.id}`, JSON.stringify(attivita));
	};

	const aggiungi = () => {
		if (frase.trim() !== '' && data !== '') {
			userActivities.update((current) => {
				const newAttivita = [...current, { nome: frase, data, completata: false }];
				saveAttivita(newAttivita);
				return newAttivita;
			});
			frase = '';
			data = '';
		}
	};

	const toggleCompletata = (index: number) => {
		userActivities.update((current) => {
			const updatedAttivita = current.map((attività, i) =>
				i === index ? { ...attività, completata: !attività.completata } : attività
			);
			saveAttivita(updatedAttivita);
			return updatedAttivita;
		});
	};

	const elimina = (index: number) => {
		userActivities.update((current) => {
			const updatedAttivita = current.filter((_, i) => i !== index);
			saveAttivita(updatedAttivita);
			return updatedAttivita;
		});
	};

	const convertiCsv = () => {
		const headers = 'attivita;data;completata\n';
		let rows = '';

		const activities = $userActivities;

		for (let i = 0; i < activities.length; i++) {
			const activity = activities[i];
			const row = `${activity.nome};${activity.data};${activity.completata ? 'SI' : 'NO'}\n`;
			rows += row;
		}

		return headers + rows;
	};

	const scaricaCsv = () => {
		const activities = $userActivities;
		const csvData = convertiCsv();
		const blob = new Blob([csvData], { type: 'text/csv' });
		const url = URL.createObjectURL(blob);
		const link = document.createElement('a');
		link.href = url;
		link.download = `${storeUser.name}_attivita(${activities.length}).csv`;
		link.click();
		console.log('fatto');
		URL.revokeObjectURL(url);
	};

	onMount(() => {
		loadAttivita();
	});
</script>

<br /><br />
<div class="container">
	{#if storeUser.id != ''}
		<label for="frase">Nuova attività</label>
		<input
			type="text"
			id="frase"
			name="frase"
			bind:value={frase}
			placeholder="Descrizione attività"
		/>
		<input type="date" id="data" name="data" bind:value={data} placeholder="Data attività" />

		<button class="agg" onclick={aggiungi}>Aggiungi</button>
		<button class="agg" onclick={scaricaCsv}>estrai csv</button>
		<br />
		<ul>
			{#each $userActivities as attività, index}
				{#if index == 0}
					<br />
				{/if}
				<li in:fly={{ y: 200, duration: 1000 }} out:fade>
					<input
						type="checkbox"
						checked={attività.completata}
						onchange={() => toggleCompletata(index)}
					/>
					<span class:completata={attività.completata}>
						{attività.nome} | {attività.data}
					</span>
					<button class="annulla" onclick={() => elimina(index)}>Elimina</button>
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
	h1 {
		color: blueviolet;
		font-size: 24px;
		margin-bottom: 20px;
		text-align: center;
	}

	.error::-moz-progress-bar {
		font-size: 18px;
	}
	.error {
		color: red;
		text-align: center;
	}
	.container {
		font-family: Arial, sans-serif;
		max-width: 400px;
		margin: 0 auto;
		background: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
		background-color: #f4f4f9;
	}

	label {
		color: blueviolet;
		font-size: 25px;
		display: block;
		margin-bottom: 5px;
		font-weight: bold;
	}

	input[type='text'],
	input[type='date'] {
		width: 100%;
		padding: 10px;
		margin: 5px 0 20px;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box;
	}

	.agg {
		border-radius: 5px;
		padding: 5px 10px;
		font-size: 14px;
		background-color: blueviolet;
		color: white;
		border: none;
		cursor: pointer;
	}

	.agg:hover {
		background-color: rgb(78, 0, 78);
	}
	.agg:active {
		transform: translateY(2px);
	}

	ul {
		list-style-type: none;
		padding: 0;
	}

	li {
		background-color: #f2f2f2;
		padding: 5px;
		margin-bottom: 5px;
		border-radius: 3px;
		display: flex;
		align-items: center;
	}
	li:hover {
		transition: all 0.3s ease-in-out;
		transform: translateY(-5px);
	}

	input[type='checkbox'] {
		margin-right: 10px;
	}

	.annulla {
		border-radius: 5px;
		margin-left: auto;
		padding: 3px 6px;
		background-color: #dc3545;
		color: white;
		border: none;
		cursor: pointer;
	}

	.annulla:hover {
		background-color: #c82333;
	}
</style>
