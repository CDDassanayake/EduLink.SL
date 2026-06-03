<script lang="ts">
	let aiInput = $state('');
	let messages = $state([
		{ role: 'ai', text: 'Hello Kasun! I\'m your AI Career Guide, trained on the Sri Lankan curriculum and university entrance requirements. I can help you choose A/L subjects, understand university pathways, find the right tutors, or plan your study schedule. What would you like to explore today?' },
		{ role: 'user', text: 'What careers can I pursue with A/L Physical Science stream?' },
		{ role: 'ai', text: 'With A/L Physical Science (Maths, Physics, Chemistry/ICT), you have excellent options in Sri Lanka:<br><br><strong>🎓 Engineering</strong> — University of Moratuwa (most competitive), University of Peradeniya, SLIIT. High z-score required.<br><br><strong>💻 Information Technology</strong> — BSc IT at UoM or SLIIT. Great choice if you enjoy programming.<br><br><strong>⚗️ Physical Sciences / Research</strong> — University of Colombo, Peradeniya. Good path into academia or R&D.<br><br><strong>🏗️ Architecture</strong> — UoM or SLIDA. Combines technical + creative skills.<br><br><strong>📡 Telecommunications</strong> — Growing sector in SL, especially with 5G expansion.<br><br>What are your strengths — do you prefer Maths-heavy paths or more creative/applied fields?' },
		{ role: 'user', text: 'I\'m interested in IT. What z-score do I need for UoM BSc IT?' },
		{ role: 'ai', text: 'For <strong>UoM BSc (Hons) IT</strong> (Physical Science stream), you typically need:<br><br>• <strong>Z-score: 1.8 – 2.2+</strong> (varies by year, very competitive)<br>• <strong>2025 cutoff</strong> was approximately 1.95 for district merit<br>• Minimum: 3 passes with at least a C in Combined Maths or ICT<br><br><strong>Tips to improve your z-score:</strong><br>1. Focus heavily on Combined Maths — it has the highest weighting<br>2. Book a verified tutor for past paper practice (Dr. Rohan Silva on EduLink has a 99 merit score)<br>3. Aim for A grades in all 3 subjects<br><br>Would you like me to suggest the best tutors on EduLink for Combined Maths in your district?' }
	]);

	function useChip(text: string) {
		aiInput = text;
	}

	function sendAI() {
		if (!aiInput.trim()) return;
		messages = [...messages, { role: 'user', text: aiInput }];
		const tempId = messages.length;
		messages = [...messages, { role: 'ai', text: 'Thinking...', isThinking: true }];
		aiInput = '';
		
		setTimeout(() => {
			messages = messages.map((msg, i) => 
				i === tempId + 1 
					? { role: 'ai', text: 'That\'s a great question! Based on the Sri Lankan curriculum and current university requirements, I\'d recommend focusing on your core A/L subjects first. Would you like more specific guidance on tutors or study resources available on EduLink SL?' }
					: msg
			);
		}, 1500);
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Enter') sendAI();
	}
</script>

<svelte:head>
	<title>AI Career Chat — EduLink SL</title>
</svelte:head>

<div class="app-topbar">
	<div class="app-topbar-title">AI Career Guide</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i></div>
	</div>
</div>

