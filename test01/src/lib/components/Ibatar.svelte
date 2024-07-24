<script lang="ts">
	import { ibanUser } from "$lib/stores/iban.svelte";



</script>

<div class="container">
    {#if ibanUser.iban != " "}
    iban:{ibanUser.iban}
    {:else}
    iban inesistente
    {/if}

</div>