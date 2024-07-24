<script lang="ts">
    import {ibanUser} from '$lib/stores/iban.svelte';
	import { storeUser } from '$lib/stores/user.svelte';
    const calcola = () =>{
        ibanUser.iban=ibanUser.st+ibanUser.cineu+ibanUser.cin+ibanUser.abi+ibanUser.cab+ibanUser.nconto;
    };
    
</script>
<div class="container">
	{#if storeUser.id > 0}
		<h1>INSERISCI IBAN</h1>
        <label for="cineu">CEU</label>
        <input type="number" id="cineu" name="cineu" bind:value={ibanUser.cineu} />  (2 numeri)
        <br><br>
        <label for="cin">CIN</label>
	    <input type="text" id="cin" name="cin" bind:value={ibanUser.cin} /> (1 carattere)
        <br /><br />
        <label for="abi"> ABI</label>
        <input type="number" id="abi" name="abi" bind:value={ibanUser.abi} /> (5 numeri)
        <br /><br />
        <label for="cab"> CAB</label>
        <input type="number" id="cab" name="cab" bind:value={ibanUser.cab} /> (5 numeri)
        <br><br>
        <label for="nconto">N°C:</label>
        <input type ="number" id="nconto" name="nconto" bind:value={ibanUser.nconto} /> (12 numeri)
        <br><br>
        <button onclick={calcola}>calcola iban</button>
        <br><br>
        {ibanUser.iban}
    {:else}
		<h1>ERRORE</h1>
        <p>non è possibile inserire l'iban perchè l'utente non ha effettuato il login</p>
	{/if}
    <br><br>
 <!-- {JSON.stringify(ibanUser, null, 2)}  -->  
</div>