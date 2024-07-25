<script lang="ts">
    import {ibanUser} from '$lib/stores/iban.svelte';
    import { storeUser } from '$lib/stores/user.svelte';

    const calcola = () => {
        ibanUser.iban = ibanUser.st + ibanUser.cineu + ibanUser.cin + ibanUser.abi + ibanUser.cab + ibanUser.nconto;
    };
</script>


<br><br>
<div class="container">
    {#if storeUser.id > 0}
        <h1>Inserisci iban</h1>
        <label for="cineu">CEU</label>
        <input type="number" id="cineu" name="cineu" bind:value={ibanUser.cineu} placeholder="2 numeri" />
        
        <label for="cin">CIN</label>
        <input type="text" id="cin" name="cin" bind:value={ibanUser.cin} placeholder="1 carattere" />
        
        <label for="abi">ABI</label>
        <input type="number" id="abi" name="abi" bind:value={ibanUser.abi} placeholder="5 numeri" />
        
        <label for="cab">CAB</label>
        <input type="number" id="cab" name="cab" bind:value={ibanUser.cab} placeholder="5 numeri" />
        
        <label for="nconto">N°C:</label>
        <input type="number" id="nconto" name="nconto" bind:value={ibanUser.nconto} placeholder="12 numeri" />
        
        <button onclick={calcola}>Calcola IBAN</button>
        
        <div class="result">{ibanUser.iban}</div>
    {:else}
        <h1 class="error">ERRORE</h1>
        <p class="error">Non è possibile inserire l'IBAN perché l'utente non ha effettuato il login</p>
    {/if}
</div>
<style>
    .container {
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
        margin-bottom: 20px;
        text-align: center;
    }

    label {
        display: block;
        margin: 10px 0 5px;
        font-weight: bold;
    }

    input[type="text"],
    input[type="number"] {
        width: 100%;
        padding: 10px;
        margin: 5px 0 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
    }

    button {
        background-color:blueviolet;
        Font-family: 'Comic Sans MS', cursive;
        color: white;
        padding: 15px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        margin-top: 20px;
        display: block;
        width: 100%;
    }

    button:hover {
        background-color: blueviolet;
    }

    .result {
        margin-top: 20px;
        font-weight: bold;
        text-align: center;
        color:blueviolet;
    }

    .error {
        color: red;
        text-align: center;
    }

     .error   ::-moz-progress-bar {
        font-size: 18px;
    }
</style>