<script lang="ts">
	import { goto } from '$app/navigation';
	import { storeBooks } from '$lib/books.svelte';
	interface Props {
		canDelete?: boolean;
	}
	let { canDelete = false }: Props = $props();

	const delBook = async (isbn: string) => {
		if (!confirm('Cancellare libro?')) return;
		storeBooks.del(isbn);
	};
	const modifyBook = async (isbn: string) => {
		goto('/books/edit/' + isbn);
	};
</script>

<table>
	<thead>
		<tr>
			<th>ISBN</th>
			<th>Title</th>
			<th>Author</th>

			{#if canDelete}
				<th>Actions</th>
			{/if}
		</tr>
	</thead>
	<tbody>
		{#each storeBooks.list() as book}
			<tr>
				<th>{book.isbn}</th>
				<th>{book.title}</th>
				<th> {book.author}</th>
				{#if canDelete}
					<td>
						<button onclick={() => modifyBook(book.isbn)}>modifica </button>
						<button onclick={() => delBook(book.isbn)}>Delete</button>
					</td>
				{/if}
			</tr>
		{/each}
	</tbody>
</table>
