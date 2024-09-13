<script lang="ts">
	import { goto } from '$app/navigation';
	import { storeLoggedUser } from '$lib/stores/logUser.svelte';
	const doLogin = () => {
		goto('/login');
	};
	const doLogout = async () => {
		await storeLoggedUser.logout();
		goto('/');
	};
</script>

<div class="toolbar">
	<p>{storeLoggedUser.user.name}</p>
	{#if storeLoggedUser.user.id}
		<button onclick={doLogout}>logout</button>
	{:else}
		<button onclick={doLogin}>login</button>
	{/if}
</div>

<style>
	.toolbar {
		display: flex;
		justify-content: space-between;
		background-color: #333;
		color: white;
	}
	p {
		color: white;
	}
</style>
