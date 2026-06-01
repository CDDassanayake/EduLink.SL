import type { User } from '$lib/types';

let user = $state<User | null>(null);
let isLoading = $state(true);
let accessToken = $state<string | null>(null);

export function getAuthStore() {
	return {
		get user() {
			return user;
		},
		get isLoading() {
			return isLoading;
		},
		get accessToken() {
			return accessToken;
		},
		setUser(newUser: User | null) {
			user = newUser;
		},
		setAccessToken(token: string | null) {
			accessToken = token;
		},
		setLoading(val: boolean) {
			isLoading = val;
		},
		logout() {
			user = null;
			accessToken = null;
			isLoading = false;
		}
	};
}
