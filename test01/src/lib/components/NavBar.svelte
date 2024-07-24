<script lang="ts">
	import { counters } from '$lib/stores/counter.svelte';
	import Avatar from './Avatar.svelte';
</script>

<div class="navbar">
	<div class="links">
		<a href="/">Home</a>
		<a href="/about">About </a>
		<a href="/user-edit"> user</a>
	</div>
	<Avatar />
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
