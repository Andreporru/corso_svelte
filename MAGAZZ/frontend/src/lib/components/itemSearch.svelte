<script lang="ts">
import { derived } from 'svelte/store';
import { articoliStore } from "$lib/types2";
import type { Item } from "$lib/types";

// Create a derived store to get the items from articoliStore
const items = derived(articoliStore, ($articoliStore) => $articoliStore as Item[]);
let codice:number=$state(0);
let sw:number=$state(0);

</script>

<input type="text" bind:value={codice} >
<button class="svg"><svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#217eca">

    <g id="SVGRepo_bgCarrier" stroke-width="0"/>
    
    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
    
    <g id="SVGRepo_iconCarrier"> <path d="M11 6C13.7614 6 16 8.23858 16 11M16.6588 16.6549L21 21M19 11C19 15.4183 15.4183 19 11 19C6.58172 19 3 15.4183 3 11C3 6.58172 6.58172 3 11 3C15.4183 3 19 6.58172 19 11Z" stroke="#217eca" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> </g>
    
    </svg></button>
<style>
        .svg{
        border: 0px;
        background-color: transparent;
    }
    .svg:hover{
        transform: translateY(-3px);
    }
    .svg:active{
        transform: translateY(2px);
    }
</style>




