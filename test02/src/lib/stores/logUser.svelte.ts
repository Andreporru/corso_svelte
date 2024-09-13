export type loggedUser = {
    id: string;
    name: string;
    email: string;
}

interface LoggedUserStore {
    user: loggedUser
    login(email: string, password: string): Promise<boolean>;
    logout(): Promise<boolean>;
    load(): Promise<void>;
}
const LOGGED_USER_KEY = 'loggedUSer';
export const storeLoggedUser: LoggedUserStore = $state({

    user: {
        id: '',
        name: '',
        email: ''
    },
    async login(email: string, password: string): Promise<boolean> {

        if (email == 'admin@gmail.com' && password == 'admin') {
            storeLoggedUser.user = {
                id: '1',
                name: 'admin',
                email,
            };
            localStorage.setItem(LOGGED_USER_KEY, JSON.stringify(storeLoggedUser.user));
        } return false;
    },
    async logout(): Promise<boolean> {
        storeLoggedUser.user = {
            id: '',
            name: '',
            email: ''
        }
        localStorage.removeItem(LOGGED_USER_KEY);
        return true;
    },
    async load(): Promise<void> {
        const userStr = localStorage.getItem(LOGGED_USER_KEY);
        if (!userStr) {
            return;
        }
        const u = JSON.parse(userStr);
        storeLoggedUser.user = { ...storeLoggedUser, ...u };
    }
});






