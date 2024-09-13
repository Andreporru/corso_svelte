<script lang="ts">
	import type { User } from '$lib/stores/user.svelte';
	const doSave = () => {
		onsave(user);
	};
	interface Props {
		user: User;
		onsave: (user: User) => void;
	}
	let { user: _user, onsave }: Props = $props();
	let user = $state($state.snapshot(_user));
</script>

<div class="container">
	id:{user.id}
	<br />
	ùname:<input type="text" bind:value={user.name} />
	email:<input type="text" bind:value={user.email} />
	<br />
	<button onclick={doSave}>Save</button>
</div>

<style>
	.container {
		border: 1px solid #333;
		padding: 10px;
		border-radius: 5px;
	}
</style>
