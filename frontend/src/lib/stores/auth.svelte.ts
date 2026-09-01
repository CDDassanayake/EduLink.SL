import type { User } from '$lib/types';
import { login as apiLogin, logout as apiLogout, getCurrentUser } from '$lib/api/auth';

let user = $state<User | null>(null);
let isLoading = $state(true);
let accessToken = $state<string | null>(null);

// Initialize from localStorage
if (typeof window !== 'undefined') {
	const storedToken = localStorage.getItem('access_token');
	const storedUser = localStorage.getItem('user');
	
	if (storedToken) {
		accessToken = storedToken;
	}
	
	if (storedUser) {
		try {
			user = JSON.parse(storedUser);
		} catch (e) {
			console.error('Failed to parse stored user:', e);
		}
	}
	
	// If we have a token but no user, try to fetch user data
	if (storedToken && !user) {
		isLoading = true;
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
			if (typeof window !== 'undefined') {
				if (newUser) {
					localStorage.setItem('user', JSON.stringify(newUser));
				} else {
					localStorage.removeItem('user');
				}
			}
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
				
				// Clear any existing auth data before login
				if (typeof window !== 'undefined') {
					localStorage.removeItem('access_token');
					localStorage.removeItem('user');
				}
				
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
				// Clear all auth state
				store.setAccessToken(null);
				store.setUser(null);
				isLoading = false;
				
				// Clear localStorage completely
				if (typeof window !== 'undefined') {
					localStorage.removeItem('access_token');
					localStorage.removeItem('user');
				}
			}
		},
		async checkAuth() {
			try {
				if (accessToken) {
					const userData = await getCurrentUser();
					store.setUser(userData);
				} else {
					// No token, clear user data
					store.setUser(null);
				}
			} catch (error) {
				// Token might be expired, clear auth state
				console.error('Auth check failed:', error);
				store.setAccessToken(null);
				store.setUser(null);
				
				// Clear localStorage on auth failure
				if (typeof window !== 'undefined') {
					localStorage.removeItem('access_token');
					localStorage.removeItem('user');
				}
			} finally {
				store.setLoading(false);
			}
		}
	};
	return store;
}
