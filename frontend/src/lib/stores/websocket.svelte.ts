import type { WebSocketMessage } from '$lib/api/messages';

let ws: WebSocket | null = null;
let reconnectTimer: number | null = null;
let messageHandlers: Set<(message: WebSocketMessage) => void> = new Set();
let connectionStatus = $state<'disconnected' | 'connecting' | 'connected'>('disconnected');
let currentUserId: string | null = null;

const API_BASE_URL = 'http://localhost:8000/api/v1';

export function getWebSocketStore() {
	return {
		get connectionStatus() {
			return connectionStatus;
		},
		
		get isConnected() {
			return connectionStatus === 'connected';
		},

		connect(userId: string) {
			if (ws?.readyState === WebSocket.OPEN) {
				return;
			}

			currentUserId = userId;
			connectionStatus = 'connecting';

			// Get access token from localStorage
			const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
			
			if (!token) {
				console.error('No access token found for WebSocket connection');
				connectionStatus = 'disconnected';
				return;
			}

			try {
				ws = new WebSocket(`${API_BASE_URL.replace('http', 'ws')}/messages/ws/chat?token=${token}`);

				ws.onopen = () => {
					console.log('WebSocket connected');
					connectionStatus = 'connected';
					if (reconnectTimer) {
						clearTimeout(reconnectTimer);
						reconnectTimer = null;
					}
				};

				ws.onmessage = (event) => {
					try {
						const message: WebSocketMessage = JSON.parse(event.data);
						messageHandlers.forEach(handler => handler(message));
					} catch (e) {
						console.error('Error parsing WebSocket message:', e);
					}
				};

				ws.onerror = (error) => {
					console.error('WebSocket error:', error);
					connectionStatus = 'disconnected';
				};

				ws.onclose = () => {
					console.log('WebSocket disconnected');
					connectionStatus = 'disconnected';
					// Attempt to reconnect after 5 seconds
					if (currentUserId) {
						reconnectTimer = window.setTimeout(() => {
							this.connect(currentUserId!);
						}, 5000);
					}
				};
			} catch (e) {
				console.error('Error creating WebSocket connection:', e);
				connectionStatus = 'disconnected';
			}
		},

		disconnect() {
			if (reconnectTimer) {
				clearTimeout(reconnectTimer);
				reconnectTimer = null;
			}
			if (ws) {
				ws.close();
				ws = null;
			}
			connectionStatus = 'disconnected';
			currentUserId = null;
		},

		sendMessage(message: WebSocketMessage) {
			if (ws?.readyState === WebSocket.OPEN) {
				ws.send(JSON.stringify(message));
			} else {
				console.error('WebSocket not connected');
			}
		},

		onMessage(handler: (message: WebSocketMessage) => void) {
			messageHandlers.add(handler);
			return () => {
				messageHandlers.delete(handler);
			};
		}
	};
}
