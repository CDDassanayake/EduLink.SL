<script lang="ts">
	import type { Message } from '$lib/api/messages';

	let { messages, onSendMessage, currentUserId } = $props<{
		messages: Message[];
		onSendMessage: (content: string) => void;
		currentUserId: string;
	}>();

	let messageInput = $state('');

	async function sendMessage() {
		if (!messageInput.trim()) return;
		await onSendMessage(messageInput);
		messageInput = '';
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Enter' && !e.shiftKey) {
			e.preventDefault();
			sendMessage();
		}
	}

	function scrollToBottom() {
		const container = document.getElementById('chat-messages');
		if (container) {
			container.scrollTop = container.scrollHeight;
		}
	}

	// Auto-scroll when messages change
	$effect(() => {
		scrollToBottom();
	});
</script>

<div class="chat-window">
	<div class="chat-messages" id="chat-messages">
		{#if messages.length === 0}
			<div class="chat-empty">
				<div style="font-size: 32px; margin-bottom: 12px;">💬</div>
				<div style="font-size: 14px; color: var(--muted-fg);">Start a conversation by sending a message</div>
			</div>
		{/if}

		{#each messages as msg}
			<div class="chat-message {msg.sender_id === currentUserId ? 'sent' : 'received'}">
				<div class="chat-bubble">
					<div class="chat-content">{msg.content}</div>
					<div class="chat-time">
						{new Date(msg.created_at).toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' })}
					</div>
				</div>
			</div>
		{/each}
	</div>

	<div class="chat-input-area">
		<textarea 
			class="chat-input" 
			placeholder="Type a message..." 
			bind:value={messageInput}
			onkeydown={handleKeydown}
			rows="1"
		></textarea>
		<button 
			class="chat-send-btn" 
			onclick={sendMessage}
			disabled={!messageInput.trim()}
		>
			<i class="ti ti-send"></i>
		</button>
	</div>
</div>

<style>
	.chat-window {
		display: flex;
		flex-direction: column;
		height: 100%;
		background: #FDFCF9;
	}

	.chat-messages {
		flex: 1;
		overflow-y: auto;
		padding: 20px;
		display: flex;
		flex-direction: column;
		gap: 12px;
	}

	.chat-empty {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100%;
		color: var(--muted-fg);
	}

	.chat-message {
		display: flex;
		max-width: 70%;
	}

	.chat-message.sent {
		align-self: flex-end;
	}

	.chat-message.received {
		align-self: flex-start;
	}

	.chat-bubble {
		padding: 12px 16px;
		border-radius: 16px;
		box-shadow: var(--sh-xs);
	}

	.chat-message.sent .chat-bubble {
		background: var(--primary);
		color: white;
		border-radius: 16px 16px 4px 16px;
	}

	.chat-message.received .chat-bubble {
		background: white;
		border: 1px solid var(--border-dk);
		border-radius: 16px 16px 16px 4px;
	}

	.chat-content {
		font-size: 14px;
		line-height: 1.5;
		word-wrap: break-word;
	}

	.chat-time {
		font-size: 11px;
		margin-top: 4px;
		opacity: 0.7;
	}

	.chat-message.sent .chat-time {
		text-align: right;
	}

	.chat-input-area {
		display: flex;
		gap: 8px;
		padding: 16px;
		background: white;
		border-top: 1px solid var(--border-dk);
	}

	.chat-input {
		flex: 1;
		padding: 10px 14px;
		border: 1.5px solid var(--border-dk);
		border-radius: 20px;
		font-family: var(--ff);
		font-size: 14px;
		resize: none;
		min-height: 40px;
		max-height: 120px;
		transition: border-color 0.15s;
	}

	.chat-input:focus {
		outline: none;
		border-color: var(--saffron);
	}

	.chat-send-btn {
		width: 40px;
		height: 40px;
		border-radius: 50%;
		background: var(--primary);
		color: white;
		border: none;
		cursor: pointer;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 16px;
		transition: all 0.15s;
		flex-shrink: 0;
	}

	.chat-send-btn:hover:not(:disabled) {
		background: var(--saffron);
	}

	.chat-send-btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}
</style>
