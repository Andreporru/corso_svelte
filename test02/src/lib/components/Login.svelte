<script lang="ts">
	import { goto } from '$app/navigation';
	import { storeLoggedUser } from '$lib/stores/logUser.svelte';

	let email = $state('');
	let password = $state('');
	interface Props {
		destURL?: string;
	}
	let { destURL }: Props = $props();
	let error = $state('');
	const login = async () => {
		error = '';
		const res: boolean = await storeLoggedUser.login(email, password);
		if (res == true) {
			//tutto ok
			if (destURL) goto(destURL);
		} else {
			//no
			error = 'email o password errati';
		}
	};
</script>

<div class="container">
	email:<input type="text" bind:value={email} />
	<br />
	password:<input type="text" bind:value={password} />
	<br />
	<button onclick={login}>Login</button>
	{#if error}
		<p style="color:red">{error}</p>
	{/if}
</div>

<!-- <pre>
{JSON.stringify(LoggedUserStore, null, 2)}
</pre> -->
<style>
	.container {
		border: 1px solid #999;
		padding: 10px;
		border-radius: 5px;
	}
</style>
