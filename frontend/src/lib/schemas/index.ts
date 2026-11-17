import { z } from 'zod';

// Auth schemas
export const loginSchema = z.object({
	email: z.string().email('Invalid email address'),
	password: z.string().min(6, 'Password must be at least 6 characters')
});

export const registerSchema = z.object({
	email: z.string().email('Invalid email address'),
	password: z.string().min(6, 'Password must be at least 6 characters'),
	full_name: z.string().min(2, 'Full name must be at least 2 characters'),
	role: z.enum(['STUDENT', 'TEACHER']),
	city: z.string().min(2, 'City must be at least 2 characters'),
	phone: z.string().min(10, 'Phone number must be at least 10 characters')
});

// Tutor schemas
export const teacherProfileSchema = z.object({
	bio: z.string().min(10, 'Bio must be at least 10 characters').optional(),
	years_experience: z.number().min(0).optional(),
	document_urls: z.string().optional(),
	subjects: z.array(z.string()).optional()
});

export const listingSchema = z.object({
	subject_id: z.string(),
	mode: z.enum(['ONLINE', 'IN_PERSON', 'HOME_VISIT', 'FLEXIBLE']),
	class_type: z.enum(['INDIVIDUAL', 'GROUP']),
	hourly_rate: z.number().min(100, 'Hourly rate must be at least LKR 100'),
	description: z.string().min(10, 'Description must be at least 10 characters'),
	trial_available: z.boolean().optional(),
	trial_rate: z.number().optional(),
	max_group_size: z.number().optional()
});

// Booking schemas
export const bookingSchema = z.object({
	tutor_id: z.string(),
	listing_id: z.string(),
	session_start: z.string(),
	session_end: z.string(),
	booking_type: z.enum(['SINGLE', 'MONTHLY']),
	package_weeks: z.number().optional()
});

// Review schemas
export const reviewSchema = z.object({
	booking_id: z.string(),
	rating: z.number().min(1).max(5, 'Rating must be between 1 and 5'),
	comment: z.string().optional()
});

// Message schemas
export const messageSchema = z.object({
	conversation_id: z.string(),
	content: z.string().min(1, 'Message cannot be empty')
});

export const conversationSchema = z.object({
	participant_ids: z.array(z.string()).min(2).max(2),
	type: z.enum(['STUDENT_TEACHER', 'TEACHER_TEACHER', 'STUDENT_STUDENT'])
});

// AI Chat schemas
export const chatSchema = z.object({
	message: z.string().min(1, 'Message cannot be empty')
});

export type LoginInput = z.infer<typeof loginSchema>;
export type RegisterInput = z.infer<typeof registerSchema>;
export type TeacherProfileInput = z.infer<typeof teacherProfileSchema>;
export type ListingInput = z.infer<typeof listingSchema>;
export type BookingInput = z.infer<typeof bookingSchema>;
export type ReviewInput = z.infer<typeof reviewSchema>;
export type MessageInput = z.infer<typeof messageSchema>;
export type ConversationInput = z.infer<typeof conversationSchema>;
export type ChatInput = z.infer<typeof chatSchema>;
