<script lang="ts">
	import { goto } from '$app/navigation';
	import { ibanUser } from '$lib/stores/iban.svelte';
	import { storeUser } from '$lib/stores/user.svelte';
	let sw: number = $state(0);
	const onclick = () => {
		sw = 1;
	};
	const ondblclick = () => {
		sw = 0;
		const {  name, mail, password, indirizzo } = storeUser;	
		const iban=ibanUser.iban;
		localStorage.setItem(`nome_${storeUser.id}`, name);
	
		localStorage.setItem(`mail_${storeUser.id}`, mail);
	
		localStorage.setItem(`indirizzo_${storeUser.id}`, indirizzo);
		localStorage.setItem(`iban_${storeUser.id}`,iban);

		const savedName=localStorage.getItem(`nome_${storeUser.id}`);
		const savedMail=localStorage.getItem(`mail_${storeUser.id}`);
		const savedIndirizzo=localStorage.getItem(`indirizzo_${storeUser.id}`);
		const savedIban=localStorage.getItem(`iban_${storeUser.id}`);

		if(savedName)
		{
			storeUser.name=savedName;
		}
		if(savedMail)
		{
			storeUser.mail=savedMail;
		}
		if(savedIndirizzo)
		{
			storeUser.indirizzo=savedIndirizzo;
		}
		if(savedIban)
		{
			ibanUser.iban=savedIban;
		}
	
	
	};
	const cambiap = () =>{
		goto('/cambia-password');
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
			<p class="dato" {onclick}>mail: {storeUser.mail}</p>

			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>indirizzo: {storeUser.indirizzo}</p>

			<!-- svelte-ignore a11y_click_events_have_key_events -->
			<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
			<p class="dato" {onclick}>iban: {ibanUser.iban}</p>
			<br>
			<button onclick={cambiap}>cambia password</button>
		{:else}
			<label for="id">inserisci id</label>
			<input {ondblclick} type="number" id="id" name="id" bind:value={storeUser.id} />
			<label for="nome">inserisci nome</label>
			<input {ondblclick} type="text" id="nome" name="nome" bind:value={storeUser.name} />
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
			<br>
			<button onclick={cambiap}>cambia password</button>
		{/if}
	{:else}	
		<h1 class="error">ERRORE</h1>
		<p class="error">
			Non è possibile visualizzare e/o inserire i dati perché l'utente non ha effettuato il login
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
		/*	font-weight: bold;*/
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
</style>
