

export type User = {
    id: string;
    name: string;
    surname:string;
    luogon:string;
    datan:string;
    mail: string;
    password: string;
    isLogged: string;
    indirizzo: string;
};

export const storeUser: User = $state({
    id: "",
    name: "",
    surname:"",
    luogon:"",
    datan:"",
    mail: "",
    password: "",
    isLogged:"false",
    indirizzo: ""
});