<div class="ai-layout">
	<!-- History sidebar -->
	<div class="ai-sidebar">
		<div class="ai-sidebar-hdr">
			<button class="btn btn-primary btn-full btn-sm"><i class="ti ti-plus"></i> New conversation</button>
		</div>
		<div style="overflow-y: auto; flex: 1">
			<div class="ai-hist-section">Today</div>
			<div class="ai-hist-item active">Career paths with A/L Science</div>
			<div class="ai-hist-item">Best tutors for Combined Maths</div>
			<div class="ai-hist-section">This week</div>
			<div class="ai-hist-item">UoM vs SLIIT entrance requirements</div>
			<div class="ai-hist-item">Improving Physics z-score</div>
			<div class="ai-hist-item">How to study for A/L exams</div>
			<div class="ai-hist-section">Earlier</div>
			<div class="ai-hist-item">Which subjects for software engineering</div>
			<div class="ai-hist-item">Scholarship opportunities in SL</div>
		</div>
	</div>

	<!-- Chat area -->
	<div class="ai-main">
		<div class="ai-topbar">
			<div class="ai-icon"><i class="ti ti-sparkles"></i></div>
			<div>
				<div style="font-size: 13px; font-weight: 700">EduLink AI Career Guide</div>
				<div style="font-size: 11px; color: var(--muted-fg)">Powered by OpenAI · Sri Lanka curriculum context</div>
			</div>
			<button class="btn btn-ghost btn-sm" style="margin-left: auto"><i class="ti ti-trash"></i> Clear</button>
		</div>

		<div class="ai-messages">
			{#each messages as msg}
				<div class="ai-msg {msg.role}">
					{#if msg.role === 'ai'}
						<div class="ai-icon-sm"><i class="ti ti-sparkles"></i></div>
					{/if}
					<div class="ai-msg-bubble" class:thinking={msg.isThinking}>{@html msg.text}</div>
				</div>
			{/each}
		</div>

		<!-- Suggestion chips -->
		<div class="ai-chips-bar">
			<div class="ai-chip" onclick={() => useChip('Which tutors for Combined Maths?')}>Which tutors for Combined Maths?</div>
			<div class="ai-chip" onclick={() => useChip('How to improve my z-score?')}>How to improve my z-score?</div>
			<div class="ai-chip" onclick={() => useChip('UoM vs SLIIT — which is better?')}>UoM vs SLIIT — which is better?</div>
			<div class="ai-chip" onclick={() => useChip('Scholarship opportunities in Sri Lanka')}>Scholarship opportunities in Sri Lanka</div>
			<div class="ai-chip" onclick={() => useChip('Create a study plan for A/L')}>Create a study plan for A/L</div>
		</div>

		<!-- Input -->
		<div class="ai-input-bar">
			<input class="ai-input" placeholder="Ask about careers, universities, subjects, tutors..." bind:value={aiInput} onkeydown={handleKeydown} />
			<button class="btn btn-primary btn-icon" onclick={sendAI}><i class="ti ti-send"></i></button>
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
	}
	.notif-btn:hover {
		border-color: var(--saffron);
		color: var(--saffron);
	}
	.ai-layout {
		display: grid;
		grid-template-columns: 220px 1fr;
		height: calc(100vh - 56px);
		overflow: hidden;
	}
	.ai-sidebar {
		background: #fff;
		border-right: 1px solid var(--border-dk);
		display: flex;
		flex-direction: column;
		overflow: hidden;
	}
	.ai-sidebar-hdr {
		padding: 16px;
		border-bottom: 1px solid var(--border);
	}
	.ai-hist-section {
		font-size: 9px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: .6px;
		color: var(--muted-fg);
		padding: 12px 14px 4px;
	}
	.ai-hist-item {
		padding: 8px 14px;
		font-size: 12px;
		color: var(--muted-fg);
		cursor: pointer;
		border-radius: 0;
		transition: background .15s;
		line-height: 1.4;
		border-left: 2px solid transparent;
	}
	.ai-hist-item:hover {
		background: var(--muted);
		color: var(--fg);
	}
	.ai-hist-item.active {
		background: var(--saffron-lt);
		color: var(--saffron-hv);
		border-left-color: var(--saffron);
		font-weight: 600;
	}
	.ai-main {
		display: flex;
		flex-direction: column;
		background: #FDFCF9;
	}
	.ai-topbar {
		background: #fff;
		border-bottom: 1px solid var(--border-dk);
		padding: 14px 20px;
		display: flex;
		align-items: center;
		gap: 10px;
	}
	.ai-icon {
		width: 32px;
		height: 32px;
		background: var(--primary);
		border-radius: var(--r-sm);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 16px;
		color: var(--saffron);
		flex-shrink: 0;
	}
	.ai-messages {
		flex: 1;
		overflow-y: auto;
		padding: 20px;
		display: flex;
		flex-direction: column;
		gap: 14px;
	}
	.ai-msg {
		display: flex;
		gap: 10px;
		max-width: 85%;
	}
	.ai-msg.user {
		align-self: flex-end;
		flex-direction: row-reverse;
	}
	.ai-msg-bubble {
		padding: 12px 16px;
		font-size: 13px;
		line-height: 1.6;
		border-radius: 16px;
	}
	.ai-msg.ai .ai-msg-bubble {
		background: #fff;
		border: 1px solid var(--border-dk);
		border-radius: 16px 16px 16px 4px;
	}
	.ai-msg.user .ai-msg-bubble {
		background: var(--primary);
		color: #fff;
		border-radius: 16px 16px 4px 16px;
	}
	.ai-msg-bubble.thinking {
		color: var(--muted-fg);
		font-style: italic;
	}
	.ai-icon-sm {
		width: 28px;
		height: 28px;
		background: var(--primary);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 13px;
		color: var(--saffron);
		flex-shrink: 0;
		margin-top: 2px;
	}
	.ai-chips-bar {
		padding: 12px 20px;
		border-top: 1px solid var(--border);
		background: #fff;
		display: flex;
		flex-wrap: wrap;
		gap: 7px;
	}
	.ai-chip {
		padding: 7px 14px;
		border-radius: 100px;
		border: 1.5px solid var(--border-dk);
		font-size: 12px;
		font-weight: 500;
		cursor: pointer;
		color: var(--muted-fg);
		background: #fff;
		transition: all .15s;
		white-space: nowrap;
	}
	.ai-chip:hover {
		border-color: var(--saffron);
		color: var(--saffron);
		background: var(--saffron-lt);
	}
	.ai-input-bar {
		padding: 12px 16px;
		border-top: 1px solid var(--border);
		background: #fff;
		display: flex;
		gap: 8px;
		align-items: center;
	}
	.ai-input {
		flex: 1;
		padding: 10px 16px;
		border: 1.5px solid var(--border-dk);
		border-radius: 100px;
		font-size: 13px;
		font-family: var(--ff);
		transition: border-color .15s;
	}
	.ai-input:focus {
		outline: none;
		border-color: var(--saffron);
	}
</style>
