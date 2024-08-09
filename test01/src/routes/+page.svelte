<script lang="ts">
	import { goto } from '$app/navigation';
	import Counter from '$lib/components/Counter.svelte';
	import NavBar from '$lib/components/NavBar.svelte';

	const onclick = () => {
		console.log('=== clicked');
		goto('/about');
	};
</script>
<div class="main">

<div class="header">
    Gestionale Personale
</div>

<div class="container">
    <div class="section">
        <h2>Benvenuto nel tuo gestionale personale</h2>
        <p>Gestisci le tue attività, controlla le tue finanze e tieni traccia dei tuoi progressi in un unico posto.</p>
    </div>

    <div class="section">
        <h2>Sezioni principali</h2>
        <div class="cards">
            <div class="card">
                <h3>Attività</h3>
                <p>Gestisci le tue attività giornaliere e pianifica il tuo lavoro.</p>
                <a href="/activities">Vai alle attività</a>
            </div>
            <div class="card">
                <h3>login</h3>  
                <p>Effettu il login per avere dati e opzioni personalizzate!</p>
                <a href="/user-edit">Vai al login</a>
            </div>
            <div class="card">
                <h3>calcolatrice</h3>
                <p>I tuoi calcoli  sempre a portatra di mano.</p>
                <a href="/calcula">Vai alla calcolatrice</a>
            </div>
            <div class="card">
                <h3>iban</h3>
                <p>componi il tuoi iban per averlo sempre con te</p>
                <a href="/iban-edit">Vai al tuo iban</a>
            </div>
        </div>
    </div>
</div>

<div class="footer">
    &copy; 2024 Gestionale Personale. Tutti i diritti riservati.
</div>
</div>

    
<style>
  
    .header {
       /* background-color: blueviolet;
        background:linear-gradient(45deg,rgb(135, 78, 158),blueviolet   );*/
        color: blueviolet;
        font-size: 30px;
        padding: 20px;
        text-align: center;
       
    }
    .container {
        max-width: 1200px;
        margin: 20px auto;
        padding: 20px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .section {
        margin-bottom: 20px;
    }
    .section h2 {
        font-size: 22px;
        color: blueviolet;
        margin-bottom: 10px;
    }
    .section p {
        margin-bottom: 10px;
    }
    .cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
    }
    .card {
        background-color: #f9f9fc;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    .card a {
        text-decoration: none;
        color: blueviolet;
        font-weight: bold;
    }
    .footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
</style>