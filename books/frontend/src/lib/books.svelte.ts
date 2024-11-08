import { bookAdd, bookDel, bookList } from "./actions";
import type { Book } from "./types";

interface StoreBooks {
    books: Record<string, Book>;
    add(isbn: string, title: string, author: string): Promise<any>;
    load(): Promise<any>;
    del(isbn: string): Promise<any>;
    list(): Book[];
    getBook(isbn: string): Book | undefined;
}

export const storeBooks: StoreBooks = $state({
    books: {},
    async add(isbn: string, title: string, author: string) {
        const res = await bookAdd(isbn, title, author);

        if (res.error) return;
        storeBooks.books[isbn] = { isbn, title, author };
        return res;
    },
    async load() {
        const res = await bookList();
        if (res.error) return res;
        res.data.books.forEach((book: Book) => {
            storeBooks.books[book.isbn] = book;
        })
        return res;
    },
    async del(isbn: string) {
        const res = await bookDel(isbn);
        if (res.error) return res;
        delete storeBooks.books[isbn];
        return res;

    },
    list() {
        return Object.values(storeBooks.books);
    },
    getBook(isbn: string) {
        return storeBooks.books[isbn];
    }
});