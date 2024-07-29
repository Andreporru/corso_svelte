<script lang="ts">
	import { ibanUser } from "$lib/stores/iban.svelte";
	import { storeUser } from "$lib/stores/user.svelte";
	import UserEdit from "./UserEdit.svelte";
 


</script>

<div class="container">
    {#if ibanUser.iban != " " }
    iban:{ibanUser.iban}
    {:else if storeUser.id != 0}
    iban inesistente
    {/if}

</div>