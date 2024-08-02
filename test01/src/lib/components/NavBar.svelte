<script lang="ts">
	import { counters } from '$lib/stores/counter.svelte';
	import Avatar from './Avatar.svelte';
	import Ibatar from './Ibatar.svelte';
</script>

<div class="navbar">
	<div class="links">
		<a href="/">Home</a>
		<a href="/about">About </a>
		<a href="/user-edit">Login</a>
		<a href="/user-show">Dati</a>
		<a href="/iban-edit">Iban</a>
	</div>
	<Avatar />
	<Ibatar />
</div>

<style>
	.navbar {
		display: flex;
		flex-direction: row;
		background-color: blueviolet;
		color: white;
		justify-content: space-between;

		padding: 10px;

		a {
			color: white;
			text-decoration: none;
			font-family: 'Comic Sans MS', cursive;

		}

		/*	a:hover {
			text-decoration: underline;
		}*/
	}
	.links {
		display: flex;
		flex-direction: row;
		gap: 10px;
	}
</style>
