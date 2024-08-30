<script lang="ts">
	
	import { onMount, onDestroy } from 'svelte';
	import Avatar from './Avatar.svelte';
	import Ibatar from './Ibatar.svelte';

	let ora: number;
	let minuti: number;
	let secondi: number;
	let millisecondi: number; // Cambiato il nome da millesimi a millisecondi

	const updateTime = () => {
		const date = new Date();
		ora = date.getHours();
		minuti = date.getMinutes();
		secondi = date.getSeconds();
		millisecondi = Math.floor(date.getMilliseconds() / 10); // Converte millisecondi in decimi di secondo
	};

	let timer: number;

	onMount(() => {
		updateTime(); // Imposta subito l'orario iniziale
		timer = setInterval(updateTime, 10); // Aggiorna ogni 10 millisecondi
	});

	onDestroy(() => {
		clearInterval(timer); // Pulisce l'intervallo quando il componente viene distrutto
	});
</script>

<div class="navbar">
	<div class="links">
		<a href="/">Home</a>
		<a href="/about">About</a>
		<a href="/login">Login</a>
		<a href="/user-show">Dati</a>
		<a href="/iban-edit">Iban</a>
		<a href="/activities">Attività</a>
		<a href="/finances">Finanze</a>
		<a href="/calcula">Calcolatrice</a>
		<a href="/calendario">Calendario</a>
	</div>
	<div class="clock">{ora}:{minuti < 10 ? '0' : ''}{minuti}:{secondi < 10 ? '0' : ''}{secondi}:{millisecondi < 10 ? '0' : ''}{millisecondi}</div>
	<Avatar />
	<Ibatar />
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=DS+digital&dig=swap');
	.navbar {
		display: flex;
		flex-direction: row;
		background-color: blueviolet;
		color: white;
		justify-content: space-between;
		padding: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 1);
		font-size: 20px;
	}
	.clock {
		font-family:'Ds-digital', monospace;
	}

	a {
		color: white;
		text-decoration: none;
	}

	a:hover {
		transition: all 0.2s ease-in-out;
		font-size: larger;
	}

	.links {
		display: flex;
		flex-direction: row;
		gap: 10px;
	}
</style>