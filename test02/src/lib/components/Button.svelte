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

<button class ="btn primary"style:background-color={bgColor} style:color {onclick}{...rest}>ciao mondo</button>

<style>
	button {
		background-color: red;

	}
	.btn {
    padding: 12px 25px;
    font-size: 18px;
    font-family: 'Arial', sans-serif;
    border: 1px solid transparent;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    outline: none;
}

/* Primary button styling */
.btn.primary {
    background: linear-gradient(45deg, #6a11cb, #2575fc);
    color: white;
    border: 1px solid #6a11cb;
}

/* Hover effect for the primary button */
.btn.primary:hover {
    background: linear-gradient(45deg, #fcdb24, #6a11cb);
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Active effect for the primary button */
.btn.primary:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Focus effect for accessibility */
.btn.primary:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(138, 43, 226, 0.3);
}
</style>
