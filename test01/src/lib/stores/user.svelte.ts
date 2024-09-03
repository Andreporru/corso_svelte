export type User = {
    id: string;
    name: string;
    mail: string;
    password: string;
    isLogged: string;
    indirizzo: string;
};

export const storeUser: User = $state({
    id: "",
    name: "",
    mail: "",
    password: "",
    isLogged:"false",
    indirizzo: ""
});