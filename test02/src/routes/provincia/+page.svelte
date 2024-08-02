<script lang="ts">
	import MostraProvincia from '$lib/components/MostraProvincia.svelte';
	import SelProvincia from '$lib/components/SelProvincia.svelte';
	let value: string = $state('');
</script>

<SelProvincia bind:value />
<MostraProvincia bind:value />
