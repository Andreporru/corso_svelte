<script lang="ts">
	import Toolbar from '$lib/components/Toolbar.svelte';
	import { storeLoggedUser } from '$lib/stores/logUser.svelte';
	import { onMount } from 'svelte';

	interface Props {
		children: any;
	}
	let { children }: Props = $props();
	let isReady = $state(false);

	onMount(async () => {
		await storeLoggedUser.load();

		isReady = true;
	});
</script>

{#if isReady}
	<div class="layout">
		<Toolbar />
		{@render children()}
	</div>
{:else}
	<p>loading</p>
{/if}
