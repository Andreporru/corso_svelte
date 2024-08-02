<script lang="ts">
	import NumericInput from '$lib/components/NumericInput.svelte';
	let value: number = $state(0);
	let value2: number = $state(123);
</script>

<NumericInput bind:value />
<p>Value:{value}</p>
<NumericInput value={value2}></NumericInput>
<p>Value:{value2}</p>
