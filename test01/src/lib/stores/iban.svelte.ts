export type Iban = {
    st: string;
    cineu: number;
    cin: string;
    abi: number;
    cab: number;
    nconto: number;
    iban: string;
}

export const ibanUser: Iban = $state({
    st: "IT",
    cineu: 0,
    cin: " ",
    abi: 0,
    cab: 0,
    nconto: 0,
    iban:" ",

})