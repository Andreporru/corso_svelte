<script lang="ts">
	import MostraProvincia from '$lib/components/MostraProvincia.svelte';
	import SelProvincia from '$lib/components/SelProvincia.svelte';
	let value: string = $state('');
</script>

<div class="container" style="margin-top:100px" >
	<h1>PROVINCE</h1>
<SelProvincia bind:value />
<MostraProvincia bind:value />
</div>
<style>
	div.container{
		margin-top: 100px;
		font-family: Arial, sans-serif;
		max-width: 400px;
		margin: 0 auto;
		background: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
		background-color: #f4f4f9;
	}
	h1 {
		color:blueviolet;
		font-size:24px;
		margin-bottom: 20px;
		text-align: center;
	}

	
</style>