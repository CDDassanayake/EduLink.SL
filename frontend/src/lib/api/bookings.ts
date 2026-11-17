import { apiClient } from './client';

export interface BookingCreate {
	tutor_id: string;
	listing_id: string;
	session_start: string;
	session_end: string;
	booking_type: 'SINGLE' | 'MONTHLY';
	package_weeks?: number;
}

export interface Booking {
	id: string;
	student_id: string;
	teacher_id: string;
	listing_id: string;
	session_start: string;
	session_end: string;
	booking_type: 'SINGLE' | 'MONTHLY';
	package_weeks: number | null;
	status: 'PENDING' | 'CONFIRMED' | 'ATTENDED' | 'CANCELLED' | 'DISPUTED';
	cancelled_by: string | null;
	cancel_reason: string | null;
	cancelled_at: string | null;
	can_review: boolean;
	created_at: string;
}

export interface BookingCancel {
	reason?: string;
}

export async function createBooking(booking: BookingCreate): Promise<Booking> {
	return apiClient<Booking>('/bookings', {
		method: 'POST',
		body: JSON.stringify(booking),
	});
}

export async function getBookings(): Promise<Booking[]> {
	return apiClient<Booking[]>('/bookings');
}

export async function getBooking(bookingId: string): Promise<Booking> {
	return apiClient<Booking>(`/bookings/${bookingId}`);
}

export async function cancelBooking(bookingId: string, data: BookingCancel): Promise<Booking> {
	return apiClient<Booking>(`/bookings/${bookingId}/cancel`, {
		method: 'PATCH',
		body: JSON.stringify(data),
	});
}

export async function markBookingAttended(bookingId: string): Promise<Booking> {
	return apiClient<Booking>(`/bookings/${bookingId}/attend`, {
		method: 'PATCH',
	});
}
