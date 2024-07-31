<script lang="ts">
	import Button from '$lib/components/Button.svelte';
	import Layout from '$lib/components/Layout.svelte';
	const onclick = () => {
		console.log('=== clicked');
		
	};
	const onfocus = () => {
		console.log('=== focused');
	};
	const onhover = (elem: HTMLElement) => {
		console.log('===hovered', elem);
		elem.style.backgroundColor = 'red';
	};
	let valore: boolean = $state(false);
	let valore2: boolean =$state(false);
	//    let dir:'column' | 'row' = $derived(vertical? 'column' : 'row');
</script>

<input type="checkbox" id="valore" name="valore" bind:checked={valore} />
<label for="valore"> verticale</label>
<input type="checkbox" id="nascondi" name="nascondi" bind:checked={valore2}>
<label for="nascondi">nascnondi</label> <br> 

<Layout direction={valore ? 'column' : 'row'} nascondi={valore2 ? 'hidden': 'visible'} {onhover} style="border:1px solid #ccc; padding: 8px">
	<!-- se ue valore è true da column se è false da row-->
	<Button label="Ciao mondo"  />
	<Button label="Ciao mondo" bgColor="blueviolet" />
	<Button label="Ciao mondo" bgColor="blueviolet" color="white" {onclick} {onfocus} />
</Layout>
