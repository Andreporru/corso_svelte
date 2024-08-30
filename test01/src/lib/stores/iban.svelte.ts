export type Iban = {
    st: string;
    cineu: unknown;
    cin: string;
    abi: unknown;
    cab: unknown;
    nconto: unknown;
    iban: string;
}

export const ibanUser: Iban = $state({
    st: 'IT',
    cineu: null,
    cin: '',
    abi: null,
    cab: null,
    nconto: null,
    iban:'',

})