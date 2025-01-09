<script lang="ts">
    import ItemAdd from "$lib/components/ItemAdd.svelte";
    import ItemList from "$lib/components/ItemList.svelte";
    import { articoliStore, media, valore } from "$lib/types2";
    import { itemList, mediaMagazzo, valoreMagazzo } from "$lib/actions";
	import { onMount } from "svelte";
	import { fade } from "svelte/transition";


    onMount(async () => {
        const items = await itemList();
        const res = await valoreMagazzo();
        const res2 = await mediaMagazzo();
        articoliStore.set(items);
        valore.set(res.data);
        media.set(res2.data);
    });
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
        flex-wrap: nowrap;
        gap: 20px;
        align-items: flex-start;
    
    }

    .component-wrapper {
        flex: 1 1 45%;
    }
</style>

