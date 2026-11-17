import { apiClient } from './client';

export interface TeacherVerification {
	id: string;
	user_id: string;
	full_name: string;
	email: string;
	city: string | null;
	bio: string | null;
	years_experience: number | null;
	document_urls: string | null;
	verification_status: 'PENDING' | 'APPROVED' | 'REJECTED';
	verification_note: string | null;
	created_at: string;
}

// Admin teacher verification endpoints
export async function getVerifications(statusFilter?: string): Promise<TeacherVerification[]> {
	const params = statusFilter ? `?status_filter=${statusFilter}` : '';
	return apiClient<TeacherVerification[]>(`/admin/verifications${params}`);
}

export async function approveVerification(profileId: string): Promise<TeacherVerification> {
	return apiClient<TeacherVerification>(`/admin/verifications/${profileId}/approve`, {
		method: 'PATCH',
	});
}

export async function rejectVerification(profileId: string, reason?: string): Promise<TeacherVerification> {
	const params = reason ? `?reason=${encodeURIComponent(reason)}` : '';
	return apiClient<TeacherVerification>(`/admin/verifications/${profileId}/reject${params}`, {
		method: 'PATCH',
	});
}
