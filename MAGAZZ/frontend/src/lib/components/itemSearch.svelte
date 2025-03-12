<script lang="ts">
    import { derived } from 'svelte/store';
    import { articoliStore } from "$lib/types2";
    import type { Item } from "$lib/types";
    import { fade, fly } from 'svelte/transition';
    import { onDestroy, onMount } from 'svelte';
    import { itemList, itemModificaC } from '$lib/actions';

    const items = derived(articoliStore, ($articoliStore) => $articoliStore as Item[]);
    let codice: string = $state('');
    let codice1: string = $state('');
    let descrizione_articolo: string = $state('');
    let prezzo: number = $state(0);
    let quantita: number = $state(0);
    let sw: number = $state(0);
    let swm: number = $state(0);
    let ricercaPerDescrizione: boolean = $state(false); 
    let risultati: Item[] = $state([]); 
    let appoggio: string = $state('');

    let codiceSpecchio: string = $state('');
    let descrizioneArticoloSpecchio: string = '';
    let prezzoSpecchio: number = 0;
    let quantitaSpecchio: number = 0;

 
    const aggiornaRisultati = () => {
        if (codice.trim() === '') {
            risultati = []; 
            return;
        }
        items.subscribe((articoli) => {
            if (ricercaPerDescrizione) {
                risultati = articoli.filter(item =>
                    item.descrizione_articolo.toLowerCase().includes(codice.toLowerCase())
                );
            } else {
                risultati = articoli.filter(item =>
                    item.codice_articolo.toLowerCase().includes(codice.toLowerCase())
                );
            }
        });
    };

    const modificaLayout = (item: Item) => {
        swm = 1;
        codice1 = item.codice_articolo;
        descrizione_articolo = item.descrizione_articolo;
        prezzo = item.prezzo;
        quantita = item.quantita;

        codiceSpecchio = item.codice_articolo;
        descrizioneArticoloSpecchio = item.descrizione_articolo;
        prezzoSpecchio = item.prezzo;
        quantitaSpecchio = item.quantita;
    };

    const modifica = async (codice_articolo: string) => {
    // Verifica se i campi sono validi
    if (codice1.trim() === "" || descrizione_articolo.trim() === "" || prezzo <= 0 || quantita < 0) {
        alert("Inserire valori validi per tutti i campi.");
        return;
    }

    // Controllo se il nuovo codice articolo è già utilizzato da un altro articolo
    let codiceInUso = false;
    items.subscribe((articoli) => {
        for (const articolo of articoli) {
            if (articolo.codice_articolo === codice1 && articolo.codice_articolo !== codice_articolo) {
                codiceInUso = true;
                break;
            }
        }
    });

    if (codiceInUso) {
        alert("Codice articolo già in uso. Inserire un codice univoco.");
        return;
    }

    // Effettua la modifica
    const result = await itemModificaC(codice_articolo, codice1, descrizione_articolo, prezzo, quantita);

    if (result.success) {
        articoliStore.update((articoli) =>
            articoli.map((item) =>
                item.codice_articolo === codice_articolo
                    ? {
                        ...item,
                        codice_articolo: codice1,
                        descrizione_articolo: descrizione_articolo,
                        prezzo: prezzo,
                        quantita: quantita,
                    }
                    : item
            )
        );
         aggiornaRisultati(); //Aggiorna i risultati della ricerca
    } else {
        alert("Errore durante la modifica dell'articolo.");
    }

    swm = 0; // Esci dalla modalità modifica
};

    const annullaModifica = () => {
        swm = 0;
        codice1 = codiceSpecchio;
        descrizione_articolo = descrizioneArticoloSpecchio;
        prezzo = prezzoSpecchio;
        quantita = quantitaSpecchio;
    };

    onMount(async () => {
        const items = await itemList();
        articoliStore.set(items);
        aggiornaRisultati(); 
    });

    onDestroy(() => {
        codice = '';
        risultati = [];
    });
</script>

