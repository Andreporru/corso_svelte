<script lang="ts">
	import { storeUser } from '$lib/stores/user.svelte';
	import { goto } from '$app/navigation';
	import { ibanUser } from '$lib/stores/iban.svelte';

	const login = () => {
		goto('/login');
	};

	const logout = () => {
		storeUser.id = '';
		storeUser.name = '';
		storeUser.surname='';
		storeUser.datan='';
		storeUser.luogon='';
		storeUser.mail = '';
		ibanUser.iban = '';
		storeUser.isLogged = 'false';
	};

	const vai = () => {
		goto('/'); 
	};
</script>

<div class="container">
	{#if storeUser.isLogged == 'true'}
		<p>Benvenuto {storeUser.name}!</p>
		<button class="auth-button" on:click={logout}>Logout</button>
	{:else}
		<button class="auth-button" on:click={login}>Login</button>
	{/if}
	<button class="auth-button" on:click={vai}>Vai alla Home</button>
</div>

<style>
	.container {
		display: flex;
		align-items: center;
		gap: 10px;
	}

	.auth-button {
		background-color: white;
		color: blueviolet;
		border: 2px solid blueviolet;
		padding: 5px 10px;
		border-radius: 5px;
	
		cursor: pointer;
		transition:
			background-color 0.3s,
			color 0.3s;
	}

	.auth-button:hover {
		background-color: blueviolet;
		color: white;
	}
</style>
