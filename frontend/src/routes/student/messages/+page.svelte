<script lang="ts">
	let messageInput = $state('');

	function sendMessage() {
		if (!messageInput.trim()) return;
		const body = document.querySelector('.chat-body');
		if (!body) return;
		const msg = document.createElement('div');
		msg.className = 'chat-msg me';
		msg.innerHTML = `<div class="chat-bubble">${messageInput}</div><div class="chat-timestamp">Just now</div>`;
		body.appendChild(msg);
		body.scrollTop = body.scrollHeight;
		messageInput = '';
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Enter') sendMessage();
	}
</script>

<svelte:head>
	<title>Messages — EduLink SL</title>
</svelte:head>

<div class="app-topbar">
	<div class="app-topbar-title">Messages</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i><div class="notif-dot"></div></div>
	</div>
</div>

<div style="padding: 20px">
	<div class="msg-layout">
		<!-- Conversation list -->
		<div class="msg-list">
			<div class="msg-list-hdr" style="display: flex; align-items: center; justify-content: space-between">
				<span>Conversations</span>
				<span style="font-size: 11px; font-family: var(--ff-mono); background: var(--saffron); color: #fff; padding: 2px 7px; border-radius: 100px; font-weight: 700">2 new</span>
			</div>
			<div class="conv-item active">
				<div style="width: 36px; height: 36px; border-radius: 50%; background: #EEF2FF; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; color: #3B4FD8; flex-shrink: 0">AP</div>
				<div class="conv-body">
					<div class="conv-name">Aruna Perera <span class="conv-time">2m</span></div>
					<div class="conv-preview">See you at 9 AM tomorrow. Please review chapter 12 on waves...</div>
				</div>
				<div class="conv-unread">1</div>
			</div>
			<div class="conv-item">
				<div style="width: 36px; height: 36px; border-radius: 50%; background: #FFF0E0; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; color: #A06000; flex-shrink: 0">DJ</div>
				<div class="conv-body">
					<div class="conv-name">Dilini Jayasuriya <span class="conv-time">1h</span></div>
					<div class="conv-preview">Do you have any specific topics for Wednesday's session?</div>
				</div>
				<div class="conv-unread">1</div>
			</div>
			<div class="conv-item">
				<div style="width: 36px; height: 36px; border-radius: 50%; background: #F0FDF4; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; color: #166534; flex-shrink: 0">RS</div>
				<div class="conv-body">
					<div class="conv-name">Dr. Rohan Silva <span class="conv-time">2d</span></div>
					<div class="conv-preview">Great work on the last past paper. Keep it up!</div>
				</div>
			</div>
		</div>

		<!-- Active chat -->
		<div class="chat-area">
			<div class="chat-hdr">
				<div style="width: 36px; height: 36px; border-radius: 50%; background: #EEF2FF; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800; color: #3B4FD8; flex-shrink: 0">AP</div>
				<div style="flex: 1">
					<div style="font-size: 13px; font-weight: 700">Aruna Perera</div>
					<div style="font-size: 11px; color: var(--muted-fg); display: flex; align-items: center; gap: 5px"><span style="width: 7px; height: 7px; background: var(--green); border-radius: 50%; display: inline-block"></span>Online · Physics tutor</div>
				</div>
				<a href="/find-tutors" class="btn btn-ghost btn-sm">View profile</a>
			</div>

			<div class="chat-body">
				<div class="chat-msg them">
					<div class="chat-bubble">Hi Kasun! Your session tomorrow is confirmed for 9 AM. We'll be covering electromagnetic induction — quite a big topic for the exam.</div>
					<div class="chat-timestamp">Yesterday, 6:14 PM</div>
				</div>
				<div class="chat-msg me">
					<div class="chat-bubble">Thank you! I've been going through the textbook. I'm a bit confused about Faraday's law and how to apply it in problems.</div>
					<div class="chat-timestamp">Yesterday, 6:22 PM</div>
				</div>
				<div class="chat-msg them">
					<div class="chat-bubble">That's very common. We'll work through it step by step tomorrow with plenty of examples. The key is understanding flux change — once that clicks, the rest follows naturally.</div>
					<div class="chat-timestamp">Yesterday, 6:30 PM</div>
				</div>
				<div class="chat-msg me">
					<div class="chat-bubble">Perfect, I'll make a note of the specific problems I'm stuck on and bring them to the session.</div>
					<div class="chat-timestamp">Yesterday, 6:35 PM</div>
				</div>
				<div class="chat-msg them">
					<div class="chat-bubble">See you at 9 AM tomorrow. Please review chapter 12 on waves briefly — we might touch on it as well if time allows.</div>
					<div class="chat-timestamp">2 minutes ago</div>
				</div>
			</div>

			<div class="chat-footer">
				<button class="btn btn-ghost btn-icon btn-sm"><i class="ti ti-paperclip"></i></button>
				<input class="chat-input" placeholder="Type a message..." bind:value={messageInput} onkeydown={handleKeydown} />
				<button class="btn btn-primary btn-icon btn-sm" onclick={sendMessage}><i class="ti ti-send"></i></button>
			</div>
		</div>
	</div>
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
		position: relative;
	}
	.notif-btn:hover {
		border-color: var(--saffron);
		color: var(--saffron);
	}
	.notif-dot {
		position: absolute;
		top: 8px;
		right: 8px;
		width: 8px;
		height: 8px;
		background: var(--saffron);
		border-radius: 50%;
	}
</style>
