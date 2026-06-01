export type UserRole = 'STUDENT' | 'TEACHER' | 'ADMIN';

export interface User {
	id: string;
	email: string;
	full_name: string;
	role: UserRole;
	city?: string;
	phone?: string;
	profile_photo_url?: string;
	merit_score: number;
	is_verified: boolean;
	teacher_verification_status?: 'PENDING' | 'APPROVED' | 'REJECTED';
	created_at: string;
	updated_at: string;
}

export interface TutorListing {
	id: string;
	teacher_id: string;
	subject_id: string;
	subject_name: string;
	mode: 'ONLINE' | 'IN_PERSON' | 'HOME_VISIT' | 'FLEXIBLE';
	class_type: 'INDIVIDUAL' | 'GROUP';
	hourly_rate: number;
	description: string;
	trial_available: boolean;
	trial_rate?: number;
	max_group_size?: number;
	status: 'ACTIVE' | 'INACTIVE' | 'EXPIRED';
	expires_at?: string;
	teacher: {
		full_name: string;
		merit_score: number;
		average_rating: number;
		review_count: number;
		city: string;
		profile_photo_url?: string;
	};
}

export interface Booking {
	id: string;
	student_id: string;
	teacher_id: string;
	listing_id: string;
	session_start: string;
	session_end: string;
	booking_type: 'SINGLE' | 'MONTHLY';
	package_weeks?: number;
	status: 'PENDING' | 'CONFIRMED' | 'ATTENDED' | 'CANCELLED' | 'DISPUTED';
	cancelled_by?: string;
	cancel_reason?: string;
	cancelled_at?: string;
	can_review: boolean;
	created_at: string;
	teacher: {
		full_name: string;
		subject: string;
	};
}

export interface Message {
	id: string;
	conversation_id: string;
	sender_id: string;
	content: string;
	read_at?: string;
	created_at: string;
	sender: {
		full_name: string;
	};
}

export interface Conversation {
	id: string;
	type: 'STUDENT_TEACHER' | 'TEACHER_TEACHER' | 'STUDENT_STUDENT';
	participant_ids: string[];
	other_user: {
		id: string;
		full_name: string;
		profile_photo_url?: string;
	};
	last_message?: Message;
	unread_count: number;
	created_at: string;
}
