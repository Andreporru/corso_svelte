<script lang="ts">
	
	import { onMount, onDestroy } from 'svelte';
	import Avatar from './Avatar.svelte';
	import Ibatar from './Ibatar.svelte';

	let ora: number;
	let minuti: number;
	let secondi: number;
	let millisecondi: number;

	const updateTime = () => {
		const date = new Date();
		ora = date.getHours();
		minuti = date.getMinutes();
		secondi = date.getSeconds();
		millisecondi = Math.floor(date.getMilliseconds() / 10); 
	};
	let timer: any;

	onMount(() => {
		updateTime(); 
		timer = setInterval(updateTime, 10);
	});

	onDestroy(() => {
		clearInterval(timer); 
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
		<a href="/admin">area amministratore</a>
	</div>
	<div class="clock">{ora}:{minuti < 10 ? '0' : ''}{minuti}:{secondi < 10 ? '0' : ''}{secondi}<!---:{millisecondi < 10 ? '0' : ''}{millisecondi}--></div>
	<Avatar />
	<!-- <Ibatar /> -->
</div>

<style>
		@font-face{
		font-family:'digital-clock-font';
		src: 'C:\Users\stagecl5\Desktop\corso_svelte\digital-7.ttf';
		}
	.navbar {
		display: flex;
		flex-direction: row;
		background-color: blueviolet;
		color: white;
		justify-content: space-between;
		padding: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 1);
		font-size: 20px;
		position: relative;
	}

	.clock {	
		font-family:'digital-clock-font', monospacecd;				
		/* position: absolute;
		right: 600px; */
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