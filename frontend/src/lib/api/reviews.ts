import { apiClient } from './client';

export interface ReviewCreate {
	booking_id: string;
	rating: number; // 1 to 5
	comment?: string;
}

export interface Review {
	id: string;
	booking_id: string;
	student_id: string;
	teacher_id: string;
	rating: number;
	comment: string | null;
	is_visible: boolean;
	created_at: string;
}

export interface TeacherRating {
	average_rating: number | null;
	review_count: number;
}

export async function createReview(review: ReviewCreate): Promise<Review> {
	return apiClient<Review>('/reviews', {
		method: 'POST',
		body: JSON.stringify(review),
	});
}

export async function getTeacherReviews(teacherId: string): Promise<Review[]> {
	return apiClient<Review[]>(`/reviews/teacher/${teacherId}`);
}

export async function getTeacherAverageRating(teacherId: string): Promise<TeacherRating> {
	return apiClient<TeacherRating>(`/reviews/teacher/${teacherId}/average`);
}
