<script lang="ts">
	import { goto } from '$app/navigation';
	import { ibanUser } from '$lib/stores/iban.svelte';

	import { storeUser } from '$lib/stores/user.svelte';
	import { redirect } from '@sveltejs/kit';
	import { writable } from 'svelte/store';
	import { userLogs } from '$lib/stores/logs.svelte';


	interface Log {
		nlog: string;
		data: string;
	}

	let nlog: string = '';
	let data: string = '';


	const loadLogs = () => {
	const savedLogs = localStorage.getItem(`logs_${storeUser.id}`);
	if (savedLogs) {
		userLogs.set(JSON.parse(savedLogs));
	} else {
		userLogs.set([]);
	}
};

const saveLogs = (logs: Log[]) => {
	localStorage.setItem(`logs_${id}`, JSON.stringify(logs));
};


	
	const aggiungiLog = () => {
	if (nlog.trim() !== '' && data !== '') {
		userLogs.update((current) => {
			
			const savedLogs = localStorage.getItem(`logs_${id}`);
			let previousLogs: Log[] = [];

			if (savedLogs) {
				previousLogs = JSON.parse(savedLogs);
			}

			// Aggiungi il nuovo log alla lista dei log esistenti
			const newLog = [...previousLogs, { nlog, data }];

			// Salva i log aggiornati nel localStorage
			saveLogs(newLog);

			// Aggiorna lo store con i log aggiornati
			return newLog;
		});

		// Resetta le variabili per l'inserimento del nuovo log
		nlog = '';  
		data = '';  
	}
};


	let password: string;
	let id: number;
	let sw = 0;
	let sw_id = 0;
	$: sw_id = id === null ? 0 : sw_id;
	$: sw = password === '' || id===null ? 0 : sw;

	let firstpassword: string;
	const onclick = () => {
		loadLogs();
		sw = 0;
		sw_id = 0;

		const savedId = localStorage.getItem(`id_${id}`);


		const savedpassword = localStorage.getItem(`password_${id}`);
		if (!savedId) {
			sw_id = 1;
		} else {
			sw = 0;
			if (password === savedpassword) {
				



				let giorno,mese,anno,ora,minuti;
				const date = new Date();
				mese = date.getMonth();
				anno = date.getFullYear();
				ora = date.getHours();
				minuti=date.getMinutes();
				giorno = date.getDate();
				storeUser.lastLogin=`${giorno.toString()}/${mese.toString()}/${anno.toString()}-${ora.toString()}:${minuti.toString()}`;
				const nlog1 = localStorage.getItem(`nlog_${id}`)
				const savedname = localStorage.getItem(`nome_${id}`);
				const savedmail = localStorage.getItem(`mail_${id}`);
				const savedAdress = localStorage.getItem(`indirizzo_${id}`);
				const savedSurname=localStorage.getItem(`cognome_${id}`);
				const savedDatan=localStorage.getItem(`datan_${id}`);
				const savedLuogon=localStorage.getItem(`luogon_${id}`);
				const savediban = localStorage.getItem(`iban_${id}`);
				const savedDc=localStorage.getItem(`firstLogin_${id}`);

				
				
				storeUser.isLogged = 'true';
				if (savedname) {
					storeUser.name = savedname;
				}
				if (savedmail) {
					storeUser.mail = savedmail;
				}
				if (savedAdress) {
					storeUser.indirizzo = savedAdress;
				}
				if (savediban) {
					ibanUser.iban = savediban;
				}
				if(savedSurname){
					storeUser.surname=savedSurname;
				}
				if(savedDatan){
					storeUser.datan=savedDatan;
				}
				if(savedLuogon){
					storeUser.luogon=savedLuogon;
				}
				if(nlog1){
					let calcola=Number(nlog1)+1
					localStorage.setItem(`nlog_${id}`,calcola.toString());
					nlog=calcola.toString();
					data=storeUser.lastLogin;
					aggiungiLog();

				}else{
					localStorage.setItem(`nlog_${id}`,'1')
					nlog='1';
					data=storeUser.lastLogin;
					aggiungiLog();
				}
				
				const nlog2=localStorage.getItem(`nlog_${id}`);
				if(nlog2)
				{
					storeUser.nlog=nlog2;
				}
				const lastLogin=storeUser.lastLogin;
				
				localStorage.setItem(`lastLogin_${id}`,lastLogin);
				storeUser.id=savedId;
				loadLogs();
			} else {
				sw = 3;
			}
		}
	};
</script>

<br /><br />
{#if sw === 3}
	<div class="wrongpass">
		<p class="errato">Password o id errati</p>
	</div>
{/if}
<br />
<div class="container">
	{#if storeUser.isLogged == 'false'}
		<h1>Login</h1>
		<label for="IDuser">ID</label>
		<input type="number" id="IDuser" name="IDuser" bind:value={id} />
		{#if sw_id === 1}
			<p class="errato">id inesistente</p>
		{/if}

		<label for="password">password</label>
		<input type="password" id="password" name="password" bind:value={password} />

		<br />

		<button {onclick}>login</button>
	{:else if storeUser.isLogged == 'true'}
		<p>login effettuato con successo</p>
	{/if}
</div>
<br />

{#if storeUser.isLogged == 'false'}
	<div class="container">
		<p>Nuovo in Gestionale personale?</p>
		<a href="/user-edit"> Registrati</a>
	</div>
{/if}
<div class="footer">
    &copy; 2024 Gestionale Personale di Porru Andrea. Tutti i diritti riservati.
</div>
<!-- <pre>
{JSON.stringify(storeUser, null, 2)}
</pre> -->

<style>
	p {
		color: blueviolet;
		font-size: 15px;
		margin-top: -10px;
	}
	a {
		color: blueviolet;
		font-size: 15px;
		margin-top: -10px;
	}
	a:hover {
		transition: all 0.3s ease-in-out;
		font-size: larger;
	}
	p.errato {
		color: red;
		font-size: 15px;
		margin-top: -10px;
	}

	button {
		padding: 15px 20px;
		margin-top: 20px;
		display: block;
		width: 100%;
		border-radius: 5px;
		background-color: white;
		border-color: blueviolet;
		border:none;
		color:blueviolet;
		font-size: 1.25rem;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
		background-image: linear-gradient(45deg, blueviolet 50%, transparent 50%);
		background-position: 100%;
		background-size: 400%;
		transition: background 500ms ease-in-out;	
	}
	.footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
		margin-top: 100px;
        position: fixed;
        bottom: 0;
        width: 100%;
        margin-left:0;
    }

	button:hover {
		box-shadow:  0 0 10px rgba(55, 1, 92, 1);
		transition: all 300ms ease-in-out;
		transform:translateY(-8px);
		background-position: 0;
		color:white;
	}
	button:active{
		transform:translatey(2px);
	}

	
	
	.container {
		font-family: Arial, sans-serif;
		max-width: 400px;
		margin: 0 auto;
		background: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.7);
		background-color: #f4f4f9;
	}
	.wrongpass {
		font-family: Arial, sans-serif;
		text-align: center;
		max-width: 400px;
		font-size: 20;
		margin: 0 auto;
		background: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(255, 2, 2, 0.3);
		background-color: #ec13133d;
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

	input[type='number'],
	input[type='password'] {
		width: 100%;
		padding: 10px;
		margin: 5px 0 20px;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box;
	}
</style>
