<script lang="ts">
	import UserEdit from '$lib/components/UserEdit.svelte';
	import UsersList from '$lib/components/UsersList.svelte';
	import { StoreUsers, type User } from '$lib/stores/user.svelte';

	let currentUser: User = $state(StoreUsers.create());
	const dosave = (user: User) => {
		console.log('===USER', user);

		StoreUsers.add(user);
	};
	const newUser = () => {
		currentUser = StoreUsers.create();
	};
</script>

<br />
<button onclick={newUser}>nuovo utente</button>
<br />
{#key currentUser.id}
	<UserEdit user={currentUser} onsave={dosave} />
{/key}

<UsersList />
