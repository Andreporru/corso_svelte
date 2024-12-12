<script lang="ts"> 
    import { articoliStore, media, valore } from "$lib/types2";
    import type { Item } from "$lib/types";
    import { itemDelete, itemModifica, mediaMagazzo, valoreMagazzo } from "$lib/actions";
	import { tweened } from "svelte/motion";
	import { fade } from "svelte/transition";

    let items: Item[] = [];
    let editing: Record<string, boolean> = {};
    let newQuantities: Record<string, number> = {};
    const valoreAnimato = tweened(0, { duration: 500, easing: t => t * (2 - t) });
    const mediaAnimato = tweened(0, { duration: 500, easing: t => t * (2 - t) });

    $: items = $articoliStore;

    $: {
        valore.subscribe((newValue) => {
            valoreAnimato.set(newValue); 
        });
    }

    $: {
        media.subscribe((newValue) => {
            mediaAnimato.set(newValue); 
        });
    }

    const modificaQuantita = async (codice_articolo: string) => {
        const nuovaQuantita = newQuantities[codice_articolo];
        if (nuovaQuantita === undefined || nuovaQuantita < 0 || isNaN(nuovaQuantita)) {
            console.error("Quantità non valida!");
            return;
        }

        const result = await itemModifica(codice_articolo, nuovaQuantita);

        if (result.success) { 
            articoliStore.update((articoli) =>
                articoli.map((item) =>
                    item.codice_articolo === codice_articolo
                        ? { ...item, quantita: nuovaQuantita }
                        : item
                )
            );

            const res = await valoreMagazzo();
            if (res.success) {
                valore.set(res.data); 
            } else {
                console.error("Errore nell'aggiornamento del valore:", res.error);
            }

            const res2 = await mediaMagazzo();
            console.log("mediaaaa:", res2);
            if (res2.success) { // Usa `res2` qui
                media.set(res2.data); // Aggiorna la media correttamente
            } else {
                console.error("Errore nell'aggiornamento della media:", res2.error);
            }
        } else {
            console.error("Errore nella modifica della quantità:", result.error);
        }

        editing[codice_articolo] = false;
    };

    const eliminaArticolo = async (codice_articolo: string) => {
        const result = await itemDelete(codice_articolo);

        if (result.success) {
            articoliStore.update((currentItems) => 
                currentItems.filter((item) => item.codice_articolo !== codice_articolo)
            );

            const res = await valoreMagazzo();
            if (res.success) {
                valore.set(res.data); 
            } else {
                console.error("Errore nell'aggiornamento del valore:", res.error);
            }

            const res2 = await mediaMagazzo();
            if (res2.success) {
                media.set(res2.data); 
                console.log("media aggiornata:", $media);
            } else {
                console.error("Errore nell'aggiornamento della media:", res2.error);
            }
        } else {
            console.error("Errore nell'eliminazione dell'articolo:", result.error);
        }
    };

    const toggleEdit = (codice_articolo: string, currentQuantita: number) => {
        editing[codice_articolo] = !editing[codice_articolo];
        if (!newQuantities[codice_articolo]) {
            newQuantities[codice_articolo] = currentQuantita;
        }
    };
</script>

<!-- HTML e Stile invariati -->


<br>
<br>

