<script lang="ts">
    import { onMount } from 'svelte';
  
    let dataCorrente = new Date();
    let meseCorrente = dataCorrente.getMonth();
    let annoCorrente = dataCorrente.getFullYear();
    let giorniNelMese: number[] = [];
    const giorniDellaSettimana = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']; 
  
    // Funzione per ottenere i giorni del mese
    function ottieniGiorniNelMese(mese: number, anno: number): number[] {
      const data = new Date(anno, mese, 1);
      const giorni: number[] = [];
  
      // Aggiungi i giorni vuoti per allineare il primo giorno del mese
      const indicePrimoGiorno = (data.getDay() + 6) % 7; // Calcola l'indice del primo giorno (Lun = 0)
      for (let i = 0; i < indicePrimoGiorno; i++) {
        giorni.push(0);
      }
  
      // Aggiungi i giorni del mese
      while (data.getMonth() === mese) {
        giorni.push(data.getDate());
        data.setDate(data.getDate() + 1);
      }
      return giorni;
    }
  
    // Funzione per cambiare mese
    function cambiaMese(cambiamento: number) {
      meseCorrente += cambiamento;
      if (meseCorrente < 0) {
        meseCorrente = 11;
        annoCorrente--;
      } else if (meseCorrente > 11) {
        meseCorrente = 0;
        annoCorrente++;
      }
      dataCorrente = new Date(annoCorrente, meseCorrente); // Aggiorna la data corrente
      giorniNelMese = ottieniGiorniNelMese(meseCorrente, annoCorrente); // Aggiorna i giorni del mese
    }
  
    onMount(() => {
      giorniNelMese = ottieniGiorniNelMese(meseCorrente, annoCorrente);
    });
  </script>
  
  
  
  <div class="calendario" style=" margin-top: 50px;">
    <h1>{dataCorrente.toLocaleString('it-IT', { month: 'long' })} {annoCorrente}</h1>
    <div class="intestazione">
      <button on:click={() => cambiaMese(-1)}>Precedente</button>
      <button on:click={() => cambiaMese(1)}>Successivo</button>
    </div>
    
    <!-- Giorni della settimana -->
    <div class="giorni-della-settimana">
      {#each giorniDellaSettimana as giornoDellaSettimana}
        <div class="giorno-della-settimana">{giornoDellaSettimana}</div>
      {/each}
    </div>
  
    <!-- Giorni del mese -->
    <div class="giorni">
      {#each giorniNelMese as giorno}
        <div class="giorno">{giorno ?? ''}</div>
      {/each}
    </div>
  </div>
  <style>
    .calendario {
       
      font-family: Arial, sans-serif;
      max-width: 400px;
      margin: 0 auto;
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      background-color: #f4f4f9;
    }
  
    h1 {
      color: blueviolet;
      font-size: 24px;
      text-align: center;
      margin-bottom: 20px;
    }
  
    .intestazione {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
  
    .intestazione button {
      background: blueviolet;
      color: white;
      padding: 10px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  
  
    .giorni, .giorni-della-settimana {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 10px;
    }
  
    .giorno, .giorno-della-settimana {
      padding: 10px;
      background-color: #e0e0e0;
      border-radius: 5px;
      text-align: center;
    }
  
    .giorno-della-settimana {
      font-weight: bold;
      background-color: transparent;
      color: blueviolet;
    }
  </style>