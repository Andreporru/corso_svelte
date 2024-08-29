<script lang="ts">
	import { counters } from '$lib/stores/counter.svelte';
	import Avatar from './Avatar.svelte';
	import Ibatar from './Ibatar.svelte';
</script>

<div class="navbar">
	<div class="links">
		<a href="/">Home</a>
		<a href="/about">About </a>
		<a href="/login">Login</a>
		<a href="/user-show">Dati</a>
		<a href="/iban-edit">Iban</a>
		<a href="/activities">attività</a>
		<a href="/finances">finanze</a>
		<a href="/calcula">calcolatrice</a>
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

		font-size: 20px;

		a {
			color: white;
			text-decoration: none;
		}

		/*	a:hover {
			text-decoration: underline;
		}*/
	}
	a:hover {
		font-size: larger;
	}
	.links {
		display: flex;
		flex-direction: row;
		gap: 10px;
	}
</style>
