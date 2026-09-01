import { getAuthStore } from '$lib/stores/auth.svelte';

export async function load() {
	const auth = getAuthStore();
	
	// Check authentication status on page load
	if (typeof window !== 'undefined') {
		await auth.checkAuth();
	}

	return {
		user: auth.user,
		isLoading: auth.isLoading
	};
}
