<script lang="ts">
	let messageInput = $state('');
	let messages = $state([
		{ id: 1, sender: 'them', text: 'Hi Mr. Aruna! I\'ve been going through the electromagnetic induction chapter. I\'m struggling a bit with how to determine the direction of induced current in different configurations.', time: 'Yesterday, 8:05 PM' },
		{ id: 2, sender: 'me', text: 'That\'s a great question Kasun! The key is to always apply Lenz\'s law first — the induced current always opposes the change in flux. I\'ll prepare a diagram showing the standard configurations for tomorrow\'s session.', time: 'Yesterday, 8:18 PM' },
		{ id: 3, sender: 'them', text: 'Thank you! Also, I\'m confused about Faraday\'s law when the area is changing vs the magnetic field changing. Are the formulas different?', time: '5 minutes ago' },
		{ id: 4, sender: 'them', text: 'I found a past paper question from 2019 that I can\'t solve — should I bring it tomorrow?', time: '2 minutes ago' }
	]);

	function sendMessage() {
		if (!messageInput.trim()) return;
		messages = [...messages, { id: messages.length + 1, sender: 'me', text: messageInput, time: 'Just now' }];
		messageInput = '';
	}
</script>

<svelte:head>
	<title>Messages — EduLink SL</title>
</svelte:head>

<div class="app-topbar">
	<div class="app-topbar-title">Messages</div>
	<div class="app-topbar-right"><div class="notif-btn"><i class="ti ti-bell"></i><div class="notif-dot"></div></div></div>
</div>

<div style="padding:20px">
	<div class="msg-layout">
		<div class="msg-list">
			<div class="msg-list-hdr" style="display:flex;align-items:center;justify-content:space-between">
				<span>Messages</span>
				<span style="font-size:11px;font-family:var(--ff-mono);background:var(--saffron);color:#fff;padding:2px 7px;border-radius:100px;font-weight:700">3 new</span>
			</div>

			<div class="conv-item active">
				<div style="width:36px;height:36px;border-radius:50%;background:#EEF2FF;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#3B4FD8;flex-shrink:0">KJ</div>
				<div class="conv-body">
					<div class="conv-name">Kasun Jayasuriya<span class="conv-time">5m</span></div>
					<div class="conv-preview">I'm confused about Faraday's law in problems...</div>
				</div>
				<div class="conv-unread">2</div>
			</div>

			<div class="conv-item">
				<div style="width:36px;height:36px;border-radius:50%;background:#FDF4FF;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#7C3AED;flex-shrink:0">NW</div>
				<div class="conv-body">
					<div class="conv-name">Nadia Wickramasinghe<span class="conv-time">1h</span></div>
					<div class="conv-preview">Can we reschedule Friday's session to Saturday?</div>
				</div>
				<div class="conv-unread">1</div>
			</div>

			<div class="conv-item">
				<div style="width:36px;height:36px;border-radius:50%;background:#F0FDF4;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#166534;flex-shrink:0">TB</div>
				<div class="conv-body">
					<div class="conv-name">Tharaka Bandara<span class="conv-time">3h</span></div>
					<div class="conv-preview">Thank you for the notes, really helpful!</div>
				</div>
			</div>

			<div class="conv-item">
				<div style="width:36px;height:36px;border-radius:50%;background:#FFF0E0;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#A06000;flex-shrink:0">SP</div>
				<div class="conv-body">
					<div class="conv-name">Sanduni Peiris<span class="conv-time">Yesterday</span></div>
					<div class="conv-preview">What topics will we cover next session?</div>
				</div>
			</div>

			<div class="conv-item">
				<div style="width:36px;height:36px;border-radius:50%;background:#F0F9FF;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#0891B2;flex-shrink:0">RA</div>
				<div class="conv-body">
					<div class="conv-name">Ruwini Alahakoon<span class="conv-time">2d</span></div>
					<div class="conv-preview">I scored 78% on the past paper — thanks!</div>
				</div>
			</div>
		</div>

		<div class="chat-area">
			<div class="chat-hdr">
				<div style="width:36px;height:36px;border-radius:50%;background:#EEF2FF;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#3B4FD8;flex-shrink:0">KJ</div>
				<div style="flex:1">
					<div style="font-size:13px;font-weight:700">Kasun Jayasuriya</div>
					<div style="font-size:11px;color:var(--muted-fg);display:flex;align-items:center;gap:5px">
						<span style="width:7px;height:7px;background:var(--green);border-radius:50%;display:inline-block"></span>
						Online · A/L Physics student · Session on Tue 24 Jun
					</div>
				</div>
				<a href="/teacher/schedule" class="btn btn-ghost btn-sm"><i class="ti ti-calendar"></i> View booking</a>
			</div>

			<div class="chat-body">
				{#each messages as msg}
					<div class="chat-msg {msg.sender}">
						<div class="chat-bubble">{msg.text}</div>
						<div class="chat-timestamp">{msg.time}</div>
					</div>
				{/each}
			</div>

			<div class="chat-footer">
				<button class="btn btn-ghost btn-icon btn-sm"><i class="ti ti-paperclip"></i></button>
				<input class="chat-input" placeholder="Reply to Kasun..." bind:value={messageInput} onkeydown={(e) => e.key === 'Enter' && sendMessage()}>
				<button class="btn btn-primary btn-icon btn-sm" onclick={sendMessage}><i class="ti ti-send"></i></button>
			</div>
		</div>
	</div>
</div>
