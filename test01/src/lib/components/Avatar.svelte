<script lang="ts">
	import { storeUser } from '$lib/stores/user.svelte';

	const login = () => {
		storeUser.id = 1;
		storeUser.name = 'Mario rossi';
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
		<button onclick={logout}></button>
	{:else}
		<button onclick={login}>Login</button>
	{/if}
</div>
