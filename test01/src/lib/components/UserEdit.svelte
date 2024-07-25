<script lang="ts">
    import { storeUser } from '$lib/stores/user.svelte';
</script>

<br><br>

<div class="container">
    <h1>Login</h1>
    <label for="IDuser">ID</label>
    <input type="number" id="IDuser" name="IDuser" bind:value={storeUser.id} />

    <label for="user">Nome</label>
    <input type="text" id="user" name="user" bind:value={storeUser.name} />

    <label for="mail">Mail</label>
    <input type="mail" id="mail" name="mail" bind:value={storeUser.mail} />
</div>

<pre>
<!--{JSON.stringify(storeUser, null, 2)}-->
</pre>
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
        color:blueviolet;
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
    input[type="number"],
    input[type="mail"] {
        width: 100%;
        padding: 10px;
        margin: 5px 0 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
    }


</style>
