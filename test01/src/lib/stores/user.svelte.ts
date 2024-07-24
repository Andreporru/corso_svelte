export type User = {
    id: number;
    name: string;
    mail: string;
};

export const storeUser: User = $state({
    id: 0,
    name: "",
    mail: "",
});