<div class="table-container" >
    <h1>Lista articoli</h1>
    <table>
        <thead>
            <tr>
                <th>CODICE ARTICOLO</th>
                <th>DESCRIZIONE</th>
                <th>PREZZO</th>
                <th>QUANTITA'</th>
                <th>MODIFICA</th>
                <th>ELIMINA</th>
            </tr>
        </thead>
        <tbody>
            {#each items as item}
            <tr>
                <td>{item.codice_articolo}</td>
                <td>{item.descrizione_articolo}</td>
                <td>{item.prezzo.toFixed(2)}€</td>
                <td>
                    {#if editing[item.codice_articolo]}
                        <input 
                            type="number" 
                            bind:value={newQuantities[item.codice_articolo]} 
                            min="0" 
                        />
                    {:else}
                        {item.quantita}
                    {/if}
                </td>
                <td>
                    {#if editing[item.codice_articolo]}
                        <!-- svelte-ignore a11y_consider_explicit_label -->
                        <button class="modifica"onclick={() => modificaQuantita(item.codice_articolo)}><svg width="20px" height="20px" viewBox="0 0 1024 1024" class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" fill="#247eca" stroke="#247eca">

                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier">
                            
                            <path d="M511.64164 924.327835c-228.816869 0-414.989937-186.16283-414.989937-414.989937S282.825796 94.347961 511.64164 94.347961c102.396724 0 200.763434 37.621642 276.975315 105.931176 9.47913 8.499272 10.266498 23.077351 1.755963 32.556481-8.488009 9.501656-23.054826 10.266498-32.556481 1.778489-67.723871-60.721519-155.148319-94.156494-246.174797-94.156494-203.396868 0-368.880285 165.482394-368.880285 368.880285S308.243749 878.218184 511.64164 878.218184c199.164126 0 361.089542-155.779033 368.60998-354.639065 0.49556-12.720751 11.032364-22.863359 23.910794-22.177356 12.720751 0.484298 22.649367 11.190043 22.15483 23.910794-8.465484 223.74966-190.609564 399.015278-414.675604 399.015278z" fill="#247eca247eca"/>
                            
                            <path d="M960.926616 327.538868l-65.210232-65.209209-350.956149 350.956149-244.56832-244.566273-65.210233 65.209209 309.745789 309.743741 0.032764-0.031741 0.03174 0.031741z" fill="#247eca"/>
                            
                            </g>
                            
                            </svg></button>
                        <!-- svelte-ignore a11y_consider_explicit_label -->
                        <button class="modifica" onclick={() => toggleEdit(item.codice_articolo, item.quantita)}><svg width="20px" height="20px" viewBox="0 0 1024 1024" class="icon" version="1.1" xmlns="http://www.w3.org/2000/svg" fill="#247eca" stroke="#247eca">

                            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                            
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                            
                            <g id="SVGRepo_iconCarrier">
                            
                            <path d="M704 288h-281.6l177.6-202.88a32 32 0 0 0-48.32-42.24l-224 256a30.08 30.08 0 0 0-2.24 3.84 32 32 0 0 0-2.88 4.16v1.92a32 32 0 0 0 0 5.12A32 32 0 0 0 320 320a32 32 0 0 0 0 4.8 32 32 0 0 0 0 5.12v1.92a32 32 0 0 0 2.88 4.16 30.08 30.08 0 0 0 2.24 3.84l224 256a32 32 0 1 0 48.32-42.24L422.4 352H704a224 224 0 0 1 224 224v128a224 224 0 0 1-224 224H320a232 232 0 0 1-28.16-1.6 32 32 0 0 0-35.84 27.84 32 32 0 0 0 27.84 35.52A295.04 295.04 0 0 0 320 992h384a288 288 0 0 0 288-288v-128a288 288 0 0 0-288-288zM103.04 760a32 32 0 0 0-62.08 16A289.92 289.92 0 0 0 140.16 928a32 32 0 0 0 40-49.92 225.6 225.6 0 0 1-77.12-118.08zM64 672a32 32 0 0 0 22.72-9.28 37.12 37.12 0 0 0 6.72-10.56A32 32 0 0 0 96 640a33.6 33.6 0 0 0-9.28-22.72 32 32 0 0 0-10.56-6.72 32 32 0 0 0-34.88 6.72A32 32 0 0 0 32 640a32 32 0 0 0 2.56 12.16 37.12 37.12 0 0 0 6.72 10.56A32 32 0 0 0 64 672z" fill="#247eca"/>
                            
                            </g>
                            
                            </svg></button>
                    {:else}
                        <!-- svelte-ignore a11y_consider_explicit_label -->
                        <button  class="modifica" onclick={() => toggleEdit(item.codice_articolo, item.quantita)}>
                            <svg width="25px" height="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#247eca">

                                <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                                
                                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                                
                                <g id="SVGRepo_iconCarrier"> <path d="M21.2799 6.40005L11.7399 15.94C10.7899 16.89 7.96987 17.33 7.33987 16.7C6.70987 16.07 7.13987 13.25 8.08987 12.3L17.6399 2.75002C17.8754 2.49308 18.1605 2.28654 18.4781 2.14284C18.7956 1.99914 19.139 1.92124 19.4875 1.9139C19.8359 1.90657 20.1823 1.96991 20.5056 2.10012C20.8289 2.23033 21.1225 2.42473 21.3686 2.67153C21.6147 2.91833 21.8083 3.21243 21.9376 3.53609C22.0669 3.85976 22.1294 4.20626 22.1211 4.55471C22.1128 4.90316 22.0339 5.24635 21.8894 5.5635C21.7448 5.88065 21.5375 6.16524 21.2799 6.40005V6.40005Z" stroke="#247eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> <path d="M11 4H6C4.93913 4 3.92178 4.42142 3.17163 5.17157C2.42149 5.92172 2 6.93913 2 8V18C2 19.0609 2.42149 20.0783 3.17163 20.8284C3.92178 21.5786 4.93913 22 6 22H17C19.21 22 20 20.2 20 18V13" stroke="#247eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> </g>
                                
                                </svg>
                        </button>
                    {/if}
                </td>
                <td>
                    <!-- svelte-ignore a11y_consider_explicit_label -->
                    <button class="cestino" onclick={() => eliminaArticolo(item.codice_articolo)}>
                        <svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">
                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                            <g id="SVGRepo_iconCarrier"> 
                                <path d="M3 6.52381C3 6.12932 3.32671 5.80952 3.72973 5.80952H8.51787C8.52437 4.9683 8.61554 3.81504 9.45037 3.01668C10.1074 2.38839 11.0081 2 12 2C12.9919 2 13.8926 2.38839 14.5496 3.01668C15.3844 3.81504 15.4756 4.9683 15.4821 5.80952H20.2703C20.6733 5.80952 21 6.12932 21 6.52381C21 6.9183 20.6733 7.2381 20.2703 7.2381H3.72973C3.32671 7.2381 3 6.9183 3 6.52381Z" fill=""></path> 
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M11.5956 22H12.4044C15.1871 22 16.5785 22 17.4831 21.1141C18.3878 20.2281 18.4803 18.7749 18.6654 15.8685L18.9321 11.6806C19.0326 10.1036 19.0828 9.31511 18.6289 8.81545C18.1751 8.31579 17.4087 8.31579 15.876 8.31579H8.12404C6.59127 8.31579 5.82488 8.31579 5.37105 8.81545C4.91722 9.31511 4.96744 10.1036 5.06788 11.6806L5.33459 15.8685C5.5197 18.7749 5.61225 20.2281 6.51689 21.1141C7.42153 22 8.81289 22 11.5956 22ZM10.2463 12.1885C10.2051 11.7546 9.83753 11.4381 9.42537 11.4815C9.01321 11.5249 8.71251 11.9117 8.75372 12.3456L9.25372 17.6087C9.29494 18.0426 9.66247 18.3591 10.0746 18.3157C10.4868 18.2724 10.7875 17.8855 10.7463 17.4516L10.2463 12.1885ZM14.5746 11.4815C14.9868 11.5249 15.2875 11.9117 15.2463 12.3456L14.7463 17.6087C14.7051 18.0426 14.3375 18.3591 13.9254 18.3157C13.5132 18.2724 13.2125 17.8855 13.2537 17.4516L13.7537 12.1885C13.7949 11.7546 14.1625 11.4381 14.5746 11.4815Z" fill=""></path> 
                            </g>
                        </svg>
                    </button>
                </td>
            </tr>
            {/each}
        </tbody>
    </table>
    <p>valore magazzino: {$valore}</p>    <p>media magazzino :{$media}</p>
</div>


<style>
    p{
        color:rgb(33, 126, 202);
        font-weight: bold;
        display: inline-block;
        gap:10px;
    }
    .modifica{
        border: 0px;
        background-color: transparent;
    } 
     .modifica:hover{
        transform: translateY(-3px);
    }
    .modifica:active{
        transform: translateY(2px);
    }

    .cestino{
        border: 0px;
        background-color: transparent;
    }
    .cestino:hover{
        transform: translateY(-3px);
    }
    .cestino:active{
        transform: translateY(2px);
    }
    .table-container {
        background-color: #f4f4f9;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        
    }

    .table-container h1 {
        color: rgb(33, 126, 202);
        text-align: center;
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
    input{
        width: 60px;
    }
</style>