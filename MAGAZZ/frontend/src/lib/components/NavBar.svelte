<script lang="ts">
	import { onMount, onDestroy } from 'svelte';


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

		<a href="/articolo/add">Aggiungi articolo</a>
		<a href="/articolo/search">Cerca articolo</a>
		<a href="/articolo/stats">Statistiche</a>
		<a href="/articolo/export">Esporta/Importa</a>
		<a href="/articolo/question">Quesiti</a>
	
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
		background-color: rgb(33, 126, 202);
		color: white;
		justify-content: space-between;
		padding: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 1);
		font-size: 20px;
		position: relative;
		height: 30px;
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
