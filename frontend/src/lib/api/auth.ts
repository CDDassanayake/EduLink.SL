import { apiClient } from './client';

export interface LoginRequest {
	username: string;
	password: string;
}

export interface RegisterRequest {
	email: string;
	password: string;
	full_name: string;
	role: 'STUDENT' | 'TEACHER' | 'ADMIN';
	city?: string;
	phone?: string;
}

export interface AuthResponse {
	access_token: string;
	token_type: string;
}

export interface User {
	id: string;
	email: string;
	full_name: string;
	role: 'STUDENT' | 'TEACHER' | 'ADMIN';
	city?: string;
	phone?: string;
	profile_photo_url?: string;
	merit_score: number;
	is_active: boolean;
	is_verified: boolean;
	is_superuser: boolean;
	created_at: string;
	updated_at: string;
}

export async function login(username: string, password: string): Promise<AuthResponse> {
	const formData = new URLSearchParams();
	formData.append('username', username);
	formData.append('password', password);

	return apiClient<AuthResponse>('/auth/jwt/login', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		body: formData.toString(),
	});
}

export async function register(data: RegisterRequest): Promise<User> {
	return apiClient<User>('/auth/register', {
		method: 'POST',
		body: JSON.stringify(data),
	});
}

export async function getCurrentUser(): Promise<User> {
	return apiClient<User>('/auth/me');
}

export async function logout(): Promise<void> {
	return apiClient<void>('/auth/jwt/logout', {
		method: 'POST',
	});
}
