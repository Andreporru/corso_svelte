<script lang="ts">
	import { storeUser } from '$lib/stores/user.svelte';
	const onclick =()=>{
		const nome = storeUser.name;
		const id = storeUser.id;
		const mail = storeUser.mail;
		localStorage.setItem('name',JSON.stringify(nome));
		localStorage.setItem('id',id.toString());
		localStorage.setItem('mail',JSON.stringify(mail));
	}
</script>

<br /><br />

<div class="container">
	<h1>Login</h1>
	<label for="IDuser">ID</label>
	<input type="number" id="IDuser" name="IDuser" bind:value={storeUser.id}/>

	<label for="user">Nome</label>
	<input type="text" id="user" name="user" bind:value={storeUser.name} />

	<label for="mail">Mail</label>
	<input type="mail" id="mail" name="mail" bind:value={storeUser.mail}  />
	<br>
	<button {onclick}>Login</button>
</div>

<pre>
<!--{JSON.stringify(storeUser, null, 2)}-->
</pre>

<style>
	
	
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

	input[type='text'],
	input[type='number'],
	input[type='mail'] {
		width: 100%;
		padding: 10px;
		margin: 5px 0 20px;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box;
	}
</style>
