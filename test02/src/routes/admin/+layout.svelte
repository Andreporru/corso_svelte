<script lang="ts">
	import { goto } from '$app/navigation';
	import { storeLoggedUser } from '$lib/stores/logUser.svelte';
	import { StoreUsers } from '$lib/stores/user.svelte';
	import { onMount } from 'svelte';

	interface Props {
		children: any;
	}
	let { children }: Props = $props();
	let isReady: boolean = $state(false);
	onMount(async () => {
		if (storeLoggedUser.user.id != '1') goto('/login');
		await StoreUsers.load();
		isReady = true;
	});
</script>

{#if isReady}
	{@render children()}
{/if}
