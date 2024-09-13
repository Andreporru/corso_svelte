export const mkid = (prefix: string): string => {
    const id = new Date().getTime().toString(36);
    return prefix + "." + id;
}