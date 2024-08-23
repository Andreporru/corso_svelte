<script lang="ts">
	import { goto } from '$app/navigation';


	import { storeUser } from '$lib/stores/user.svelte';
	import { redirect } from '@sveltejs/kit';
	let password : string;
	let id:number;
    let sw=0;


	let firstpassword:string;
	const onclick =()=>{

			sw=0;
			
			const savedId = localStorage.getItem(`id_${id}`);

		    const savedpassword = localStorage.getItem(`password_${id}`);
            if (!savedId){
                sw=1;
            }else
            {

                sw=0;
                if(password===savedpassword)
                {
                   
                    const savedname = localStorage.getItem(`nome_${id}`);
                    const savedmail = localStorage.getItem(`mail_${id}`);
                    storeUser.isLogged="true";
                    if(savedname)
                    {
                        storeUser.name=savedname;   
                    }
                    if(savedmail)
                    {
                        storeUser.mail=savedmail;   
                    }
                    storeUser.id=Number(savedId);

                }else
                {
                    sw=3;
                }
            }
		
		}
	
</script>

<br /><br />

<div class="container">
{#if storeUser.isLogged=="false"}
	<h1>Login</h1>
	<label for="IDuser">ID</label>
	<input type="number" id="IDuser" name="IDuser" bind:value={id}/>

	
	<label for="password">password</label>
	<input type="password" id="password" name="password" bind:value={password}  />

	<br>
	

	<button {onclick}>login</button>
{:else if storeUser.isLogged== "true"}
<p>login effettuato con successo</p>
{/if}


</div>
{#if sw===1}
    <p>id non trovato, </p>
    <a href="/user-edit"> Registrarsi?</a>
{/if}
{#if sw===3}
    <p>Password o id errati</p>
{/if}

<pre>
{JSON.stringify(storeUser, null, 2)}
</pre>

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


	input[type='number'],
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
