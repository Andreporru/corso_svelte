<script lang="ts">
    import {ibanUser} from '$lib/stores/iban.svelte';
    import { storeUser } from '$lib/stores/user.svelte';

    const calcola = () => {
        ibanUser.iban = ibanUser.st + ibanUser.cineu + ibanUser.cin + ibanUser.abi + ibanUser.cab + ibanUser.nconto;
    };
</script>


<!-- svelte-ignore css_unused_selector -->
<br><br>
<div class="container">
    {#if storeUser.id > 0}
        <h1>Inserisci iban</h1>
        <div class="primary">
        <label for="cineu">CEU</label>
        <input type="number" id="cineu" name="cineu" min="0" max="99" bind:value={ibanUser.cineu} placeholder="2 numeri" />
        </div>
        <div class="primary">
        <label for="cin">CIN</label>
        <input type="text" id="cin" name="cin" maxlength="2" bind:value={ibanUser.cin} placeholder="1 carattere" />
        </div>
        <div class="primary">
        <label for="abi">ABI</label>
        <input type="number" id="abi" name="abi" bind:value={ibanUser.abi} placeholder="5 numeri" />
        </div>
        <div class="primary">
        <label for="cab">CAB</label>
        <input type="number" id="cab" name="cab" bind:value={ibanUser.cab} placeholder="5 numeri" />
        </div>
        <div class="primary">
        <label for="nconto">N°C:</label>
        <input type="number" id="nconto" name="nconto" bind:value={ibanUser.nconto} placeholder="12 numeri" />
        </div>
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
    .primary:hover{
        transform: translateY(-8px);
      
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
        
        
        background: linear-gradient(45deg,blueviolet,   rgb(4, 161, 96));

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
        background:linear-gradient(45deg,rgb(4, 161, 96),blueviolet   );
        transform: translateY(-8px);
    }
    button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(21, 1, 29, 0.3);
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

     .error::-moz-progress-bar {
        font-size: 18px;
    }
</style>