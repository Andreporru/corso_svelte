<script lang="ts">
	import { goto } from '$app/navigation';


	import { storeUser } from '$lib/stores/user.svelte';
	import { redirect } from '@sveltejs/kit';
	let password : string;
	let sw = 0;

	

	let firstpassword:string;
	const onclick =()=>{
		if (storeUser.password && password && storeUser.password !== password)
		{
			console.log('password incompleta o diversa');
			sw=1;
		}else 
		{

	        storeUser.isLogged = "true";
			const nome = storeUser.name;
			const id = storeUser.id;
			const mail = storeUser.mail;
			const pass = storeUser.password;
			localStorage.setItem(`nome_${storeUser.id}`,nome);
			localStorage.setItem(`id_${storeUser.id}`,id.toString());
			localStorage.setItem(`mail_${storeUser.id}`,mail);
			localStorage.setItem(`password_${storeUser.id}`,pass);
			goto("/");
		}
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
	
	<label for="password">password</label>
	<input type="password" id="password" name="password" bind:value={storeUser.password}  />


	<label for="confermaPassword">conferma password</label>
	<input type="password" id="confermaPassword" name="confermaPassword"
	style= "box-shadow: {storeUser.password && password && storeUser.password !== password ? '0 0 15px red' : 'none'}"
	bind:value={password}  />

	
	{#if storeUser.password && password && storeUser.password !== password}
		<p>Password incongruenti</p>
	{/if}
	{#if sw==1}
		<p></p>
	{/if}

	<br>
	

	<button {onclick}>registrati</button>



</div>
	{#if sw==1}
	<p>conferma password incompleta o icongruente</p>
	{/if}

<!-- <pre>
{JSON.stringify(storeUser, null, 2)}
</pre> -->

<style>
	p{
		color: red;
		font-size: 13px;
		margin-top: -10px;
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
	input[type='mail'],
	input[type='password']
	 {
		width: 100%;
		padding: 10px;
		margin: 5px 0 20px;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box;
	}
	
  
</style>
