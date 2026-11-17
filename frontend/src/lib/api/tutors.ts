import { apiClient } from './client';

const API_BASE_URL = 'http://localhost:8000/api/v1';

export interface TutorListing {
	id: string;
	teacher_id: string;
	subject_id: string;
	mode: 'ONLINE' | 'IN_PERSON' | 'HOME_VISIT' | 'FLEXIBLE';
	class_type: 'INDIVIDUAL' | 'GROUP';
	hourly_rate: number;
	description?: string;
	trial_available: boolean;
	trial_rate?: number;
	max_group_size?: number;
	status: 'ACTIVE' | 'INACTIVE' | 'EXPIRED';
}

export interface Tutor {
	id: string;
	full_name: string;
	profile_photo_url?: string;
	merit_score: number;
	average_rating?: number;
	review_count: number;
	listings: TutorListing[];
}

export interface TutorProfile extends Tutor {
	bio?: string;
	years_experience?: number;
	verification_status: string;
	city?: string;
}

export interface AvailabilitySlot {
	id: string;
	teacher_id: string;
	day_of_week: number;
	start_time: string;
	end_time: string;
	is_recurring: boolean;
}

export interface BlockedDate {
	id: string;
	teacher_id: string;
	blocked_date: string;
	reason?: string;
}

export interface Subject {
	id: string;
	name: string;
	category: string;
}

export interface TeacherProfileUpdate {
	bio?: string;
	years_experience?: number;
	document_urls?: string; // JSON string of document URLs
}

export interface TeacherProfileDetailResponse {
	id: string;
	user_id: string;
	bio?: string;
	years_experience?: number;
	document_urls?: string;
	verification_status: 'PENDING' | 'APPROVED' | 'REJECTED';
	verification_note?: string;
	listing_active: boolean;
}

export interface TutorSearchParams {
	subject_id?: string;
	city?: string;
	stream?: string;
	mode?: 'ONLINE' | 'IN_PERSON' | 'HOME_VISIT' | 'FLEXIBLE';
	min_rating?: number;
	max_price?: number;
	available_today?: boolean;
}

export interface CreateListingParams {
	subject_id: string;
	mode: 'ONLINE' | 'IN_PERSON' | 'HOME_VISIT' | 'FLEXIBLE';
	class_type: 'INDIVIDUAL' | 'GROUP';
	hourly_rate: number;
	description?: string;
	trial_available?: boolean;
	trial_rate?: number;
	max_group_size?: number;
}

export interface UpdateListingParams {
	mode?: 'ONLINE' | 'IN_PERSON' | 'HOME_VISIT' | 'FLEXIBLE';
	class_type?: 'INDIVIDUAL' | 'GROUP';
	hourly_rate?: number;
	description?: string;
	trial_available?: boolean;
	trial_rate?: number;
	max_group_size?: number;
}

export interface CreateAvailabilitySlotParams {
	day_of_week: number;
	start_time: string;
	end_time: string;
	is_recurring?: boolean;
}

export interface CreateBlockedDateParams {
	blocked_date: string;
	reason?: string;
}

// Public tutor search endpoints
export async function searchTutors(params: TutorSearchParams = {}): Promise<Tutor[]> {
	const queryParams = new URLSearchParams();
	
	if (params.subject_id) queryParams.append('subject_id', params.subject_id);
	if (params.city) queryParams.append('city', params.city);
	if (params.stream) queryParams.append('stream', params.stream);
	if (params.mode) queryParams.append('mode', params.mode);
	if (params.min_rating !== undefined) queryParams.append('min_rating', params.min_rating.toString());
	if (params.max_price !== undefined) queryParams.append('max_price', params.max_price.toString());
	if (params.available_today) queryParams.append('available_today', 'true');

	const queryString = queryParams.toString();
	const endpoint = queryString ? `/tutors?${queryString}` : '/tutors';
	
	return apiClient<Tutor[]>(endpoint);
}

