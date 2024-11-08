<script lang="ts">
	import { page } from '$app/stores';
	import { storeBooks } from '$lib/books.svelte';
	import BookAdd from '$lib/components/BookAdd.svelte';
	import type { Book } from '$lib/types';

	let isbn = $page.params.isbn;
	let book: Book | undefined = storeBooks.getBook(isbn);
</script>

{#if book}
	<BookAdd {book} />
{:else}
	<p>Book not found</p>
{/if}
