<script lang="ts">
	import { itemList, mediaMagazzo, valoreMagazzo } from "$lib/actions";
	import { articoliStore, media, valore } from "$lib/types2";
	import { onMount } from "svelte";

    onMount(async () => {
        const items = await itemList();
        const res = await valoreMagazzo();
        const res2 = await mediaMagazzo();
        articoliStore.set(items);
        valore.set(res.data);
        media.set(res2.data);
    });

  
</script>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestione Magazzino</title>

</head>
<body>
    <div class="home-container">
        <header class="header">
            <h1 class="main-title">Gestione Magazzino</h1>
            <p class="subtitle">Ottimizza il tuo magazzino in modo semplice ed efficace</p>
        </header>
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <section class="features">
            <!-- svelte-ignore a11y_click_events_have_key_events -->
            
            <div class="feature-card" >
                <div class="feature-icon">📦</div>
                <h2 class="feature-title">Gestione Articoli</h2>
                <p class="feature-desc">Aggiungi, modifica ed elimina articoli in pochi clic.</p>
            </div>
            
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h2 class="feature-title">Analisi Magazzino</h2>
                <p class="feature-desc">Visualizza valori e medie in tempo reale.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <h2 class="feature-title">Ricerca Articoli</h2>
                <p class="feature-desc">Trova rapidamente gli articoli di cui hai bisogno.</p>
            </div>
        </section>


        <div class="buttons">
            
        
            <button class="button" > <a href="/articolo/add">Gestione articoli</a></button>
            <button class="button" > <a href="/articolo/search">Ricerca articoli</a></button>
            <button class="button"> <a href="/articolo/stats">Statistiche</a> </button>
        </div>
    </div>
    <div class="footer">
        <p>© 2025 - Gestione Magazzino - Andrea porru</p>
    </div>


</body>

<style>
   .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 30px;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px ;
        
    }
 
    body {
        margin: 0;
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }
    a{
        text-decoration: none;
        color: white;
    }

    .home-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 20px;
    }

    .header {
        margin-bottom: 40px;
    }

    .main-title {
        font-size: 3rem;
        color: #217eca;
        animation: fadeInTitle 2s ease-in-out;
    }

    .subtitle {
        font-size: 1.2rem;
        color: #555;
    }

    /* Sezione Features */
    .features {
        display: flex;
        gap: 20px;
        justify-content: center;
        margin: 40px 0;
    }

    .feature-card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        width: 250px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }

    .feature-icon {
        font-size: 3rem;
        color: #217eca;
        margin-bottom: 15px;
    }

    .feature-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 10px;
        color: #333;
    }

    .feature-desc {
        font-size: 0.9rem;
        color: #666;
    }

    /* Pulsanti */
    .buttons {
        margin-top: 50px;
        display: flex;
        gap: 20px;
    }

    .button {
        background-color: #217eca;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }

    .button:hover {
        background-color: #1a5c99;
        transform: scale(1.05);
    }

    .button:active {
        transform: scale(1);
    }

    /* Animazioni */
    @keyframes fadeInTitle {
        0% {
            opacity: 0;
            transform: translateY(-20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInCards {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .feature-card {
        animation: fadeInCards 1s ease-in-out;
    }
</style>