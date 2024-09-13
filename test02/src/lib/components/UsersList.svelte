<script lang="ts">
	import { StoreUsers } from '$lib/stores/user.svelte';
</script>

<div class="container">
	{#each StoreUsers.list() as user}
		<div class="user">
			<p>id: {user.id}</p>
			<p>name: {user.name}</p>
			<p>email: {user.email}</p>
		</div>
	{/each}
</div>

<style>
	.container {
		border: 1px solid #333;
		padding: 10xp;
		border-radius: 5px;
	}
	.user {
		display: flex;
		flex-direction: row;
		gap: 10px;
	}
</style>
