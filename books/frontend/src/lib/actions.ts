const BASE_URL = 'http://localhost:8000';
export const bookAdd = async (isbn: string, title: string, author: string) => {
    console.log('=== BOOK:', isbn, title, author);

    const req = await fetch(BASE_URL + '/books/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ isbn, title, author })
    });
    const res = await req.json();

    return res;
};
export const bookList = async () => {
    const req = await fetch(BASE_URL + '/books/list');
    const res = await req.json();
    return res;
}
export const bookDel = async (isbn: string) => {

    const req = await fetch(BASE_URL + '/books/del/' + isbn, {
        method: 'DELETE',
    });
    const res = await req.json();
    return res;
}