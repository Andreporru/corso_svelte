<script lang="ts">
	import { goto } from '$app/navigation';
	import Counter from '$lib/components/Counter.svelte';
	import NavBar from '$lib/components/NavBar.svelte';

	const onclick = () => {
		console.log('=== clicked');
		goto('/about');
	};
</script>

<div class="container" >
<h1>Benvenuto nel tuo gestionale personale!!!</h1>

<p><a href="/about">About</a></p>
<br><br>	

</div>
<style>
    .container {
        font-family: Arial, sans-serif;
        max-width: 400px;
        margin: 0 auto;
  
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
 
    }
</style>