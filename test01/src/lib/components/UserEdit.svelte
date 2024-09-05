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
	let sw_cs = 0;
	let sw_cm = 0;
	let sw_cid = 0;

	let c_s = 0;
	let c_m = 0;
	let c_n = 0;
	let length = 0;
	$: sw_p = storeUser.password === '' || storeUser.password === null ? 0 : sw_p;
	$: sw_c = storeUser.name !== '' && storeUser.mail !== '' && storeUser.id !== null && storeUser.surname !== '' ? 0 : sw_c;
	$: sw_cn = storeUser.name !== '' ? 0 : sw_cn;
	$: sw_cs = storeUser.surname !== '' ? 0: sw_cs;
	$: sw_cm = storeUser.mail !== '' ? 0 : sw_cm;
	$: sw_cid = storeUser.id !== null ? 0 : sw_cid;
	$: sw_id = storeUser.id===null ? 0 : sw_id;

	const clean = () => {
		storeUser.name = '';
		storeUser.surname='';
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
		if (storeUser.name === '' || storeUser.mail === '' || storeUser.surname==='' || storeUser.id === null) {
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
		if(storeUser.surname===''){
			sw_cs = 1;
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
			const { id,name,surname,datan,luogon,  mail, password, indirizzo } = storeUser;
			localStorage.setItem(`nome_${storeUser.id}`, name);
			localStorage.setItem(`surname_${storeUser.id}`,surname);
			localStorage.setItem(`datan_${storeUser.id}`,datan);
			localStorage.setItem(`luogon_${storeUser.luogon}`, luogon);
			localStorage.setItem(`id_${storeUser.id}`, id);
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
		<br/>
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
	<label for="surname">Cognome*</label>
	<input
		type="text"
		id="surname"
		required
		name="user"
		style="box-shadow: {sw_cs==1 ? '0 0 15px red':'none'}"
		bind:value={storeUser.surname}
	/>

	<label for="mail">Mail*</label>
	<input
		type="mail"
		id="mail"
		name="mail"
		style="box-shadow: {sw_cm == 1 ? '0 0 15px red' : 'none'}"
		bind:value={storeUser.mail}
	/>
	<label for="luogon">Luogo di nascita</label>
	<input type = "text" id ="luogon" name="luogon" bind:value={storeUser.luogon}/>
	<label for="datan">Data di nascita</label>
	<input type = "date" id ="datan" name="datan" bind:value={storeUser.datan}/>
	<label for="indirizzo">Indirizzo</label>
	<input type="text" id="indirizzo" name="indirizzo" bind:value={storeUser.indirizzo}/>

	<label for="password">Password*</label>
	<input type="password" id="password" name="password" bind:value={storeUser.password} />

	<label for="confermaPassword">Conferma password</label>
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

<div class="footer">
    &copy; 2024 Gestionale Personale di Porru Andrea. Tutti i diritti riservati.
</div>
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

	button:hover {
		box-shadow:  0 0 10px rgba(55, 1, 92, 1);
		transition: all 300ms ease-in-out;
		transform:translateY(-8px);
		background-position: 0;
		color:white;
	}
	button:active{
		transform:translateY(2px);
	}
	.footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
		margin-top: 100px;
        /* position: fixed; */
        bottom: 0;
        width: 100%;
        margin-left:0;
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
	input[type='date'],
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
