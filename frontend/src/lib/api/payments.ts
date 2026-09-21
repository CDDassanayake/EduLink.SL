import { apiClient } from './client';

export interface ListingPaymentRequest {
	listing_id: string;
	plan: 'BASIC' | 'STANDARD' | 'PREMIUM';
}

export interface ListingPaymentResponse {
	client_secret: string;
	payment_intent_id: string;
	amount: number;
}

export async function createListingPayment(params: ListingPaymentRequest): Promise<ListingPaymentResponse> {
	return apiClient<ListingPaymentResponse>('/payments/listing-checkout', {
		method: 'POST',
		body: JSON.stringify(params),
	});
}

export async function getPaymentHistory(): Promise<any[]> {
	return apiClient<any[]>('/payments/history');
}
