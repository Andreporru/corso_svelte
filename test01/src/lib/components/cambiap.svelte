<script lang="ts">
	import { storeUser } from '$lib/stores/user.svelte';
	let password: string;
	let sw_01 = 0;
	let sw_err = 0;
	let sw_p = 0;
	let sw = 0;
	let p1: string;
	let p2: string;

	$: sw_p = p1 === '' || p2 === '' ? 0 : sw_p;
	$: sw_err = password === '' ? 0 : sw_err;

	const verifica = () => {
		sw_01 = 0;
		sw_err = 0;
		console.log(sw_01, sw_err);

		const savedpassword = localStorage.getItem(`password_${storeUser.id}`);
		if (savedpassword) {
			storeUser.password = savedpassword;
			console.log(storeUser.password);
		}
		if (savedpassword === password) {
			p1 = '';
			p2 = '';
			sw_01 = 1;

			console.log(sw_01, sw_err);
		} else {
			sw_err = 1;
			console.log(sw_01, sw_err);
		}
	};
	const onclick = () => {
		sw_p = 0;
		let c_s = 0;
		let c_m = 0;
		let c_n = 0;
		let length = 0;
		const stringa = p1;
		length = stringa.length;
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
		if (c_s === 0 || c_m === 0 || c_n === 0 || length < 8) {
			sw_p = 1;
		}
		if (p1 && p2 && p1 === p2 && sw_p === 0) {
			localStorage.setItem(`password_${storeUser.id}`, p1);
			sw = 1;
		}
	};
</script>

<br /><br />
{#if sw == 0}
	<div class="container">
		{#if sw_01 == 0}
			<label for="password">inserisci la vecchia password </label>
			<input type="password" name="password" id="password" bind:value={password} />
			<button onclick={verifica}>verifica</button>
		{:else}
			<label for="password">Nuova password</label>
			<input type="password" name="password" id="passwword" bind:value={p1} />
			<br /><br />
			<label for="password"> Conferma nuova password</label>
			<input
				type="password"
				name="password"
				id="password"
				style="box-shadow: {p1 && p2 && p1 !== p2 ? '0 0 15px red' : 'none'}"
				bind:value={p2}
			/>
			{#if p1 && p2 && p1 !== p2}
				<br /><br />
				<p class="errato">Password incongruenti</p>
			{/if}
			{#if sw_p === 1}
				<br />
				<br />

				<p class="errato">
					Password non valida (la password dev'essere minimo di 8 caratteri e contenere almeno un
					numero,un simbolo e una maiuscola)
				</p>
			{/if}

			<button {onclick}>Cambia password</button>
		{/if}
	</div>
	{#if sw_err !== 0}
		<br />
		<div class="wrongpass">
			<p class="errato">password errata</p>
		</div>
	{/if}
{:else}
	<div class="container">
		<p>password cambiata correttamente</p>
		<a href="/"> Torna alla home</a>
	</div>
{/if}

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

	button {
		margin-top: 20px;
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
	p.errato {
		color: red;
		font-size: 15px;
		margin-top: -10px;
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

	label {
		display: block;
		margin: 10px 0 5px;
		font-weight: bold;
	}

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
