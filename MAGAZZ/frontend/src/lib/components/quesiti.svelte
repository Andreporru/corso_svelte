<script lang="ts">
    let ricerca = $state('');
    let mostra = $state(false);
    let parola = $state('');
    let risultati: string[] = $state([]);
    let quesito1 = $state('');
   
    

    let quesiti: { [key: string]: string } = {
        "Importazione": "/pdf/importazione.pdf",
        "Esportazione": "/pdf/esportazione.pdf",
        "Aggiornamento": "/pdf/aggiornamento.pdf",
        "Eliminazione": "/pdf/eliminazione.pdf",
        "Aggiunta": "/pdf/aggiunta.pdf",
        "Ricerca": "/pdf/ricerca.pdf",
        "Statistiche": "/pdf/statistiche.pdf",
        "Visualizzazione": "/pdf/visualizzazione.pdf",
        "Andamento": "/pdf/andamento.pdf",
        "Grafici": "/pdf/grafici.pdf",
        "Fatturazione": "/pdf/fatturazione.pdf",
    };
    let tuttiQuesiti = Object.keys(quesiti);

    
    risultati = [...tuttiQuesiti].sort(() => Math.random() - 0.5).slice(0, 5);

    function toggleContenuto(quesito: string) {
        mostra = true;
        parola = quesito;
        quesito1 = quesito;
       
    }

    function toggleContenuto1() {
        mostra = false;
        ricerca = ''; 
        risultati = [...tuttiQuesiti].sort(() => Math.random() - 0.5).slice(0, 5);
    }

    function aggiornaRisultati() {
        if (ricerca.trim() === '') {
            risultati = [...tuttiQuesiti].sort(() => Math.random() - 0.5).slice(0, 5);
        } else {
            risultati = Object.keys(quesiti).filter(quesito =>
                quesito.toLowerCase().includes(ricerca.toLowerCase())
            );
        }
    }

    function apriPDF(quesito: string) {
        let pdfPath = quesiti[quesito];
        if (pdfPath) {
            window.open(pdfPath, "_blank");
        } else {
            alert("⚠️ PDF non trovato per: " + quesito);
        }
    }
</script>

<div class="container">
    <h1 class="titolo">📜 Documentazione</h1>

    <input 
        type="text" 
        class="ricerca" 
        bind:value={ricerca} 
        placeholder="🔍 Cerca documento..."
        oninput={aggiornaRisultati}
    >

    <div class="lista-container">
        {#if !mostra}
            {#if risultati.length > 0}
                {#each risultati as quesito}
                    <button class="quesito-btn" onclick={() => toggleContenuto(quesito)}>
                        {quesito}
                    </button>
                {/each}
            {:else}
                <p class="nessun-risultato">⚠️ Nessun documento trovato.</p>
            {/if}
        {:else}
            <div class="contenuto">
                <!-- svelte-ignore a11y_missing_attribute -->
                <iframe src={`/pdf/${parola.toLowerCase()}.pdf`} width="100%" height="600px"></iframe>
          
                <!-- svelte-ignore a11y_consider_explicit_label -->
                <button class="svg" onclick={toggleContenuto1}>
                    <svg width="40px" height="40px" viewBox="0 0 17 17" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#217eca" transform="rotate(0)matrix(-1, 0, 0, 1, 0, 0)" stroke="#217eca">

                        <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                        
                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                        
                        <g id="SVGRepo_iconCarrier"> <path d="M14.583 15v1h-7.083c-3.032 0-5.5-2.467-5.5-5.5s2.468-5.5 5.5-5.5h2.912l-2.646-2.646 0.707-0.707 3.853 3.853-3.853 3.854-0.707-0.708 2.646-2.646h-2.912c-2.481 0-4.5 2.019-4.5 4.5s2.019 4.5 4.5 4.5h7.083z" fill="#217eca"/> </g>
                        
                        </svg>
                </button>
                <!-- svelte-ignore a11y_consider_explicit_label -->
                <button onclick={() => apriPDF(quesito1)} class ="svg"><svg fill="#217eca" width="40px" height="40px" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">

                    <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                    
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                    
                    <g id="SVGRepo_iconCarrier"> <g fill-rule="evenodd" transform="translate(42.667 42.667)"> <path d="M178.0832,42.6666667 L221.594,77.0716667 L191.217,107.448667 L163.24992,85.3333333 L42.6666667,85.3333333 L42.6666667,296.106667 L82.0209067,170.666667 L341.333333,170.666667 L341.333,170.665667 L384,170.665667 L437.333333,170.666667 L372.583253,384 L-2.13162821e-14,384 L-2.13162821e-14,42.6666667 L178.0832,42.6666667 Z M379.79136,213.333333 L113.354027,213.333333 L73.1874133,341.333333 L340.95808,341.333333 L379.79136,213.333333 Z"/> <path fill-rule="nonzero" d="M384,7.10542736e-15 L384,149.333333 L341.333333,149.333333 L341.332777,72.836 L264.836777,149.332777 L204.496777,149.333333 L311.162777,42.666 L234.666667,42.6666667 L234.666667,7.10542736e-15 L384,7.10542736e-15 Z"/> </g> </g>
                    
                    </svg></button>
            </div>
           
        {/if}
    </div>
</div>

<style>
.container {

    text-align: center;
    padding-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.titolo {
    font-size: 50px;
    color: rgb(33, 126, 202);
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    margin-bottom: 30px;
}

.ricerca {
    border: 2px solid #ddd;
    border-radius: 30px;
    padding: 10px;
    width: 250px;
    font-size: 16px;
    text-align: center;
    margin-bottom: 20px;
    border-color: rgb(33, 126, 202);
    outline: none;
}

.lista-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

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

.contenuto {
    background: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    animation: fadeIn 0.3s ease-in-out;
}

.nessun-risultato {
    font-size: 18px;
    color: gray;
    font-style: italic;
}
button{
    color:rgb(33, 126, 202);
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

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>