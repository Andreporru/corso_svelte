<script lang="ts">
	import { bookAdd } from '$lib/actions';
	import { storeBooks } from '$lib/books.svelte';
	import type { Book } from '$lib/types';

	interface Props {
		book?: Book;
	}
	let { book }: Props = $props();

	let isbn: string = $state(book ? book.isbn : '');
	let title: string = $state(book ? book.title : '');
	let author: string = $state(book ? book.author : '');

	const BASE_URL = 'http://localhost:8000';

	const book_add = async () => {
		const res = await storeBooks.add(isbn, title, author);

		if (res.console.error) {
			alert(res.error.message);
			return;
		}
	};
</script>

<div class="book-add-container">
	ISBN:<input type="text" bind:value={isbn} /><br />
	TITLE:<input type="text" bind:value={title} /><br />
	AUTHOR:<input type="text" bind:value={author} /><br />
	<button onclick={book_add}>Add</button>
</div>
