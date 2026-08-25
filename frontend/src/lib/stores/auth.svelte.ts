import type { User } from '$lib/types';
import { login as apiLogin, logout as apiLogout, getCurrentUser } from '$lib/api/auth';

let user = $state<User | null>(null);
let isLoading = $state(true);
let accessToken = $state<string | null>(null);

// Initialize from localStorage
if (typeof window !== 'undefined') {
	const storedToken = localStorage.getItem('access_token');
	if (storedToken) {
		accessToken = storedToken;
	}
}

export function getAuthStore() {
	const store = {
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
			if (typeof window !== 'undefined') {
				if (token) {
					localStorage.setItem('access_token', token);
				} else {
					localStorage.removeItem('access_token');
				}
			}
		},
		setLoading(val: boolean) {
			isLoading = val;
		},
		async login(email: string, password: string) {
			try {
				store.setLoading(true);
				const response = await apiLogin(email, password);
				store.setAccessToken(response.access_token);
				
				// Get user data after login
				const userData = await getCurrentUser();
				store.setUser(userData);
				store.setLoading(false);
				return true;
			} catch (error: any) {
				store.setLoading(false);
				// Convert technical errors to user-friendly messages
				if (error?.response?.status === 401) {
					throw new Error('Invalid email or password. Please try again.');
				} else if (error?.response?.status === 400) {
					throw new Error('Please check your email and password and try again.');
				} else if (error?.message && !error?.response) {
					throw error;
				} else {
					throw new Error('Login failed. Please try again later.');
				}
			}
		},
		async logout() {
			try {
				await apiLogout();
			} catch (error) {
				console.error('Logout error:', error);
			} finally {
				store.setAccessToken(null);
				user = null;
				isLoading = false;
			}
		},
		async checkAuth() {
			try {
				if (accessToken) {
					const userData = await getCurrentUser();
					store.setUser(userData);
				}
			} catch (error) {
				// Token might be expired, clear auth state
				store.logout();
			} finally {
				store.setLoading(false);
			}
		}
	};
	return store;
}
