<script lang="ts">
    import { articoliStore, valore, media } from "$lib/types2";
    import { saveAs } from "file-saver";
    import { jsPDF } from "jspdf";
    import Papa from "papaparse";
    import { derived } from "svelte/store";
    import type { Item } from "$lib/types";
    import { onMount } from "svelte";
    import { exportMagazzino, importMagazzino, itemList, mediaMagazzo, valoreMagazzo } from "$lib/actions";

    const items = derived(articoliStore, ($articoliStore) => $articoliStore as Item[]);
    let percorso : string = $state("");
    let totaleMagazzino: number = $state(0);
    let sw_p : number = $state(0);
    let mediaMagazzino = $state(0);
    let isLoading = $state(false); 

    $effect(() => {
        const unsubscribeValore = valore.subscribe((val) => {
            totaleMagazzino = val ?? 0; 
        });

        const unsubscribeMedia = media.subscribe((med) => {
            mediaMagazzino = med ?? 0;
        });

        return () => {
            unsubscribeValore();
            unsubscribeMedia();
        };
    });
    const esportaCSV = async (percorso:string) => {
        isLoading = true; 
        // console.log(percorso);
        const res = await exportMagazzino(percorso);
        if (res.success)
            alert("Esportazione avvenuta con successo");
        else
            alert("Errore nell'esportazione");
        setTimeout(() => {
            isLoading = false; 
        }, 500);
        percorso = "";
        sw_p = 0;
    };
    const importaCSV = async (percorso:string) => {
        isLoading = true; 
        const res = await importMagazzino(percorso);
        if (res.success)
            alert("Importazione avvenuta con successo");
        else
            alert("Errore nell'importazione");
        setTimeout(() => {
            isLoading = false; 
        }, 500);
        percorso = "";
        sw_p = 0;
    };

    const esportaPDF = async () => {
        isLoading = true; 
        const doc = new jsPDF();
        doc.setFontSize(16);
        doc.text("Report Magazzino", 10, 10);

        doc.setFontSize(12);
        doc.text(`Valore totale magazzino: €${totaleMagazzino.toFixed(2)}`, 10, 20);
        doc.text(`Media valore magazzino: €${mediaMagazzino.toFixed(2)}`, 10, 30);

        let y = 40;
        doc.setFont("helvetica", "bold");
        doc.text("Codice", 10, y);
        doc.text("Descrizione", 60, y);
        doc.text("Prezzo (€)", 120, y);
        doc.text("Quantità", 160, y);

        y += 10;
        doc.setFont("helvetica", "normal");

        await new Promise<void>((resolve) => {
            items.subscribe((articoli) => {
                articoli.forEach((articolo) => {
                    doc.text(articolo.codice_articolo, 10, y);
                    doc.text(articolo.descrizione_articolo, 60, y);
                    doc.text(articolo.prezzo.toFixed(2), 120, y);
                    doc.text(articolo.quantita.toString(), 160, y);
                    y += 10;

                    if (y > 280) {
                        doc.addPage();
                        y = 10;
                    }
                });
                resolve();
            });
        });

        doc.save("report-magazzino.pdf");
        setTimeout(() => {
            isLoading = false; 
        }, 900);
       
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
<div class="report-container">
    <h1>Genera/Importa Report</h1>
    <p>Valore Totale Magazzino: €{totaleMagazzino ? totaleMagazzino.toFixed(2) : "0.00"}</p>
    <p>Media Valore Magazzino: €{mediaMagazzino.toFixed(2)}</p>

    {#if isLoading}
        <div class="loader"></div>
    {:else if sw_p == 0}
        <button class="normal" onclick={esportaPDF}>Esporta PDF</button>
        <button class="normal" onclick={()=> sw_p = 1}>Esporta CSV</button>
        <!-- svelte-ignore a11y_consider_explicit_label -->
        <br>
        <!-- svelte-ignore a11y_consider_explicit_label -->
        <button class="svg" onclick={()=> sw_p = 2}><svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">

            <g id="SVGRepo_bgCarrier" stroke-width="0"/>
            
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
            
            <g id="SVGRepo_iconCarrier"> <path d="M12 4L12 14M12 14L15 11M12 14L9 11" stroke="#217eca" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> <path d="M12 20C7.58172 20 4 16.4183 4 12M20 12C20 14.5264 18.8289 16.7792 17 18.2454" stroke="#217eca" stroke-width="1.5" stroke-linecap="round"/> </g>
            
            </svg></button> 
    {:else if sw_p == 1}
        <input type="text" bind:value={percorso} placeholder="Inserisci il percorso del file" />
        <button class="normal" onclick={() => esportaCSV(percorso)}>Estrai</button>
        <button class="normal" onclick={() => sw_p = 0}>Annulla</button>
    {:else if sw_p == 2}
    <input type="text" bind:value={percorso} placeholder="Inserisci il percorso del file" />
    <button class="normal"  onclick={() => importaCSV(percorso)}>Importa</button>
    <button class="normal" onclick={() => sw_p = 0}>Annulla</button>

    {/if}
</div>


<style>
    .report-container {
        text-align: center;
        margin: 20px auto;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        max-width: 600px;
    }

    h1 {
        color: rgb(33, 126, 202);
        margin-bottom: 15px;
    }

    p {
        margin: 10px 0;
        font-size: 18px;
        color: #444;
    }

    .normal {
        background-color: rgb(33, 126, 202);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 10px;
    }

    .normal:hover {
        background-color: rgb(0, 109, 211);
        transform: translateY(-2px);
    }

    .normal:active {
        transform: translateY(1px);
    }

    .loader {
        width: 40px;
        height: 40px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid rgb(33, 126, 202);
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 20px auto;
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

    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>
