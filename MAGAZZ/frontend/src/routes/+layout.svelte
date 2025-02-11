<script lang="ts">
	
import NavBar from '$lib/components/NavBar.svelte';
</script>

<NavBar />

<div class="container">
	<slot /> 
</div>

<style>
	.container {
		margin: 0;
		/* padding: 0; */
		/* display: flex; */
		flex-direction: column;
		align-items: center;

	}
</style>
