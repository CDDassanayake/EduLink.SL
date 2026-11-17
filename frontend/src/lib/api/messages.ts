import { apiClient } from './client';

export interface Conversation {
	id: string;
	type: 'STUDENT_TEACHER' | 'TEACHER_TEACHER' | 'STUDENT_STUDENT';
	participant_ids: string[];
	created_at: string;
}

export interface ConversationCreate {
	participant_ids: string[];
	type: 'STUDENT_TEACHER' | 'TEACHER_TEACHER' | 'STUDENT_STUDENT';
}

export interface Message {
	id: string;
	conversation_id: string;
	sender_id: string;
	content: string;
	read_at: string | null;
	created_at: string;
}

export interface WebSocketMessage {
	type: string;
	conversation_id?: string;
	content?: string;
	sender_id?: string;
	created_at?: string;
}

export async function getConversations(): Promise<Conversation[]> {
	return apiClient<Conversation[]>('/messages/conversations');
}

export async function createConversation(data: ConversationCreate): Promise<Conversation> {
	return apiClient<Conversation>('/messages/conversations', {
		method: 'POST',
		body: JSON.stringify(data),
	});
}

export async function getConversationMessages(conversationId: string): Promise<Message[]> {
	return apiClient<Message[]>(`/messages/conversations/${conversationId}/messages`);
}

export async function markConversationRead(conversationId: string): Promise<{ status: string; messages_marked_read: number }> {
	return apiClient<{ status: string; messages_marked_read: number }>(
		`/messages/conversations/${conversationId}/read`,
		{
			method: 'PATCH',
		}
	);
}
