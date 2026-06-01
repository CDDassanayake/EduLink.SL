const API_BASE_URL = 'http://localhost:8000/api/v1';

export async function apiClient<T>(
	endpoint: string,
	options: RequestInit = {}
): Promise<T> {
	// Get access token from auth store (will implement proper store access later)
	const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;

	const response = await fetch(`${API_BASE_URL}${endpoint}`, {
		...options,
		headers: {
			'Content-Type': 'application/json',
			...(token ? { Authorization: `Bearer ${token}` } : {}),
			...options.headers,
		},
	});

	if (!response.ok) {
		const error = await response.json().catch(() => ({ detail: 'Request failed' }));
		throw new Error(error.detail || 'Request failed');
	}

	return response.json();
}
