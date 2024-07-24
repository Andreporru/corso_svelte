<script lang="ts">
	import { goto } from '$app/navigation';
	import Counter from '$lib/components/Counter.svelte';
	import NavBar from '$lib/components/NavBar.svelte';

	const onclick = () => {
		console.log('=== clicked');
		goto('/about');
	};
</script>

<Counter />
<h1>Welcome to SvelteKit!!</h1>
<p><a href="/about">About</a></p>
<p><button {onclick}>About</button></p>
