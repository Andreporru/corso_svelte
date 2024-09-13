import { mkid } from "$lib/utils";

export type User = {
    id: string;
    name: string;
    email: string;
};

interface UsersStore {
    users: Record<string, User>;

    create(): User;
    add(user: User, save?: boolean): Promise<void>;
    del(id: string): Promise<void>;
    get(id: string): Promise<User>;
    list(): User[];
    load(): Promise<void>;
}

const USERS_KEYS = 'users_keys';
export const StoreUsers: UsersStore = $state({
    users: {},

    create(): User {
        return {
            id: mkid('user'),
            name: '',
            email: '',
        };
    },
    async add(user: User, save = true) {
        if (save) {
            StoreUsers.users[user.id] = user;
            localStorage.setItem(user.id, JSON.stringify(user))
            localStorage.setItem(USERS_KEYS, JSON.stringify(Object.keys(StoreUsers)));
        }
    },
    async del(id: string) {
        delete StoreUsers.users[id];
        localStorage.removeItem(id);
        localStorage.setItem(USERS_KEYS, JSON.stringify(Object.keys(StoreUsers)));
    },
    async get(id: string): Promise<User> {
        return StoreUsers.users[id];
    },
    list(): User[] {
        return Object.values(StoreUsers.users);
    },
    async load() {
        const keys: string[] = JSON.parse(localStorage.getItem(USERS_KEYS) || '[]');
        keys.map((id: string) => {
            const user = StoreUsers.create();
            const userStr = localStorage.getItem(id);
            if (!userStr) return;

            const userObj = JSON.parse(userStr);
            StoreUsers.add({ ...user, ...userObj }, false);
        }
        )
    },
});

