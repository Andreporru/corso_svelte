<script lang="ts">
	import { counters } from '../stores/counter.svelte';

	let double: number = $derived(counters.count * 2);
	const onclick = () => {
		counters.count = parseInt(counters.count.toString()) + 1;
	};
</script>

<button {onclick}>{counters.count}</button>
val:{double}

<input type="number" bind:value={counters.count} />

<style>
	button {
		padding: 0 2rem;
	}
</style>
