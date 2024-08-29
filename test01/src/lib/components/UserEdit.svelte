<script lang="ts">
	import { goto } from '$app/navigation';
	import { storeUser } from '$lib/stores/user.svelte';
	import { onMount } from 'svelte';

	let password: string = '';
	let sw_id = 0;
	let idd: number;
	let sw_p = 0;
	let sw_c = 0;

	let sw_cn = 0;
	let sw_cm = 0;
	let sw_cid = 0;

	let c_s = 0;
	let c_m = 0;
	let c_n = 0;
	let length = 0;
	$: sw_p = storeUser.password === '' || storeUser.password === null ? 0 : sw_p;
	$: sw_c = storeUser.name !== '' && storeUser.mail !== '' && storeUser.id !== null ? 0 : sw_c;
	$: sw_cn = storeUser.name !== '' ? 0 : sw_cn;
	$: sw_cm = storeUser.mail !== '' ? 0 : sw_cm;
	$: sw_cid = storeUser.id !== null ? 0 : sw_cid;

	const clean = () => {
		storeUser.name = '';
		storeUser.password = '';
		storeUser.mail = '';
		storeUser.indirizzo = '';
		password = '';
	};

	const onclick = () => {
		c_s = 0;
		c_m = 0;
		c_n = 0;
		sw_id = 0;
		sw_p = 0;
		sw_c = 0;

		const stringa = storeUser.password;
		length = stringa.length;
		if (storeUser.name === '' || storeUser.mail === '' || storeUser.id === null) {
			console.log('campi non compilati');
			sw_c = 1;
			console.log(sw_c);
		}
		if (storeUser.name === '') {
			sw_cn = 1;
		}
		if (storeUser.mail === '') {
			sw_cm = 1;
		}
		if (storeUser.id === null) {
			sw_cid = 1;
		}

		const savedId = localStorage.getItem(`id_${storeUser.id}`);
		if (savedId) {
			console.log('ID già esistente');
			sw_id = 1;
		}

		for (let i = 0; i < length; i++) {
			const char = stringa[i];
			if ('#%£&€*$+-/.,;:!?'.includes(char)) {
				c_s += 1;
			} else if ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.includes(char)) {
				c_m += 1;
			} else if ('0123456789'.includes(char)) {
				c_n += 1;
			}
		}

		console.log(`Simboli: ${c_s}, Maiuscole: ${c_m}, Cifre: ${c_n}`);

		if (c_s === 0 || c_n === 0 || c_m === 0 || length < 8) {
			console.log('Password non valida');
			sw_p = 1;
		}

		if (sw_p === 0 && sw_id === 0 && sw_c === 0) {
			storeUser.isLogged = 'true';
			const { id, name, mail, password, indirizzo } = storeUser;
			localStorage.setItem(`nome_${storeUser.id}`, name);
			localStorage.setItem(`id_${storeUser.id}`, id.toString());
			localStorage.setItem(`mail_${storeUser.id}`, mail);
			localStorage.setItem(`password_${storeUser.id}`, password);
			localStorage.setItem(`indirizzo_${storeUser.indirizzo}`, indirizzo);
			goto('/');
		}
	};
	onMount(() => {
		clean();
	});
</script>

<br />

<div class="container">
	<h1>Registrati</h1>
	<label for="IDuser">ID*</label>
	<input
		type="number"
		id="IDuser"
		name="IDuser"
		style="box-shadow: {sw_cid == 1 ? '0 0 15px red' : 'none'}"
		bind:value={storeUser.id}
	/>
	{#if sw_id === 1}
		<br />
		<p>ID esistente</p>
	{/if}

	<label for="user">Nome*</label>
	<input
		type="text"
		id="user"
		required
		name="user"
		style="box-shadow: {sw_cn == 1 ? '0 0 15px red' : 'none'}"
		bind:value={storeUser.name}
	/>

	<label for="mail">Mail*</label>
	<input
		type="mail"
		id="mail"
		name="mail"
		style="box-shadow: {sw_cm == 1 ? '0 0 15px red' : 'none'}"
		bind:value={storeUser.mail}
	/>

	<label for="indirizzo">indirizzo</label>
	<input type="text" id="indirizzo" name="indirizzo" bind:value={storeUser.indirizzo}/>

	<label for="password">password</label>
	<input type="password" id="password" name="password" bind:value={storeUser.password} />

	<label for="confermaPassword">conferma password</label>
	<input
		type="password"
		id="confermaPassword"
		name="confermaPassword"
		style="box-shadow: {storeUser.password && password && storeUser.password !== password
			? '0 0 15px red'
			: 'none'}"
		bind:value={password}
	/>


	{#if storeUser.password && password && storeUser.password !== password}
	<br><br>
		<p>Le passwod non corrispondono</p>
	{/if}

	{#if sw_p === 1}
		<br />
		<br />

		<p>
			Password non valida (la password dev'essere minimo di 8 caratteri e contenere almeno un
			numero,un simbolo e una maiuscola)
		</p>
	{/if}

	<br />

	<button {onclick}>registrati</button>
</div>
<br />
{#if sw_c == 1}
	<div class="campi">
		<p class="errato">Campi obbligatori vuoti</p>
	</div>
{/if}

<!-- <pre>
{JSON.stringify(storeUser, null, 2)}
</pre> -->

<style>
	p {
		color: red;
		font-size: 13px;
		margin-top: -10px;
	}
	.campi {
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

	button {
		transition: all 0.5s ease-in-out;
		background: linear-gradient(45deg, blueviolet, rgb(4, 161, 96));
		color: white;
		padding: 15px 20px;
		border: none;
		border-radius: 5px;
		cursor: pointer;
		font-size: 18px;
		margin-top: 20px;
		display: block;
		width: 100%;
	}

	button:hover {
		transition: all 0.5s ease-in-out;
		background: linear-gradient(45deg, rgb(4, 161, 96), blueviolet);
		transform: translateY(-5px);
	}
	button:focus {
		outline: none;
		box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.1);
	}
	.container {
	
		font-family: Arial, sans-serif;
		max-width: 400px;
		margin: 0 auto;
		background: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
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
	input[type='mail'],
	input[type='password'] {
		height: 30px;
		width: 100%;
		padding: 5px;
		margin: 5px 0 5px;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box;
	}
</style>
