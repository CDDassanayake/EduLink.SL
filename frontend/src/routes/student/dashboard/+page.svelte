<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { getAuthStore } from '$lib/stores/auth.svelte';

	let authStore = getAuthStore();
	let { data } = $props();

	// Get greeting based on time of day
	function getGreeting() {
		const hour = new Date().getHours();
		if (hour < 12) return 'Good morning';
		if (hour < 17) return 'Good afternoon';
		return 'Good evening';
	}

	// Get formatted date
	function getCurrentDate() {
		return new Date().toLocaleDateString('en-GB', {
			weekday: 'long',
			day: 'numeric',
			month: 'long',
			year: 'numeric'
		});
	}

	let user = $derived(data.user);
	let isLoading = $derived(data.isLoading);
</script>

<svelte:head>
	<title>Student Dashboard — EduLink SL</title>
</svelte:head>

{#if isLoading}
	<div class="loading-container">
		<div class="loading-spinner"></div>
		<div class="loading-text">Loading your dashboard...</div>
	</div>
{:else if user}
	<!-- Top bar -->
	<div class="app-topbar">
		<div class="app-topbar-title">Dashboard</div>
		<div class="app-topbar-right">
			<div class="notif-btn"><i class="ti ti-bell"></i><div class="notif-dot"></div></div>
			<a href="/find-tutors" class="btn btn-saffron btn-sm"><i class="ti ti-plus"></i>Book a tutor</a>
		</div>
	</div>

	<!-- Welcome -->
	<div class="welcome-bar">
		<div>
			<div class="wb-greeting">{getGreeting()}, {user.full_name.split(' ')[0]} 👋</div>
			<div class="wb-sub">{getCurrentDate()} · {user.role} · {user.city || 'Location not set'}</div>
		</div>
		<div style="text-align: right">
			<div style="font-size: 22px; font-weight: 800; color: var(--saffron)">{user.merit_score}<span style="font-size: 13px; opacity: .7">/100</span></div>
			<div style="font-size: 10px; font-family: var(--ff-mono); text-transform: uppercase; letter-spacing: .5px; opacity: .7">Merit Score</div>
		</div>
	</div>
{/if}

{#if user}
<div class="app-content">
	<!-- Stats -->
	<div class="stats-row stats-4" style="margin-bottom: 20px">
		<div class="stat-box stat-primary">
			<div class="stat-label"><i class="ti ti-calendar"></i> Upcoming</div>
			<div class="stat-value" style="color: var(--primary)">3</div>
			<div class="stat-sub">sessions this week</div>
		</div>
		<div class="stat-box stat-teal">
			<div class="stat-label"><i class="ti ti-check"></i> Completed</div>
			<div class="stat-value">24</div>
			<div class="stat-sub" style="color: var(--green)">+3 this month</div>
		</div>
		<div class="stat-box stat-saffron">
			<div class="stat-label"><i class="ti ti-book"></i> Subjects</div>
			<div class="stat-value">3</div>
			<div class="stat-sub">Physics, Maths, Chem</div>
		</div>
		<div class="stat-box stat-green">
			<div class="stat-label"><i class="ti ti-shield"></i> Merit</div>
			<div class="stat-value" style="color: var(--green)">95</div>
			<div class="stat-sub" style="color: var(--green)">Excellent</div>
		</div>
	</div>

	<!-- Two column grid -->
	<div class="grid-2" style="align-items: start">
		<!-- Upcoming sessions -->
		<div class="section-card">
			<div class="sec-head" style="margin-bottom: 14px">
				<div style="font-size: 14px; font-weight: 700">Upcoming sessions</div>
				<a href="/student/bookings" class="sec-action">View all</a>
			</div>
			<div class="upcoming-session">
				<div style="width: 36px; height: 36px; border-radius: var(--r-sm); background: #EEF2FF; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; color: #3B4FD8; flex-shrink: 0">AP</div>
				<div class="us-sep"></div>
				<div class="us-info">
					<div class="us-name">Aruna Perera</div>
					<div class="us-sub"><i class="ti ti-atom" style="font-size: 11px"></i> Physics</div>
				</div>
				<div class="us-time">
					<div class="us-time-val">9:00 AM</div>
					<div class="us-time-day">Today</div>
				</div>
				<span class="badge badge-primary">Online</span>
			</div>
			<div class="upcoming-session">
				<div style="width: 36px; height: 36px; border-radius: var(--r-sm); background: #FFF0E0; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; color: #A06000; flex-shrink: 0">DJ</div>
				<div class="us-sep"></div>
				<div class="us-info">
					<div class="us-name">Dilini Jayasuriya</div>
					<div class="us-sub"><i class="ti ti-calculator" style="font-size: 11px"></i> Combined Maths</div>
				</div>
				<div class="us-time">
					<div class="us-time-val">2:00 PM</div>
					<div class="us-time-day">Wed</div>
				</div>
				<span class="badge badge-teal">Online</span>
			</div>
			<div class="upcoming-session">
				<div style="width: 36px; height: 36px; border-radius: var(--r-sm); background: #F0FDF4; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; color: #166534; flex-shrink: 0">RS</div>
				<div class="us-sep"></div>
				<div class="us-info">
					<div class="us-name">Dr. Rohan Silva</div>
					<div class="us-sub"><i class="ti ti-flask" style="font-size: 11px"></i> Chemistry</div>
				</div>
				<div class="us-time">
					<div class="us-time-val">5:00 PM</div>
					<div class="us-time-day">Fri</div>
				</div>
				<span class="badge badge-saffron">In-person</span>
			</div>
			<a href="/find-tutors" class="btn btn-ghost btn-full" style="margin-top: 12px"><i class="ti ti-plus"></i> Book another tutor</a>
		</div>

		<!-- Right column: notifications + AI -->
		<div style="display: flex; flex-direction: column; gap: 16px">
			<div class="section-card">
				<div class="sec-head" style="margin-bottom: 12px">
					<div style="font-size: 14px; font-weight: 700">Notifications</div>
					<span class="badge badge-saffron">3 new</span>
				</div>
				<div class="notif-item">
					<div class="ni-icon" style="background: var(--saffron-lt); color: var(--saffron)"><i class="ti ti-calendar"></i></div>
					<div>
						<div class="ni-text"><strong>Reminder:</strong> Physics class with Aruna Perera today at 9:00 AM</div>
						<div class="ni-time">2 hours ago</div>
					</div>
				</div>
				<div class="notif-item">
					<div class="ni-icon" style="background: var(--green-lt); color: var(--green)"><i class="ti ti-check"></i></div>
					<div>
						<div class="ni-text"><strong>Booking confirmed</strong> for Chemistry with Dr. Rohan — Fri 27 Jun</div>
						<div class="ni-time">Yesterday</div>
					</div>
				</div>
				<div class="notif-item">
					<div class="ni-icon" style="background: var(--teal-lt); color: var(--teal)"><i class="ti ti-message"></i></div>
					<div>
						<div class="ni-text">New message from <strong>Dilini Jayasuriya</strong></div>
						<div class="ni-time">2 days ago</div>
					</div>
				</div>
			</div>

			<!-- AI Career Chat teaser -->
			<div class="section-card" style="background: var(--primary); border-color: transparent">
				<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px">
					<div style="width: 30px; height: 30px; background: rgba(255,255,255,.1); border-radius: var(--r-sm); display: flex; align-items: center; justify-content: center; font-size: 15px; color: var(--saffron)"><i class="ti ti-sparkles"></i></div>
					<div>
						<div style="font-size: 13px; font-weight: 700; color: #fff">AI Career Guide</div>
						<div style="font-size: 10px; color: rgba(255,255,255,.5)">Powered by OpenAI</div>
					</div>
				</div>
				<div style="font-size: 13px; color: rgba(255,255,255,.75); line-height: 1.55; margin-bottom: 12px">Hi {user.full_name.split(' ')[0]}! Ready to explore career paths and get study tips?</div>
				<a href="/student/ai-chat" class="btn btn-outline-white btn-full btn-sm"><i class="ti ti-sparkles"></i> Open AI Career Chat</a>
			</div>
		</div>
	</div>
</div>
{/if}

<style>
	.loading-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 60vh;
		gap: 16px;
	}
	.loading-spinner {
		width: 40px;
		height: 40px;
		border: 3px solid var(--border);
		border-top-color: var(--saffron);
		border-radius: 50%;
		animation: spin 0.8s linear infinite;
	}
	@keyframes spin {
		to { transform: rotate(360deg); }
	}
	.loading-text {
		font-size: 14px;
		color: var(--muted-fg);
	}

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
	.app-content {
		flex: 1;
		padding: 24px;
		overflow-y: auto;
	}
	.welcome-bar {
		background: linear-gradient(135deg, #0E163A 0%, #161F4E 55%, #0D3B6E 100%);
		padding: 24px 28px;
		color: #fff;
		display: flex;
		align-items: center;
		justify-content: space-between;
	}
	.wb-greeting {
		font-size: 20px;
		font-weight: 800;
		margin-bottom: 2px;
	}
	.wb-sub {
		font-size: 13px;
		opacity: .7;
	}
	.upcoming-session {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 12px;
		border-radius: var(--r-sm);
		border: 1.5px solid var(--border-dk);
		background: #fff;
		margin-bottom: 8px;
		cursor: pointer;
		transition: all .15s;
	}
	.upcoming-session:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
	}
	.us-time {
		text-align: center;
		min-width: 52px;
	}
	.us-time-val {
		font-family: var(--ff-mono);
		font-size: 13px;
		font-weight: 700;
		color: var(--primary);
	}
	.us-time-day {
		font-size: 10px;
		color: var(--muted-fg);
		font-family: var(--ff-mono);
	}
	.us-sep {
		width: 1px;
		height: 36px;
		background: var(--border-dk);
	}
	.us-info {
		flex: 1;
	}
	.us-name {
		font-size: 13px;
		font-weight: 700;
		margin-bottom: 1px;
	}
	.us-sub {
		font-size: 12px;
		color: var(--muted-fg);
	}
	.notif-item {
		display: flex;
		gap: 10px;
		padding: 11px 0;
		border-bottom: 1px solid var(--border);
	}
	.notif-item:last-child {
		border-bottom: none;
	}
	.ni-icon {
		width: 32px;
		height: 32px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 14px;
		flex-shrink: 0;
	}
	.ni-text {
		flex: 1;
		font-size: 13px;
		color: var(--fg);
		line-height: 1.45;
	}
	.ni-time {
		font-size: 11px;
		color: var(--muted-fg);
		margin-top: 2px;
	}
</style>
