<script lang="ts">
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto'; // Importazione relativa per Chart.js
    import { articoliStore } from "$lib/types2";
    import { derived } from "svelte/store";
  
    // Grafico per quantità per prodotto
    const datiQuantita = derived(articoliStore, ($articoliStore) => {
      return $articoliStore.map(articolo => ({
        label: articolo.descrizione_articolo,
        value: articolo.quantita
      }));
    });
  
    // Grafico per valore totale per prodotto
    const datiValore = derived(articoliStore, ($articoliStore) => {
      return $articoliStore.map(articolo => ({
        label: articolo.descrizione_articolo,
        value: articolo.prezzo * articolo.quantita
      }));
    });
  
    let chartQuantitaInstance:Chart;
    let chartValoreInstance:Chart; 
    let canvasQuantita:HTMLCanvasElement; 
    let canvasValore:HTMLCanvasElement; // Canvas per il grafico valore
  
    onMount(() => {
      // Dati per il grafico quantità
      datiQuantita.subscribe(data => {
        if (chartQuantitaInstance) {
          chartQuantitaInstance.destroy();
        }
  
        const labels = data.map(d => d.label);
        const values = data.map(d => d.value);
  
        chartQuantitaInstance = new Chart(canvasQuantita, {
          type: 'bar',
          data: {
            labels,
            datasets: [
              {
                label: 'Quantità per prodotto',
                data: values,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
              }
            ]
          },
          options: {
            responsive: true,
            plugins: {
              legend: { display: true },
              tooltip: { enabled: true }
            },
            scales: {
              y: { beginAtZero: true }
            }
          }
        });
      });
  
      // Dati per il grafico valore totale
      datiValore.subscribe(data => {
        if (chartValoreInstance) {
          chartValoreInstance.destroy();
        }
  
        const labels = data.map(d => d.label);
        const values = data.map(d => d.value);
  
        chartValoreInstance = new Chart(canvasValore, {
          type: 'bar',
          data: {
            labels,
            datasets: [
              {
                label: 'Valore totale per prodotto',
                data: values,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
              }
            ]
          },
          options: {
            responsive: true,
            plugins: {
              legend: { display: true },
              tooltip: { enabled: true }
            },
            scales: {
              y: { beginAtZero: true }
            }
          }
        });
      });
    });
  </script>
  
  <div class="stat-container">
    <div class="chart-container">
      <h3>Quantità per Prodotto</h3>
      <canvas bind:this={canvasQuantita}></canvas>
    </div>
    <div class="chart-container">
      <h3>Valore Totale per Prodotto</h3>
      <canvas bind:this={canvasValore}></canvas>
    </div>
  </div>
  
  <style>
    .stat-container {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 20px;
      padding: 20px;

    
      animation: fadeIn 0.5s ease-in-out;
      margin-top: 50px;
    }
  
    .chart-container {
      width: 45%;
      max-width: 500px;
      padding: 10px;
      background: #ffffff;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      text-align: center;
    }
  
    canvas {
      display: block;
      width: 100%;
      height: 300px;
    }
  
    h3 {
      font-size: 18px;
      margin-bottom: 10px;
      color: rgb(33, 126, 202);
    }
  
    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
  </style>
  