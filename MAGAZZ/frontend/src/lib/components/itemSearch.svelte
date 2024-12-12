<script lang="ts">
    import { derived } from 'svelte/store';
    import { articoliStore } from "$lib/types2";
    import type { Item } from "$lib/types";
    import { fade, fly } from 'svelte/transition';
    
    const items = derived(articoliStore, ($articoliStore) => $articoliStore as Item[]);
    let codice: string = $state('');
    let codice1: string = $state('');
    let codice_articolo: string = $state('');
    let descrizione_articolo: string = $state('');
    let prezzo: number = $state(0);
    let quantita: number = $state(0);  
    let sw: number = $state(0);
    
    const cerca = () => {
        if (codice === "") {
            sw = 3;
        } else {
            items.subscribe((items) => {
                const item = items.find((item) => item.codice_articolo === codice);
                if (item) {
                    sw = 1;
                    console.log(item);
                    codice1 = codice;
                    descrizione_articolo = item.descrizione_articolo;
                    prezzo = item.prezzo;
                    quantita = item.quantita;
                } else {
                    sw = 2;
                    console.log("Articolo non trovato");
                }
            });
        }
    };
    
    const controlla = () => {
        if (codice === "") {
            sw = 0;
        }
    };
    </script>
    
    <div class="container" in:fly={{ y: 20, duration: 450 }}>
        <h1 in:fly={{ y: -30, duration: 500 }} out:fly={{ y: 30, duration: 500 }}>
            Ricerca
        </h1>
        <div class="ricerca" in:fly={{ x: -50, duration: 400 }} out:fly={{ x: 50, duration: 400 }}>
            <input type="text" bind:value={codice} oninput={controlla} class:sw2={sw === 2||sw === 3} >
            <!-- svelte-ignore a11y_consider_explicit_label -->
            <button class="svg" onclick={cerca}>
                <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <path d="M11 6C13.7614 6 16 8.23858 16 11M16.6588 16.6549L21 21M19 11C19 15.4183 15.4183 19 11 19C6.58172 19 3 15.4183 3 11C3 6.58172 6.58172 3 11 3C15.4183 3 19 6.58172 19 11Z" stroke="#217eca" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                    </g>
                </svg>
            </button>
        </div>
        <br>
        <br>
        {#if sw === 1}
            <div class="table-container" in:fade={{ duration: 500 }} out:fade={{ duration: 500 }}>
                <table in:fly={{ y: -20, duration: 400 }} out:fly={{ y: 20, duration: 400 }}>
                    <thead>
                        <tr>
                            <th>Codice Articolo</th>
                            <th>Descrizione Articolo</th>
                            <th>Prezzo</th>
                            <th>Quantità</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{codice1}</td>
                            <td>{descrizione_articolo}</td>
                            <td>{prezzo}</td>
                            <td>{quantita}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        <!-- {:else if sw === 2}
            <div class="message error" in:fly={{ x: -50, duration: 300 }} out:fly={{ x: 50, duration: 300 }}>
                <p in:fade={{ duration: 300 }}>Articolo non trovato</p>
            </div>
        {:else if sw === 3}
            <div></div> -->
        {/if}
    </div>
    
    
    <style>
    h1 {
        color: rgb(33, 126, 202);
        font-size: 50px;
        padding-right: 35px;
        /* animation-name: example;
        animation-duration: 4s; */
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .ricerca {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
    }
    .svg {
        border: 0px;
        background-color: transparent;
    }
    .svg:hover {
        transform: translateY(-3px);
    }
    .svg:active {
        transform: translateY(2px);
    }
    .table-container {
        padding: 10px;
        margin-bottom: 20px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 10px;
    }
    th, td {
        padding: 6px;
        text-align: left;
        border: 1px solid #ddd;
    }
    th {
        background-color: rgb(33, 126, 202);
        color: white;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    tr:hover {
        background-color: #f1f1f1;
    }
    .sw2 {
    background-color: #f50c0098;
    border: 2px solid #ff0038;
    animation: shake 0.5s ease-in-out;
}

@keyframes shake {
    0% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    50% { transform: translateX(5px); }
    75% { transform: translateX(-5px); }
    100% { transform: translateX(0); }
}
    div.message p {
        margin: 0 0 1em;
        color: #85031f;
    }
    div.message.error {
        background: #FFD8D6 url(error20.png) no-repeat 15px 50%;
        border-color: #FF0038;
        animation: shake 0.5s ease-in-out;
    }
    /* @keyframes example {
        0% { transform: translateY(10px); }
        25% { transform: translateY(-10px); }
        50% { transform: translateY(10px); }
    } */
    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }
    input[type="text"] {
        width: 250px;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    
    input[type="text"]:focus {
        border-color: rgb(33, 126, 202);
        box-shadow: 0 0 5px rgba(33, 126, 202, 0.5);
        outline: none;
    }

    </style>
    