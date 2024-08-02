<script lang="ts">
	interface Props {
		value: string;
	}
	let { value = $bindable() }: Props = $props();

	const prov: string[] = ['no', 'vc', 'mi', 'xx'];
</script>

<div>
	<select bind:value>
		<option value="no">no</option>
		<option value="mi">mi</option>
		<option value="xx">xx</option>
	</select>
</div>
