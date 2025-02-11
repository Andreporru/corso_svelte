<script lang="ts">
    let ricerca = $state('');
    let mostra = $state(false);
    var quesiti: { [key: string]: string } = {
        "Importazione": "Nuova funzione che permette di importare articoli da un file CSV.",
        "Esportazione": "Nuova funzione che permette di esportare articoli in un file CSV.",
        "Aggiornamento": "Nuova funzione che permette di aggiornare gli articoli in magazzino.",
        "Eliminazione": "Nuova funzione che permette di eliminare articoli dal magazzino."
    };
    let parola = $state('');
    let mostraContenuto: { [key: string]: boolean } = {};

    Object.keys(quesiti).forEach((quesito) => {
        mostraContenuto[quesito] = false;
    });

    function toggleContenuto(quesito: string) {
        mostra = true;
        parola = quesito;
    }
    
    function toggleContenuto1() {
        mostra = false;
    }
</script>

<div class="container">
    <h1 class="titolo">Novità</h1>
    
    <div class="lista-container">
        {#if !mostra}
            {#each Object.keys(quesiti) as quesito}
                <button class="quesito-btn" onclick={() => toggleContenuto(quesito)}>
                    {quesito}
                </button>
            {/each}
        {:else}
            <div class="contenuto">
                <p>{quesiti[parola]}</p>
          
                <!-- svelte-ignore a11y_consider_explicit_label -->
                <button class="svg" onclick={toggleContenuto1}>
                    <svg width="45px" height="40px" viewBox="0 0 1024 1024" class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" fill="#247eca" stroke="#247eca">

                        <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                        
                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                        
                        <g id="SVGRepo_iconCarrier">
                        
                        <path d="M704 288h-281.6l177.6-202.88a32 32 0 0 0-48.32-42.24l-224 256a30.08 30.08 0 0 0-2.24 3.84 32 32 0 0 0-2.88 4.16v1.92a32 32 0 0 0 0 5.12A32 32 0 0 0 320 320a32 32 0 0 0 0 4.8 32 32 0 0 0 0 5.12v1.92a32 32 0 0 0 2.88 4.16 30.08 30.08 0 0 0 2.24 3.84l224 256a32 32 0 1 0 48.32-42.24L422.4 352H704a224 224 0 0 1 224 224v128a224 224 0 0 1-224 224H320a232 232 0 0 1-28.16-1.6 32 32 0 0 0-35.84 27.84 32 32 0 0 0 27.84 35.52A295.04 295.04 0 0 0 320 992h384a288 288 0 0 0 288-288v-128a288 288 0 0 0-288-288zM103.04 760a32 32 0 0 0-62.08 16A289.92 289.92 0 0 0 140.16 928a32 32 0 0 0 40-49.92 225.6 225.6 0 0 1-77.12-118.08zM64 672a32 32 0 0 0 22.72-9.28 37.12 37.12 0 0 0 6.72-10.56A32 32 0 0 0 96 640a33.6 33.6 0 0 0-9.28-22.72 32 32 0 0 0-10.56-6.72 32 32 0 0 0-34.88 6.72A32 32 0 0 0 32 640a32 32 0 0 0 2.56 12.16 37.12 37.12 0 0 0 6.72 10.56A32 32 0 0 0 64 672z" fill="#247eca"/>
                        
                        </g>
                        
                        </svg></button>
                    {#if parola != "Eliminazione" && parola != "Aggiornamento"}
                    
                    <!-- svelte-ignore a11y_consider_explicit_label -->
                    <button class="svg">
                        <a href="/articolo/export"><svg width="55px" height="55px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">
        
                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier"> <path d="M12 4L12 14M12 14L15 11M12 14L9 11" stroke="#217eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> <path d="M12 20C7.58172 20 4 16.4183 4 12M20 12C20 14.5264 18.8289 16.7792 17 18.2454" stroke="#217eca" stroke-width="1.5" stroke-linecap="round"/> </g>
                            
                            </svg></a></button>
                    {:else if parola == "Eliminazione"}
                    <!-- svelte-ignore a11y_consider_explicit_label -->
                    <button class="svg">
                        <a href="/articolo/add">
                        <svg width="40px" height="40px" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" stroke-width="3" stroke="#217eca" fill="none">

                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier">
                            
                            <line x1="8.06" y1="8.06" x2="55.41" y2="55.94"/>
                            
                            <line x1="55.94" y1="8.06" x2="8.59" y2="55.94"/>
                            
                            </g>
                            
                            </svg>
                    </button>
                    {:else if parola == "Aggiornamento"}
                    <!-- svelte-ignore a11y_consider_explicit_label -->
                    <button class="svg">
                        <a href="/articolo/search"><svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#247eca">

                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier"> <path d="M21.2799 6.40005L11.7399 15.94C10.7899 16.89 7.96987 17.33 7.33987 16.7C6.70987 16.07 7.13987 13.25 8.08987 12.3L17.6399 2.75002C17.8754 2.49308 18.1605 2.28654 18.4781 2.14284C18.7956 1.99914 19.139 1.92124 19.4875 1.9139C19.8359 1.90657 20.1823 1.96991 20.5056 2.10012C20.8289 2.23033 21.1225 2.42473 21.3686 2.67153C21.6147 2.91833 21.8083 3.21243 21.9376 3.53609C22.0669 3.85976 22.1294 4.20626 22.1211 4.55471C22.1128 4.90316 22.0339 5.24635 21.8894 5.5635C21.7448 5.88065 21.5375 6.16524 21.2799 6.40005V6.40005Z" stroke="#247eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> <path d="M11 4H6C4.93913 4 3.92178 4.42142 3.17163 5.17157C2.42149 5.92172 2 6.93913 2 8V18C2 19.0609 2.42149 20.0783 3.17163 20.8284C3.92178 21.5786 4.93913 22 6 22H17C19.21 22 20 20.2 20 18V13" stroke="#247eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> </g>
                            
                            </svg></a></button>
                    {/if}
            </div>
        {/if}
    </div>
</div>

<style>
    /* Contenitore principale */
    .container {
        text-align: center;
        margin-top: 50px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    a{
        text-decoration: none;
        color: white;
    }
    .svg {
        border: 0px;
        background-color: transparent;
    }
    .svg:hover {
        transform: scale(1.3);
        transition: transform 0.3s ease;
    }
    .svg:active {
        transform: translateY(2px);
    }

    /* Titolo */
    .titolo {
        font-size: 50px;
        color: rgb(33, 126, 202);
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-bottom: 30px;
    }

    /* Contenitore della lista */
    .lista-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }

    /* Pulsanti della lista */
    .quesito-btn {
        background: linear-gradient(to right, rgb(33, 126, 202), rgb(0, 109, 211));
        color: white;
        font-size: 18px;
        border: none;
        padding: 12px 25px;
        border-radius: 30px;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        width: 250px;
        text-transform: uppercase;
        font-weight: bold;
    }

    .quesito-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 15px rgba(0, 109, 211, 0.3);
    }

    .quesito-btn:active {
        transform: translateY(1px);
    }

    /* Contenuto selezionato */
    .contenuto {
        background: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        max-width: 500px;
        animation: fadeIn 0.3s ease-in-out;
    }

    .contenuto p {
        font-size: 18px;
        color: #333;
        margin-bottom: 15px;
    }

    /* Pulsante "Torna Indietro" */
  
    /* Animazione di comparsa */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
