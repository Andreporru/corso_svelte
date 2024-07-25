<script lang="ts">
	import { storeUser } from '$lib/stores/user.svelte';

	const login = () => {
		storeUser.id = 1;
		storeUser.name = 'Mario rosso';
		storeUser.mail = '';
	};
	const logout = () => {
		storeUser.id = 0;
		storeUser.name = '';
		storeUser.mail = '';
	};
</script>

<div class="container">
	{#if storeUser.id > 0}
		benvenuto {storeUser.name}!
		<button class="auth-button" onclick={logout}></button>
	{:else}
		<button class="auth-button" onclick={login}>Login</button>
	{/if}
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
		border: 2px solid white;
		padding: 5px 10px;
		border-radius: 5px;
		font-family: 'Comic Sans MS', cursive;
		cursor: pointer;
		transition: background-color 0.3s, color 0.3s;
	}

	.auth-button:hover {
		background-color: blueviolet;
		color: white;
		border: 2px solid white;
	}
</style>