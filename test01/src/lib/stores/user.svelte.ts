export type User = {
    id: unknown;
    name: string;
    mail: string;
    password: string;
    isLogged: string;
    indirizzo: string;
};

export const storeUser: User = $state({
    id: null,
    name: "",
    mail: "",
    password: "",
    isLogged:"false",
    indirizzo: ""
});