<script lang="ts">
	import SelProvincia from './SelProvincia.svelte';

	interface Props {
		value: string;
	}
	let { value = $bindable() }: Props = $props();
	const prov: Record<string, string> = {
		no: 'novara',
		mi: 'milano',
		vc: 'vercelli'
	};
	const provincia = $derived(prov[value] ?? 'provincia sconosciuta');
</script>

<input value="bin" />
