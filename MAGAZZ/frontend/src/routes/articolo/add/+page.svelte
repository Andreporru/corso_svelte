<script lang="ts">
    import ItemAdd from "$lib/components/ItemAdd.svelte";
    import ItemList from "$lib/components/ItemList.svelte";
    import { articoliStore, media, valore } from "$lib/types2";
    import { itemList, mediaMagazzo, valoreMagazzo } from "$lib/actions";
	import { onMount } from "svelte";
	import { fade } from "svelte/transition";

    // Carica gli articoli iniziali nel `articoliStore`
    // onMount(async () => {
    //     const items = await itemList();
    //     const res = await valoreMagazzo();
    //     const res2 = await mediaMagazzo();
    //     articoliStore.set(items);
    //     valore.set(res.data);
    //     media.set(res2.data);
    // });
</script>

<div class="pagina-container" in:fade={{ duration: 400 }}>
    <div class="component-wrapper">
        <ItemAdd />
    </div>
    <div class="component-wrapper">
        <ItemList />
    </div>
</div>

<style>
    .pagina-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
        max-width: 1200px;
        margin: 0 auto;
        font-family: Arial, sans-serif;
    }

    .component-wrapper {
        flex: 1 1 45%;
    }
</style>

