<script lang="ts">
	import type { Conversation } from '$lib/api/messages';
	import { formatRelativeTime } from '$lib/utils/dates';

	let { conversations, selectedConversationId, onSelectConversation } = $props<{
		conversations: Conversation[];
		selectedConversationId: string | null;
		onSelectConversation: (id: string) => void;
	}>();

	function getConversationName(conversation: Conversation): string {
		// In a real app, you'd fetch user names from the participant IDs
		// For now, return a placeholder
		return conversation.type.replace('_', ' ');
	}
</script>

<div class="conversation-list">
	<div class="conversation-list-header">
		<div style="font-size: 14px; font-weight: 700;">Messages</div>
	</div>

	<div class="conversation-list-body">
		{#if conversations.length === 0}
			<div class="no-conversations">
				<div style="font-size: 32px; margin-bottom: 12px;">💬</div>
				<div style="font-size: 13px; color: var(--muted-fg);">No conversations yet</div>
			</div>
		{:else}
			{#each conversations as conv}
				<div 
					class="conversation-item {selectedConversationId === conv.id ? 'active' : ''}" 
					onclick={() => onSelectConversation(conv.id)}
				>
					<div class="conversation-avatar">
						{getConversationName(conv).split(' ').map(n => n[0]).join('')}
					</div>
					<div class="conversation-info">
						<div class="conversation-name">{getConversationName(conv)}</div>
						<div class="conversation-time">{formatRelativeTime(conv.created_at)}</div>
					</div>
				</div>
			{/each}
		{/if}
	</div>
</div>

<style>
	.conversation-list {
		display: flex;
		flex-direction: column;
		height: 100%;
		background: white;
		border-right: 1px solid var(--border-dk);
		width: 300px;
		flex-shrink: 0;
	}

	.conversation-list-header {
		padding: 16px;
		border-bottom: 1px solid var(--border);
	}

	.conversation-list-body {
		flex: 1;
		overflow-y: auto;
	}

	.no-conversations {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100%;
		color: var(--muted-fg);
		padding: 20px;
	}

	.conversation-item {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 12px 16px;
		cursor: pointer;
		transition: background 0.15s;
		border-left: 3px solid transparent;
	}

	.conversation-item:hover {
		background: var(--muted);
	}

	.conversation-item.active {
		background: var(--saffron-lt);
		border-left-color: var(--saffron);
	}

	.conversation-avatar {
		width: 40px;
		height: 40px;
		border-radius: 50%;
		background: var(--primary);
		color: var(--saffron);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 14px;
		font-weight: 700;
		flex-shrink: 0;
	}

	.conversation-info {
		flex: 1;
		min-width: 0;
	}

	.conversation-name {
		font-size: 14px;
		font-weight: 600;
		margin-bottom: 2px;
	}

	.conversation-time {
		font-size: 12px;
		color: var(--muted-fg);
	}
</style>
