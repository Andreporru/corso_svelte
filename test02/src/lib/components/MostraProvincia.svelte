<script lang="ts">
	import SelProvincia from './SelProvincia.svelte';

	interface Props {
		value: string;
	}
	let { value = $bindable() }: Props = $props();
	const prov: Record<string, string> = {
		no: 'novara',
		mi: 'milano',
		vc: 'vercelli',
		sv: 'savona',
		po: 'prato',
		os: 'oristano',
		sa:'salerno'
	};
	const provincia = $derived(prov[value] ?? 'provincia sconosciuta');

</script>
<div >
	<p>{provincia}</p>
</div>
<style>
	p{
		text-align: center;
		font-size:20px;
		text-shadow: blueviolet;
	}
</style>
