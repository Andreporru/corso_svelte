<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { createEventDispatcher } from 'svelte';
	import { writable } from 'svelte/store';

	const dispatch = createEventDispatcher();
	const theme = writable<'light' | 'dark'>('light');
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

	const chiaroScuro = () => {
		dispatch('toggleTheme');
	};

	function toggleTheme() {
		theme.update(current => {
			const newTheme = current === 'light' ? 'dark' : 'light';
			document.documentElement.setAttribute('data-theme', newTheme);
			localStorage.setItem('theme', newTheme);
			return newTheme;
		});
	}
</script>

<div class="navbar" data-theme={$theme}>
	<div class="links">
		<a class = "e" href="/" data-theme={$theme} >Home</a>

		<a  class="e"  href="/articolo/add" data-theme={$theme}>Aggiungi articolo</a>
		<a  class="e" href="/articolo/search" data-theme={$theme}>Cerca articolo</a>
		<a  class="e" href="/articolo/stats" data-theme={$theme}>Statistiche</a>
		<a  class="e" href="/articolo/export" data-theme={$theme}>Esporta/Importa</a>
		<a  class="e" href="/articolo/question" data-theme={$theme}>Quesiti</a>

	</div>
	<!-- <h1 class="titolo">GESTIONE MAGAZZINO</h1> -->
	<div class="clock">
		{ora}:{minuti < 10 ? '0' : ''}{minuti}:{secondi < 10
			? '0'
			: ''}{secondi}<!---:{millisecondi < 10 ? '0' : ''}{millisecondi}-->
	</div>

</div>

<style>
	@font-face {
		font-family: 'digital-clock-font';
		src: 'C:\Users\stagecl5\Desktop\corso_svelte\digital-7.ttf';
	}
	.navbar {
		display: flex;
		flex-direction: row;
		background-color: rgb(33,126,222);
		color: white;
		justify-content: space-between;
		padding: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 1);
		font-size: 20px;
		font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
		position: relative;
	}

	.clock {
		font-family: 'digital-clock-font', monospacecd;
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