export async function getTutorProfile(tutorId: string): Promise<TutorProfile> {
	return apiClient<TutorProfile>(`/tutors/${tutorId}/profile`);
}

export async function getTutorAvailability(tutorId: string, week?: string): Promise<AvailabilitySlot[]> {
	const queryParams = new URLSearchParams();
	if (week) queryParams.append('week', week);
	
	const queryString = queryParams.toString();
	const endpoint = queryString ? `/tutors/${tutorId}/availability?${queryString}` : `/tutors/${tutorId}/availability`;
	
	return apiClient<AvailabilitySlot[]>(endpoint);
}

export async function getTutorReviews(tutorId: string, page: number = 1, perPage: number = 10): Promise<{
	reviews: any[];
	total: number;
	page: number;
	per_page: number;
	average_rating: number;
}> {
	const queryParams = new URLSearchParams();
	queryParams.append('page', page.toString());
	queryParams.append('per_page', perPage.toString());
	
	return apiClient<any>(`/tutors/${tutorId}/reviews?${queryParams.toString()}`);
}

export async function getSubjects(): Promise<Subject[]> {
	return apiClient<Subject[]>('/tutors/subjects');
}

// Teacher listing management endpoints (require authentication)
export async function createListing(params: CreateListingParams): Promise<TutorListing> {
	return apiClient<TutorListing>('/tutors/listings', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(params),
	});
}

export async function getMyListings(): Promise<TutorListing[]> {
	return apiClient<TutorListing[]>('/tutors/my-listings');
}

export async function updateListing(listingId: string, params: UpdateListingParams): Promise<TutorListing> {
	return apiClient<TutorListing>(`/tutors/listings/${listingId}`, {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(params),
	});
}

export async function deleteListing(listingId: string): Promise<void> {
	return apiClient<void>(`/tutors/listings/${listingId}`, {
		method: 'DELETE',
	});
}

// Availability management endpoints (require authentication)
export async function createAvailabilitySlot(params: CreateAvailabilitySlotParams): Promise<AvailabilitySlot> {
	return apiClient<AvailabilitySlot>('/tutors/availability', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(params),
	});
}

export async function getMyAvailability(): Promise<AvailabilitySlot[]> {
	return apiClient<AvailabilitySlot[]>('/tutors/my-availability');
}

export async function deleteAvailabilitySlot(slotId: string): Promise<void> {
	return apiClient<void>(`/tutors/availability/${slotId}`, {
		method: 'DELETE',
	});
}

export async function createBlockedDate(params: CreateBlockedDateParams): Promise<{ message: string }> {
	return apiClient<{ message: string }>('/tutors/blocked-dates', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(params),
	});
}

export async function getMyBlockedDates(): Promise<BlockedDate[]> {
	return apiClient<BlockedDate[]>('/tutors/my-blocked-dates');
}

export async function deleteBlockedDate(blockedDateId: string): Promise<void> {
	return apiClient<void>(`/tutors/blocked-dates/${blockedDateId}`, {
		method: 'DELETE',
	});
}

// Teacher profile verification endpoints
export async function createOrUpdateTeacherProfile(params: TeacherProfileUpdate, userId?: string): Promise<TeacherProfileDetailResponse> {
	const queryParams = userId ? `?user_id=${userId}` : '';
	return apiClient<TeacherProfileDetailResponse>(`/tutors/profile${queryParams}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(params),
	});
}

export async function getMyTeacherProfile(): Promise<TeacherProfileDetailResponse> {
	return apiClient<TeacherProfileDetailResponse>('/tutors/profile/me');
}

export async function uploadDocument(file: File): Promise<{ url: string; filename: string }> {
	const formData = new FormData();
	formData.append('file', file);

	const response = await fetch(`${API_BASE_URL}/tutors/upload-document`, {
		method: 'POST',
		body: formData,
	});

	if (!response.ok) {
		const error = await response.json();
		throw new Error(error.detail || 'Failed to upload document');
	}

	return response.json();
}


