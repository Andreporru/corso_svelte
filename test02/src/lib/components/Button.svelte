<script lang="ts">
	import Page from '../../routes/+page.svelte';

	interface Props {
		label: string;
		bgColor?: string;
		color?: string;
		// events
		onclick?: () => void;
		// ...rest
		[key: string]: any;
		

	}
	
	let { label, bgColor, color, onclick, ...rest }: Props = $props();

</script>

<button style:background-color={bgColor} style:color {onclick}{...rest}>ciao mondo</button>

<style>
	button {
		background-color: red;
	}
</style>
