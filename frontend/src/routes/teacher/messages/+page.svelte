<script lang="ts">
	import { getConversations, createConversation, getConversationMessages, markConversationRead, type Conversation, type Message } from '$lib/api/messages';
	import ConversationList from '$lib/components/ConversationList.svelte';
	import ChatWindow from '$lib/components/ChatWindow.svelte';
	import { getAuthStore } from '$lib/stores/auth.svelte';
	import { getWebSocketStore } from '$lib/stores/websocket.svelte';
	import type { WebSocketMessage } from '$lib/api/messages';

	let authStore = getAuthStore();
	let wsStore = getWebSocketStore();
	
	let conversations = $state<Conversation[]>([]);
	let selectedConversationId = $state<string | null>(null);
	let messages = $state<Message[]>([]);
	let isLoading = $state(false);
	let error = $state('');

	async function loadConversations() {
		isLoading = true;
		error = '';
		try {
			conversations = await getConversations();
		} catch (e: any) {
			error = e.message || 'Failed to load conversations';
		} finally {
			isLoading = false;
		}
	}

	async function selectConversation(conversationId: string) {
		selectedConversationId = conversationId;
		await loadMessages(conversationId);
		await markConversationRead(conversationId);
	}

	async function loadMessages(conversationId: string) {
		isLoading = true;
		error = '';
		try {
			messages = await getConversationMessages(conversationId);
		} catch (e: any) {
			error = e.message || 'Failed to load messages';
		} finally {
			isLoading = false;
		}
	}

	async function handleSendMessage(content: string) {
		if (!selectedConversationId) return;
		
		wsStore.sendMessage({
			type: 'message',
			conversation_id: selectedConversationId,
			content
		} as WebSocketMessage);

		const tempMessage: Message = {
			id: 'temp',
			conversation_id: selectedConversationId,
			sender_id: authStore.user?.id || '',
			content,
			read_at: null,
			created_at: new Date().toISOString()
		};
		messages = [...messages, tempMessage];
	}

	async function startNewConversation(participantId: string) {
		try {
			const conv = await createConversation({
				participant_ids: [authStore.user?.id || '', participantId],
				type: 'STUDENT_TEACHER'
			});
			await loadConversations();
			selectConversation(conv.id);
		} catch (e: any) {
			error = e.message || 'Failed to create conversation';
		}
	}

	$effect(() => {
		if (authStore.user) {
			wsStore.connect(authStore.user.id);
			loadConversations();
		}
		return () => {
			wsStore.disconnect();
		};
	});

	$effect(() => {
		const unsubscribe = wsStore.onMessage((message: WebSocketMessage) => {
			if (message.type === 'message' && message.conversation_id === selectedConversationId) {
				messages = [...messages, {
					id: message.id || 'ws-' + Date.now(),
					conversation_id: message.conversation_id || '',
					sender_id: message.sender_id || '',
					content: message.content || '',
					read_at: null,
					created_at: message.created_at || new Date().toISOString()
				}];
			}
		});
		return unsubscribe;
	});
</script>

<svelte:head>
	<title>Messages — EduLink SL</title>
</svelte:head>

<div class="app-topbar">
	<div class="app-topbar-title">Messages</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i></div>
	</div>
</div>

<div class="messages-layout">
	<ConversationList
		conversations={conversations}
		selectedConversationId={selectedConversationId}
		onSelectConversation={selectConversation}
	/>

	{#if selectedConversationId}
		<ChatWindow
			messages={messages}
			onSendMessage={handleSendMessage}
			currentUserId={authStore.user?.id || ''}
		/>
	{:else}
		<div class="no-conversation-selected">
			<div style="font-size: 32px; margin-bottom: 12px;">💬</div>
			<div style="font-size: 14px; color: var(--muted-fg);">Select a conversation to start messaging</div>
		</div>
	{/if}
</div>

<style>
	.app-topbar {
		background: #fff;
		border-bottom: 1px solid var(--border-dk);
		padding: 16px 24px;
		display: flex;
		align-items: center;
		justify-content: space-between;
	}
	.app-topbar-title {
		font-size: 18px;
		font-weight: 700;
	}
	.app-topbar-right {
		display: flex;
		align-items: center;
		gap: 12px;
	}
	.notif-btn {
		width: 36px;
		height: 36px;
		border-radius: 50%;
		border: 1.5px solid var(--border-dk);
		background: #fff;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 18px;
		color: var(--muted-fg);
		cursor: pointer;
		transition: all 0.15s;
	}
	.notif-btn:hover {
		border-color: var(--saffron);
		color: var(--saffron);
	}
	.messages-layout {
		display: flex;
		height: calc(100vh - 56px);
	}
	.no-conversation-selected {
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background: #FDFCF9;
		color: var(--muted-fg);
	}
</style>
