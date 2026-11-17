import { apiClient } from './client';

export interface ChatRequest {
	message: string;
}

export interface ChatResponse {
	response: string;
}

export interface HistoryResponse {
	history: Array<{ role: string; content: string }>;
}

export async function sendChatMessage(message: string): Promise<ChatResponse> {
	return apiClient<ChatResponse>('/ai/chat', {
		method: 'POST',
		body: JSON.stringify({ message }),
	});
}

export async function getChatHistory(): Promise<HistoryResponse> {
	return apiClient<HistoryResponse>('/ai/chat/history');
}

export async function clearChatHistory(): Promise<{ status: string; message: string }> {
	return apiClient<{ status: string; message: string }>('/ai/chat/history', {
		method: 'DELETE',
	});
}
