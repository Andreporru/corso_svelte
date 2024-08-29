<script lang="ts">
	import { goto } from '$app/navigation';
	import { ibanUser } from '$lib/stores/iban.svelte';

	import { storeUser } from '$lib/stores/user.svelte';
	import { redirect } from '@sveltejs/kit';

	let password: string;
	let id: number;
	let sw = 0;
	let sw_id = 0;
	$: sw_id = id === null ? 0 : sw_id;
	$: sw = password === '' || id===null ? 0 : sw;

	let firstpassword: string;
	const onclick = () => {
		sw = 0;
		sw_id = 0;

		const savedId = localStorage.getItem(`id_${id}`);

		const savedpassword = localStorage.getItem(`password_${id}`);
		if (!savedId) {
			sw_id = 1;
		} else {
			sw = 0;
			if (password === savedpassword) {
				const savedname = localStorage.getItem(`nome_${id}`);
				const savedmail = localStorage.getItem(`mail_${id}`);
				const savedAdress = localStorage.getItem(`indirizzo_${id}`);
				const savediban = localStorage.getItem(`iban_${id}`);
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

				storeUser.id = Number(savedId);
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
		transition: all 0.5s ease-in-out;
		background: linear-gradient(45deg, blueviolet, rgb(4, 161, 96));

		font-family: 'Comic Sans MS', cursive;
		color: white;
		padding: 15px 20px;
		border: none;
		border-radius: 5px;
		cursor: pointer;
		font-size: 16px;
		margin-top: 20px;
		display: block;
		width: 100%;
	}

	button:hover {
		background: linear-gradient(45deg, rgb(4, 161, 96), blueviolet);
		transform: translateY(-8px);
	}
	button:focus {
		outline: none;
		box-shadow: 0 0 0 3px rgba(21, 1, 29, 0.3);
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
