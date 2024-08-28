export type User = {
    id: number;
    name: string;
    mail: string;
    password: string;
    isLogged: string;
    indirizzo: string;
};

export const storeUser: User = $state({
    id: 0,
    name: "",
    mail: "",
    password: "",
    isLogged:"false",
    indirizzo: ""
});