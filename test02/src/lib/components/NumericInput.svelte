<script lang="ts">
	interface Props {
		value: number;
	}
	let { value = $bindable() }: Props = $props();
	const onkeydown = (event: KeyboardEvent) => {
		console.log('===KEY', event);
		switch (event.key) {
			case 'Arrowup':
				value++;
				break;
			case 'Arrowup':
				value++;
				break;
			case 'Backspace':
			case 'Delete':
			case 'Tab':
		}
		if (event.key < '0' || event.key > '9') {
			event.preventDefault();
		}
	};
</script>

<input type="number" bind:value {onkeydown} />
