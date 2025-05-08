<script lang="ts">
	import { onMount, onDestroy } from "svelte";
	import { writable } from "svelte/store";

	let ora: number;
	let minuti: number;
	let secondi: number;
	let timer: any;

	
	const updateTime = () => {
		const date = new Date();
		ora = date.getHours();
		minuti = date.getMinutes();
		secondi = date.getSeconds();
	};

	
	onMount(() => {
		updateTime();
		timer = setInterval(updateTime, 1000);

	
		
	});
 
	onDestroy(() => {
		clearInterval(timer);
	});


</script>


<div class="navbar">
	<div class="links">
		<a href="/" class="active">Home</a>
		<a href="/articolo/add" class="active">Aggiungi articolo</a>
		<a href="/articolo/search" class="active">Cerca articolo</a>
		<a href="/articolo/stats" class="active">Statistiche</a>
		<a href="/articolo/export" class="active">Esporta/Importa</a>
		<a href="/articolo/question" class="active">Documentazione</a>
	</div>

	
	<div class="clock">
		{ora}:{minuti < 10 ? "0" : ""}{minuti}:{secondi < 10 ? "0" : ""}{secondi}
	</div>
</div>


<style>
	@font-face {
		font-family: "digital-clock-font";
		src: url("/digital-7.ttf");
	}

	.navbar {
		border-radius: 10px;
		height: 30px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		background-color: rgb(33, 126, 222);
		color: white;
		padding: 15px 25px;
		box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
		font-size: 20px;
		font-family: "Trebuchet MS", sans-serif;
		position: relative;
		transition: all 0.3s ease-out;
	}

	.navbar:hover {
		background-color: rgb(26, 99, 164);
		box-shadow: 0 0 25px rgba(0, 0, 0, 0.7);
	}

	.links {
		display: flex;
		gap: 25px;
	}

	.links a {
		color: white;
		text-decoration: none;
		position: relative;
		padding-bottom: 8px;
		transition: color 0.3s, transform 0.3s ease-in-out;
	}

	/* Effetto di hover sui link */
	.links a:hover {
		color: #ffcc00; /* Colore dorato per l'hover */
		transform: translateY(-4px); /* Leggera animazione per spostare il link */
	}

	/* Rimuoviamo l'effetto dorato per il link attivo */
	.active {
		color: white; /* Nessun colore dorato per il link attivo */
		font-weight: normal; /* Non rendiamo il link più in evidenza */
	}

	.clock {
		font-family: "digital-clock-font", monospace;
		font-size: 22px;
		color: #ffcc00;
	}
</style>