<div class="container" in:fly={{ y: 20, duration: 450 }}>
    <h1>Ricerca</h1>
    <div class="ricerca">
  
        <input
            type="text"
            class="lente"
            bind:value={codice}
            oninput={aggiornaRisultati}
            placeholder="Cerca articolo..."
        />


        <div class="radio-container">
            <label>
                <input type="radio" name="tipoRicerca" bind:group={ricercaPerDescrizione} value={false} />
                Cerca per codice
            </label>
            <label>
                <input type="radio" name="tipoRicerca" bind:group={ricercaPerDescrizione} value={true} />
                Cerca per descrizione
            </label>
        </div>
    </div>


    {#if risultati.length > 0}
        <div class="table-container" in:fade={{ duration: 500 }} out:fade={{ duration: 500 }}>
            <table>
                <thead>
                    <tr>
                        <th>Codice Articolo</th>
                        <th>Descrizione Articolo</th>
                        <th>Prezzo</th>
                        <th>Quantità</th>
                        <th>Modifica</th>
                    </tr>
                </thead>
                <tbody>
                    {#each risultati as item}
                        <tr>
                            {#if swm === 1 && codiceSpecchio === item.codice_articolo}
                                <td><input type="text" bind:value={codice1}></td>
                                <td><input type="text" bind:value={descrizione_articolo}></td>
                                <td><input type="number" bind:value={prezzo}></td>
                                <td><input type="number" bind:value={quantita}></td>
                                <td>
                                    <!-- svelte-ignore a11y_consider_explicit_label -->
                                    <button class="svg" onclick={() => modifica(item.codice_articolo)}><svg width="20px" height="20px" viewBox="0 0 1024 1024" class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" fill="#247eca" stroke="#247eca">

                                        <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                                        
                                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                                        
                                        <g id="SVGRepo_iconCarrier">
                                        
                                        <path d="M511.64164 924.327835c-228.816869 0-414.989937-186.16283-414.989937-414.989937S282.825796 94.347961 511.64164 94.347961c102.396724 0 200.763434 37.621642 276.975315 105.931176 9.47913 8.499272 10.266498 23.077351 1.755963 32.556481-8.488009 9.501656-23.054826 10.266498-32.556481 1.778489-67.723871-60.721519-155.148319-94.156494-246.174797-94.156494-203.396868 0-368.880285 165.482394-368.880285 368.880285S308.243749 878.218184 511.64164 878.218184c199.164126 0 361.089542-155.779033 368.60998-354.639065 0.49556-12.720751 11.032364-22.863359 23.910794-22.177356 12.720751 0.484298 22.649367 11.190043 22.15483 23.910794-8.465484 223.74966-190.609564 399.015278-414.675604 399.015278z" fill="#247eca247eca"/>
                                        
                                        <path d="M960.926616 327.538868l-65.210232-65.209209-350.956149 350.956149-244.56832-244.566273-65.210233 65.209209 309.745789 309.743741 0.032764-0.031741 0.03174 0.031741z" fill="#247eca"/>
                                        
                                        </g>
                                        
                                        </svg></button>
                                    <!-- svelte-ignore a11y_consider_explicit_label -->
                                    <button class="svg" onclick={annullaModifica}><svg width="20px" height="20px" viewBox="0 0 1024 1024" class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" fill="#247eca" stroke="#247eca">

                                        <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                                        
                                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                                        
                                        <g id="SVGRepo_iconCarrier">
                                        
                                        <path d="M704 288h-281.6l177.6-202.88a32 32 0 0 0-48.32-42.24l-224 256a30.08 30.08 0 0 0-2.24 3.84 32 32 0 0 0-2.88 4.16v1.92a32 32 0 0 0 0 5.12A32 32 0 0 0 320 320a32 32 0 0 0 0 4.8 32 32 0 0 0 0 5.12v1.92a32 32 0 0 0 2.88 4.16 30.08 30.08 0 0 0 2.24 3.84l224 256a32 32 0 1 0 48.32-42.24L422.4 352H704a224 224 0 0 1 224 224v128a224 224 0 0 1-224 224H320a232 232 0 0 1-28.16-1.6 32 32 0 0 0-35.84 27.84 32 32 0 0 0 27.84 35.52A295.04 295.04 0 0 0 320 992h384a288 288 0 0 0 288-288v-128a288 288 0 0 0-288-288zM103.04 760a32 32 0 0 0-62.08 16A289.92 289.92 0 0 0 140.16 928a32 32 0 0 0 40-49.92 225.6 225.6 0 0 1-77.12-118.08zM64 672a32 32 0 0 0 22.72-9.28 37.12 37.12 0 0 0 6.72-10.56A32 32 0 0 0 96 640a33.6 33.6 0 0 0-9.28-22.72 32 32 0 0 0-10.56-6.72 32 32 0 0 0-34.88 6.72A32 32 0 0 0 32 640a32 32 0 0 0 2.56 12.16 37.12 37.12 0 0 0 6.72 10.56A32 32 0 0 0 64 672z" fill="#247eca"/>
                                        
                                        </g>
                                        
                                        </svg></button>
                                </td>
                            {:else}
                                <td>{item.codice_articolo}</td>
                                <td>{item.descrizione_articolo}</td>
                                <td>{item.prezzo.toFixed(2)}€</td>
                                <td>{item.quantita}</td>
                                <td>
                                    <!-- svelte-ignore a11y_consider_explicit_label -->
                                    <button class="svg" onclick={() => modificaLayout(item)}><svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#247eca">

                                        <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                                        
                                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                                        
                                        <g id="SVGRepo_iconCarrier"> <path d="M21.2799 6.40005L11.7399 15.94C10.7899 16.89 7.96987 17.33 7.33987 16.7C6.70987 16.07 7.13987 13.25 8.08987 12.3L17.6399 2.75002C17.8754 2.49308 18.1605 2.28654 18.4781 2.14284C18.7956 1.99914 19.139 1.92124 19.4875 1.9139C19.8359 1.90657 20.1823 1.96991 20.5056 2.10012C20.8289 2.23033 21.1225 2.42473 21.3686 2.67153C21.6147 2.91833 21.8083 3.21243 21.9376 3.53609C22.0669 3.85976 22.1294 4.20626 22.1211 4.55471C22.1128 4.90316 22.0339 5.24635 21.8894 5.5635C21.7448 5.88065 21.5375 6.16524 21.2799 6.40005V6.40005Z" stroke="#247eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> <path d="M11 4H6C4.93913 4 3.92178 4.42142 3.17163 5.17157C2.42149 5.92172 2 6.93913 2 8V18C2 19.0609 2.42149 20.0783 3.17163 20.8284C3.92178 21.5786 4.93913 22 6 22H17C19.21 22 20 20.2 20 18V13" stroke="#247eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> </g>
                                        
                                        </svg></button>
                                </td>
                            {/if}
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    {/if}
</div>

<style>
    h1 {
        color: rgb(33, 126, 202);
        font-size: 50px;
        padding-right: 35px;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .ricerca {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
    }

    .radio-container {
        margin-top: 10px;
        display: flex;
        gap: 10px;
        align-items: center;
    }

    .table-container {
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 15px;
    }

    table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: white;
    }

    th, td {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
        font-size: 16px;
    }

    th {
        background-color: rgb(33, 126, 202);
        color: white;
        font-weight: bold;
    }

    tr:nth-child(even) {
        background-color: #f1f6fa;
    }

    tr:hover {
        background-color: #eef6ff;
    }

    .lente {
        width: 250px;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .lente:focus {
        border-color: rgb(33, 126, 202);
        box-shadow: 0 0 5px rgba(33, 126, 202, 0.5);
        outline: none;
    }

    input[type="text"],
    input[type="number"] {
        border-color: rgb(33, 126, 202);
        outline: none;
        border-radius: 5px;
    }
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
</style>
