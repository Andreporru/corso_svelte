<script lang="ts">
	import { storeUser } from '$lib/stores/user.svelte';
</script>

<div class="container">
	<h1>User Edit</h1>
	<label for="IDuser">id</label>
	<input type="number" id="IDuser" name="IDuser" bind:value={storeUser.id} />
	<br /><br />
	<label for="user"> nome</label>
	<input type="text" id="user" name="user" bind:value={storeUser.name} />
	<br /><br />
	<label for="mail"> mail</label>
	<input type="mail" id="mail" name="mail" bind:value={storeUser.mail} />
</div>

<pre>
    {JSON.stringify(storeUser, null, 2)}
</pre>
