<script lang="ts">
	import { goto } from '$app/navigation';
	import { ibanUser } from '$lib/stores/iban.svelte';
	import { storeUser } from '$lib/stores/user.svelte';
	import { userLogs } from '$lib/stores/logs.svelte';

	const percorso = './dati.txt';

	let sw: number = $state(0);
	const onclick = () => {
		sw = 1;
	};
	const ondblclick = () => {
		sw = 0;
		const { name, surname, datan, luogon, mail, password, indirizzo } = storeUser;
		const iban = ibanUser.iban;
		localStorage.setItem(`nome_${storeUser.id}`, name);
		localStorage.setItem(`cognome_${storeUser.id}`, surname);
		localStorage.setItem(`datan_${storeUser.id}`, datan);
		localStorage.setItem(`luogon_${storeUser.id}`, luogon);
		localStorage.setItem(`mail_${storeUser.id}`, mail);

		localStorage.setItem(`indirizzo_${storeUser.id}`, indirizzo);
		localStorage.setItem(`iban_${storeUser.id}`, iban);

		const savedName = localStorage.getItem(`nome_${storeUser.id}`);
		const savedMail = localStorage.getItem(`mail_${storeUser.id}`);
		const savedSurname = localStorage.getItem(`cognome_${storeUser.id}`);
		const savedDatan = localStorage.getItem(`datan_${storeUser.id}`);
		const savedLuogon = localStorage.getItem(`luogon_${storeUser.id}`);
		const savedIndirizzo = localStorage.getItem(`indirizzo_${storeUser.id}`);
		const savedIban = localStorage.getItem(`iban_${storeUser.id}`);

		if (savedName) {
			storeUser.name = savedName;
		}
		if (savedSurname) {
			storeUser.surname = savedSurname;
		}
		if (savedDatan) {
			storeUser.datan = savedDatan;
		}
		if(savedLuogon){
			storeUser.luogon=savedLuogon
		}
		if (savedIndirizzo) {
			storeUser.indirizzo = savedIndirizzo;
		}
		if (savedIban) {
			ibanUser.iban = savedIban;
		}
	};
	const cambiap = () => {
		goto('/cambia-password');
	};
	const convertiCsv = () => {
		const headers = 'ID;NOME;COGNOME;LUOGO_NASCITA;DATA_NASCITA;EMAIL;INDIRIZZO;IBAN\n';
		const row = `${storeUser.id};${storeUser.name};${storeUser.surname};${storeUser.luogon};${storeUser.datan};${storeUser.mail};${storeUser.indirizzo};${ibanUser.iban}\n`;
		return headers + row;
	};
	const scaricaCsv = () => {
		const csvData = convertiCsv();
		const blob = new Blob([csvData], { type: 'text/csv' });
		const url = URL.createObjectURL(blob);
		const link = document.createElement('a');
		link.href = url;
		link.download = `${storeUser.name}_dati.csv`;
		link.click();
		console.log('fatto');
		URL.revokeObjectURL(url);
	};
	const stampa = () => {
		const printEL = window.open('', '_blank');
		if (printEL) {
			printEL.document.open();
			printEL.document.write(`
			<html>
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
				<title>stampa_dati_${storeUser.name}_${storeUser.surname}</title>
				<body>
					<h1>Informazioni  di ${storeUser.name} ${storeUser.surname}</h1>
					<div>
						<table>
							<tr><td>ID</td><td>Nome</td><td>Cognome</td><td>Data nascita</td><td>Luogo nascita</td><td>Email</td></tr>
							<tr><td>${storeUser.id}</td><td>${storeUser.name}</td><td>${storeUser.surname}</td><td>${storeUser.datan}</td><td>${storeUser.luogon}</td><td>${storeUser.mail}</td></tr>
						</table>
					</div>
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
			console.error('la finestra non può essere aperta');
		}
	};
	const stampalog = () => {
		const printEL = window.open('', '_blank');
		if (printEL) {
			const activities = $userLogs;
			let activitiesHtml = '';

			activities.forEach((attività: {  nlog: string; data: string  }) => {
				activitiesHtml += `
					<tr>
						<td>${attività.nlog}</td>
						<td>${attività.data}</td>
					</tr>
				`;
			});

			printEL.document.open();
			printEL.document.write(`
				<html>
					<head>
						<title>stampa_logs_${storeUser.name}_${storeUser.surname}</title>
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
						<h1>Logs di ${storeUser.name} ${storeUser.surname}</h1>
						<table>
							<thead>
								<tr>
									<th>N° logs</th>
									<th>Data</th>
									
								</tr>
							</thead>
							<tbody>
								${activitiesHtml}
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
</script>

<br /><br />
<div class="container">
	{#if storeUser.id != ''}
		<h1>Dati Utente</h1>
		{#if sw == 0}
			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>id: {storeUser.id}</p>
			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>nome: {storeUser.name}</p>
			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>cognome: {storeUser.surname}</p>
			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>data nascita: {storeUser.datan}</p>
			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>luogo nascita: {storeUser.luogon}</p>

			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>mail: {storeUser.mail}</p>

			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>indirizzo: {storeUser.indirizzo}</p>

			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>iban: {ibanUser.iban}</p>
			<p class="dato">data creazione account: {storeUser.firstLogin}</p>
			<p class="dato">ultimo accesso: {storeUser.lastLogin}</p>

			<br />
			<button onclick={cambiap}>cambia password</button>
			<button class="funz" onclick={scaricaCsv}>estrai file csv</button>
			<button class="funz" onclick={stampa}>stampa</button>
			<button class="funz" onclick={stampalog}>stampa log</button>
		{:else}
			<label for="id">inserisci id</label>
			<input {ondblclick} type="number" id="id" name="id" bind:value={storeUser.id} />
			<label for="nome">inserisci nome</label>
			<input {ondblclick} type="text" id="nome" name="nome" bind:value={storeUser.name} />
			<label for="surname">inserisci cognome</label>
			<input {ondblclick} type="text" id="surname" name="surname" bind:value={storeUser.surname} />
			<label for="luogon">Luogo di nascita</label>
			<input {ondblclick} type="text" id="luogon" name="luogon" bind:value={storeUser.luogon} />
			<label for="datan">Data di nascita</label>
			<input {ondblclick} type="date" id="datan" name="datan" bind:value={storeUser.datan} />
			<label for="email">inserisci email</label>
			<input {ondblclick} type="mail" id="email" name="email" bind:value={storeUser.mail} />
			<label for="indirizzo">indirizzo</label>
			<input
				{ondblclick}
				type="text"
				id="indirizzo"
				name="idirizzo"
				bind:value={storeUser.indirizzo}
			/>
			<label for="iban">inserisci iban</label>
			<input {ondblclick} type="text" id="iban" name="iban" bind:value={ibanUser.iban} />
			<br />
			<button onclick={cambiap}>cambia password</button>
			<button onclick={scaricaCsv}>scrivi file txt</button>
			<button onclick={stampa}>stampa</button>
			<button class="funz" onclick={stampalog}>stampa log</button>
		{/if}
	{:else}
		<h1 class="error">ERRORE</h1>
		<p class="error">
			Non è possibile visualizzare e/o inserire i dati perché l'utente non ha effettuato il login
		</p>
	{/if}
</div>
<div class="footer">
	&copy; 2024 Gestionale Personale di Porru Andrea. Tutti i diritti riservati.
</div>

<style>
	.error::-moz-progress-bar {
		font-size: 18px;
	}
	.error {
		color: red;
		text-align: center;
	}
	button {
		border-radius: 5px;
		padding: 5px 10px;
		font-size: 14px;
		background-color: blueviolet;
		color: white;
		border: none;
		cursor: pointer;
	}

	button:hover {
		background-color: rgb(78, 0, 78);
	}
	button:active {
		transform: translateY(2px);
	}
	.funz {
		border-radius: 5px;
		padding: 5px 10px;
		font-size: 14px;
		background-color: white;
		color: blueviolet;
		border: none;
		cursor: pointer;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
	}

	.funz:hover {
		background-color: blueviolet;
		color: white;
	}
	.funz:active {
		transform: translateY(2px);
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

	h1 {
		color: blueviolet;
		font-size: 24px;
		margin-bottom: 20px;
		text-align: center;
	}

	label {
		display: block;
		margin: 10px 0 5px;
		font-weight: bold;
	}

	input[type='text'],
	input[type='number'],
	input[type='date'],
	input[type='mail'] {
		width: 100%;
		padding: 10px;
		margin: 5px 0 20px;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box;
	}
	p {
		display: block;
		margin: 10px 0 5px;
	}
	.dato {
		display: block;
		margin: 10px 0 5px;
		font-weight: bold;
	}
	.dato:hover {
		transition: all 0.3s ease-in-out;
		transform: translateY(-4px);
	}
	.footer {
		background-color: #333;
		color: white;
		text-align: center;
		padding: 10px;
		margin-top: 480px;
		/* position: fixed; */
		bottom: 0;
		width: 100%;
		margin-left: 0;
	}
</style>
