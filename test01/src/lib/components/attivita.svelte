<script lang="ts">
    let attivita: string[] = [];
    let frase: string = '';

    const aggiungi = () => {
        if (frase.trim() !== '') {
            attivita = [...attivita, frase];
            frase = ''; // pulisce il campo di input dopo l'aggiunta
        }
    };

    const elimina = (index: number) => {
        attivita = attivita.filter((_, i) => i !== index);
    };
</script>

<div class="container" style="margin-top:50px;">
    <label for="frase">Nuova attività</label>
    <input type="text" id="frase" name="frase" bind:value={frase}>
    <button class="agg" on:click={aggiungi}>Aggiungi</button>
    <br>
    <ul>
        {#each attivita as attività, index}
            {#if index==0}
            <br>
            {/if}
            <li>
                <input type="checkbox">
                {attività}
                <button class ="annulla" on:click={() => elimina(index)}>Elimina</button>
            </li>
        {/each}
    </ul>
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

    label {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
    }

    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin: 5px 0 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
    }
    .agg {
        padding: 5px 10px;
        font-size: 14px;
        background-color:blueviolet;
        color: white;
        border: none;
        cursor: pointer;
    }

    .agg:hover {
        background-color:rgb(78, 0, 78);
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        background-color: #f2f2f2;
        padding: 5px;
        margin-bottom: 5px;
        border-radius: 3px;
        display: flex;
        align-items: center;
    }

    li span.completata {
        text-decoration: line-through;
        color: gray;
    }

    input[type="checkbox"] {
        margin-right: 10px;
    }

    .annulla {
        margin-left:auto;

        padding: 3px 6px;
        margin-left: 10px;
        background-color: #dc3545;
        color: white;
        border: none;
        cursor: pointer;
    }

    .annulla:hover {
        background-color: #c82333;
    }
</style>