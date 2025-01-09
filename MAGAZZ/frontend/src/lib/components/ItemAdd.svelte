<script lang="ts">
    import { articoliStore, media, valore } from "$lib/types2";
    import { itemAdd, itemList, mediaMagazzo, valoreMagazzo } from "$lib/actions";
	import { fade } from "svelte/transition";
	import { onMount } from "svelte";


    let codice_articolo: string = "";
    let descrizione_articolo: string = "";
    let prezzo: number = 0;
    let quantita: number = 0;
    let sw_e: number = 0; 
    let sw_c:number=0;
    let errore: string | null = null; 
    $: sw_c = codice_articolo !== "" ? 0 : sw_c;

    const item_Add = async () => {
        sw_e = 0; 
        errore = null;
        
        

        
        if(codice_articolo=="")
        {
            sw_c=1;
        }else{
            const result = await itemAdd(codice_articolo, descrizione_articolo, prezzo, quantita);
            if (!result.success) {
            sw_e = 1;
            errore = result.error;  
            } else {
                sw_e = 0; 
                errore = null;
                codice_articolo = "";
                descrizione_articolo = "";
                prezzo = 0;
                quantita = 0;

             
                articoliStore.update((articoli) => [...articoli, result.data]);
                alert("Articolo aggiunto con successo!");
                const items = await itemList();
                articoliStore.set(items);
                const res = await valoreMagazzo();
                if (res.success) {
                    valore.set(res.data); 
                }else{
                    console.error("Errore:", res.error);
                }
                const res2 = await mediaMagazzo();
                if (res2.success) {
                    media.set(res2.data);
                }else{
                    console.error("Errore:", res2.error);
                }
            }
        }
    //    location.reload();
   };
    onMount(async () => {
        const items = await itemList();
        const res = await valoreMagazzo();
        const res2 = await mediaMagazzo();
        articoliStore.set(items);
        valore.set(res.data);
        media.set(res2.data);
    });
</script>


<br>
<br>
<div class="form-container" >
    <h1>Aggiunta Articolo</h1>
    <div>
        Codice articolo:
        <input type="text" bind:value={codice_articolo} />
    </div>
    <div>
        Descrizione articolo:
        <input type="text" bind:value={descrizione_articolo} />
    </div>
    <div>
        Prezzo:
        <input type="number" bind:value={prezzo} />
    </div>
    <div>
        Quantità:
        <input type="number" bind:value={quantita} />
    </div>
    <button onclick={item_Add}>Aggiungi</button>

    {#if sw_e === 1}
        {console.log("Errore:", errore)}
        <p class="error-message">Errore: {errore}</p>
    {/if}
    {#if sw_c === 1}
    <p class="error-message">Errore: codice articolo nullo</p>
    {/if}

</div>

<style>
    .form-container {
        background-color: #f4f4f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    .form-container h1 {
        color: rgb(33, 126, 202);
        text-align: center;
    }

    .form-container div {
        margin-bottom: 15px;
    }

    .form-container input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
    }

    .form-container button {
        display: block;
        width: 100%;
        padding: 10px;
        background-color: rgb(33, 126, 202);
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .form-container button:hover {
        background-color: rgb(0, 109, 211);
    }

    .error-message {
        color: red;
        font-weight: bold;
        margin-top: 10px;
    }
</style>