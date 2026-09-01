import { apiClient } from './client';
import type { TutorListing } from './tutors';

// Admin listing approval endpoints
export async function getPendingListings(): Promise<TutorListing[]> {
	return apiClient<TutorListing[]>('/admin/listings/pending');
}

export async function approveListing(listingId: string): Promise<TutorListing> {
	return apiClient<TutorListing>(`/admin/listings/${listingId}/approve`, {
		method: 'PATCH',
	});
}

export async function rejectListing(listingId: string): Promise<void> {
	return apiClient<void>(`/admin/listings/${listingId}/reject`, {
		method: 'PATCH',
	});
}
