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


<div class="main">
    <div class="home-container">
        <header class="header">
            <h1 class="main-title">Gestione Magazzino</h1>
            <p class="subtitle">Ottimizza il tuo magazzino in modo semplice ed efficace</p>
        </header>
        <section class="features">
            <div class="feature-card">
                <div class="card-inner">
                    <div class="card-front">
                        <div class="feature-icon">📦</div>
                        <h2 class="feature-title">Gestione Articoli</h2>
                    </div>
                    <div class="card-back">
                        <p class="feature-desc">Aggiungi, modifica ed elimina articoli in pochi clic.</p>
                        <!-- svelte-ignore a11y_consider_explicit_label -->
                        <button class="svg"><a href="/articolo/add"><svg fill="#217eca" height="40px" width="40px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 297.391 297.391" xml:space="preserve" stroke="#217eca">

                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier"> <g> <path d="M134.342,260.156c-3.231-13.083-4.897-26.503-4.964-39.979l-0.208-41.787c-0.016-3.273-1.102-6.452-3.093-9.05 l-30.405-39.673c-4.913-6.411-14.067-8.15-20.701-3.544c-7.083,4.919-8.551,14.692-3.367,21.457l18.207,23.756 c2.974,3.88,4.134,8.852,3.186,13.647v0c-0.856,4.329-6.099,6.078-9.383,3.132L48.962,157.03 c-6.971-6.254-10.731-15.331-10.226-24.683l3.656-67.643c0.447-8.272-5.897-15.341-14.169-15.788 c-8.275-0.444-15.34,5.897-15.788,14.169L7.06,162.54c-0.179,3.331,0.756,6.626,2.659,9.366l49.991,71.979 c6.412,9.232,11.08,19.559,13.774,30.471l2.852,11.549c1.666,6.745,7.718,11.485,14.666,11.485h32.896 c3.503,0,6.969-1.068,9.712-3.247c4.737-3.765,6.698-9.828,5.302-15.48L134.342,260.156z"/> <path d="M163.049,260.156c3.231-13.083,4.897-26.503,4.964-39.979l0.208-41.787c0.016-3.273,1.102-6.452,3.094-9.05l30.405-39.673 c4.913-6.411,14.067-8.15,20.702-3.544c7.083,4.919,8.551,14.692,3.367,21.457l-18.207,23.756 c-2.974,3.88-4.134,8.852-3.185,13.647v0c0.856,4.329,6.099,6.078,9.383,3.132l34.649-31.087 c6.971-6.254,10.731-15.331,10.226-24.683l-3.656-67.643c-0.447-8.272,5.897-15.341,14.169-15.788 c8.275-0.444,15.34,5.897,15.788,14.169l5.375,99.455c0.179,3.331-0.756,6.626-2.659,9.366l-49.991,71.979 c-6.412,9.232-11.08,19.559-13.775,30.471l-2.852,11.549c-1.666,6.745-7.718,11.485-14.666,11.485h-32.896 c-3.503,0-6.969-1.068-9.712-3.247c-4.737-3.765-6.698-9.828-5.302-15.48L163.049,260.156z"/> <path d="M175.862,109.255l28.202-59.636c3.541-7.489,0.341-16.432-7.147-19.974L137.281,1.444 c-7.49-3.542-16.432-0.342-19.974,7.147L89.105,68.227c-3.541,7.489-0.341,16.432,7.148,19.974l59.636,28.202 c2.072,0.98,4.254,1.443,6.403,1.443C167.911,117.846,173.299,114.672,175.862,109.255z"/> </g> </g>
                            
                            </svg></a></button>
                    </div>
                </div>
            </div>
            <div class="feature-card">
                <div class="card-inner">
                    <div class="card-front">
                        <div class="feature-icon">📊</div>
                        <h2 class="feature-title">Analisi Magazzino</h2>
                    </div>
                    <div class="card-back">
                        <p class="feature-desc">Visualizza valori e medie in tempo reale.</p>
                        <!-- svelte-ignore a11y_consider_explicit_label -->
                        <button class="svg"><a href="/articolo/stats"><svg fill="#217eca" width="40px" height="40px" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">

                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier"> <path d="M0 14h16v2H0v-2zm8.5-8l4-4H11V0h5v5h-2V3.5L9.5 8l-1 1-2-2-5 5L0 10.5 6.5 4 8 5.5l.5.5z" fill-rule="evenodd"/> </g>
                            
                            </svg></a></button>
                    </div>
                </div>
            </div>
            <div class="feature-card">
                <div class="card-inner">
                    <div class="card-front">
                        <div class="feature-icon">🔍</div>
                        <h2 class="feature-title">Ricerca Articoli</h2>
                    </div>
                    <div class="card-back">
                        <p class="feature-desc">Trova rapidamente gli articoli di cui hai bisogno.</p>
                        <!-- svelte-ignore a11y_consider_explicit_label -->
                        <button class="svg"><a href="/articolo/search"><svg width="45px" height="45px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">

                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier"> <path d="M11 6C13.7614 6 16 8.23858 16 11M16.6588 16.6549L21 21M19 11C19 15.4183 15.4183 19 11 19C6.58172 19 3 15.4183 3 11C3 6.58172 6.58172 3 11 3C15.4183 3 19 6.58172 19 11Z" stroke="#217eca" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> </g>
                            
                            </svg></a></button>
                    </div>
                </div>
            </div>
        </section>
    </div>
   
</div>

<style>
    .svg{
        border: 0px;
        background-color: transparent;
    } 
     .svg:hover{
        transform: scale(1.3);
        transition: transform 0.3s ease;
    }
    .svg:active{
        transform: translateY(2px);
    }

     .home-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 20px;
    }
    .main {
        margin: 0;
        font-family: 'Arial', sans-serif;
        background-color: white;
        color: #333;
    }
    a{
        text-decoration: none;
        color: white;
    }
    .features {
        display: flex;
        gap: 100px;
        justify-content: center;
        margin: 40px 0;
    }
    .feature-card {
        perspective: 1000px;
        width: 250px;
        height: 180px;
    }
 
    .card-inner {
        width: 100%;
        height: 100%;
        position: relative;
        transform-style: preserve-3d;
        transition: transform 0.6s;
    }
    
    .feature-card:hover .card-inner {
        transform: rotateY(180deg);
    }
    
    .card-front, .card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        border-radius: 10px;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        background-color: #ffffff;
    }
    
    .card-back {
        transform: rotateY(180deg);
        background-color: #ffffff;
        color: rgb(0, 0, 0);
    }
    
    .feature-icon {
        font-size: 3rem;
        color: #217eca;
        margin-bottom: 15px;
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
    }
    
    .feature-desc {
        font-size: 1rem;
        text-align: center;
    }
    
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
</style>
