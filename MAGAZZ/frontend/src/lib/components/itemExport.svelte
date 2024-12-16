<script lang="ts">
    import { articoliStore, valore, media } from "$lib/types2";
    import { saveAs } from "file-saver";
    import { jsPDF } from "jspdf";
    import Papa from "papaparse";
    import { derived } from "svelte/store";
    import type { Item } from "$lib/types";
	import { onMount } from "svelte";
	import { itemList, mediaMagazzo, valoreMagazzo } from "$lib/actions";

    // Derivato per ottenere la lista degli articoli
    const items = derived(articoliStore, ($articoliStore) => $articoliStore as Item[]);

    // Variabili per totale e media del magazzino
    let totaleMagazzino: number = $state(0);
    let mediaMagazzino = $state(0);

    $effect(() => {
        const unsubscribeValore = valore.subscribe((val) => {
           
            totaleMagazzino = val ?? 0; // Fallback a 0 se val è undefined
            console.log("eee:",totaleMagazzino);
        });

        const unsubscribeMedia = media.subscribe((med) => {
            mediaMagazzino = med ?? 0;
        });

        return () => {
            unsubscribeValore();
            unsubscribeMedia();
        };
    });
    
 


    
    const esportaPDF = () => {
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
        });

        doc.save("report-magazzino.pdf");
    };

  
    const esportaCSV = () => {

        items.subscribe((articoli) => {
            const data = articoli.map((articolo) => ({
                "Codice Articolo": articolo.codice_articolo,
                "Descrizione": articolo.descrizione_articolo,
                "Prezzo (€)": articolo.prezzo.toFixed(2),
                "Quantità": articolo.quantita,
            }));

            const csv = Papa.unparse(data);
            const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
            saveAs(blob, "report-magazzino.csv");
        });
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


<div class="report-container">
    <h1>Genera Report</h1>
    <p>Valore Totale Magazzino: €{totaleMagazzino ? totaleMagazzino.toFixed(2) : "0.00"}</p>

    <p>Media Valore Magazzino: €{mediaMagazzino.toFixed(2)}</p>
    <button onclick={esportaPDF}>Esporta PDF</button>
    <button onclick={esportaCSV}>Esporta CSV</button>
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

    button {
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

    button:hover {
        background-color: rgb(0, 109, 211);
        transform: translateY(-2px);
    }

    button:active {
        transform: translateY(1px);
    }

    @media (max-width: 600px) {
        button {
            width: 100%;
            margin: 10px 0;
        }
    }
</style>