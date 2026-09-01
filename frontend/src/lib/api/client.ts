const API_BASE_URL = 'http://localhost:8000/api/v1';

export async function apiClient<T>(
	endpoint: string,
	options: RequestInit = {}
): Promise<T> {
	// Get access token from localStorage
	const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;

	// Don't set default Content-Type if it's already set (e.g., for form data)
	const hasContentType = options.headers && 
		(typeof options.headers === 'object' && 'Content-Type' in options.headers);

	const headers: Record<string, string> = {
		...(hasContentType ? {} : { 'Content-Type': 'application/json' }),
		...(token ? { Authorization: `Bearer ${token}` } : {}),
		...(typeof options.headers === 'object' ? options.headers as Record<string, string> : {}),
	};

	const response = await fetch(`${API_BASE_URL}${endpoint}`, {
		...options,
		headers,
	});

	if (!response.ok) {
		const errorData = await response.json().catch(() => ({ detail: 'Request failed' }));
		const error = new Error(errorData.detail || 'Request failed');
		(error as any).response = {
			status: response.status,
			data: errorData
		};
		throw error;
	}

	return response.json();
}
