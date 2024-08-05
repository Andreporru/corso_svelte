<script lang="ts">
	interface Props {
		value: string;
	}
	let { value = $bindable() }: Props = $props();

	/*const prov: string[] = ['no', 'vc', 'mi', 'xx'];*/
</script>

<div >
	<select class="prov" bind:value>
		<option value="no">no</option>
		<option value="mi">mi</option>
		<option value="sv">sv</option>
		<option value="sa">sa</option>
		<option	value="po">po</option>
		<option value="os">os</option>
		<option value="xx">xx</option>
	</select>
</div>
<style>
.prov{
	width: 100%;
	padding:10px;
	margin: 5px 0 20px;
	border: 1px solid #ccc;
	border-radius:5px;
	box-sizing: border-box;
}
</style>