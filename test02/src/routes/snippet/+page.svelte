<script lang="ts">
	type image = {
		url: string;
		href?: string;
	};
	const images = [
		{
			url: 'https://cdn.pixabay.com/photo/2023/09/05/14/39/old-8235289_1280.jpg',
			href: 'https://google.com'
		},
		{
			url: 'https://cdn.pixabay.com/photo/2024/02/11/13/33/kumquats-8566508_1280.jpg'
		},
		{
			url: 'https://cdn.pixabay.com/photo/2023/01/10/02/28/quad-7708760_1280.jpg',
			href: 'https://google.com'
		}
	];
</script>

{#snippet img(image: any)}
	<img src={image.url} alt="current img" />
{/snippet}

<div class="container">
	{#each images as image}
		{#if image.href}
			<a href={image.href}>
				{@render img(image)}
			</a>
		{:else}
			{@render img(image)}
		{/if}
	{/each}
</div>

<style>
	.container {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		gap: 1rep;
	}
	img {
		height: 250px;
		max-height: 250px;
	}
</style>
