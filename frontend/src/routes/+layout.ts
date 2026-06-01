import { getAuthStore } from '$lib/stores/auth.svelte';

export async function load() {
	// Initialize auth state from localStorage if available
	const auth = getAuthStore();
	
	if (typeof window !== 'undefined') {
		const storedToken = localStorage.getItem('access_token');
		const storedUser = localStorage.getItem('user');
		
		if (storedToken && storedUser) {
			auth.setAccessToken(storedToken);
			auth.setUser(JSON.parse(storedUser));
		}
		auth.setLoading(false);
	}

	return {
		user: auth.user,
		isLoading: auth.isLoading
	};
}
