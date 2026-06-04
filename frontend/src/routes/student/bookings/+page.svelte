<script lang="ts">
	import { goto } from '$app/navigation';

	let activeTab = $state('upcoming');
	let showCancelBox = $state(false);

	function switchTab(tab: string) {
		activeTab = tab;
	}

	function toggleCancelBox() {
		showCancelBox = !showCancelBox;
	}
</script>

<svelte:head>
	<title>My Bookings — EduLink SL</title>
</svelte:head>

<div class="app-topbar">
	<div class="app-topbar-title">My Bookings</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i></div>
		<a href="/find-tutors" class="btn btn-saffron btn-sm"><i class="ti ti-plus"></i>Book a tutor</a>
	</div>
</div>

<div class="app-content">
	<div class="tabs">
		<div class="tab {activeTab === 'upcoming' ? 'active' : ''}" onclick={() => switchTab('upcoming')}>Upcoming <span class="tab-count">3</span></div>
		<div class="tab {activeTab === 'completed' ? 'active' : ''}" onclick={() => switchTab('completed')}>Completed <span class="tab-count">21</span></div>
		<div class="tab {activeTab === 'cancelled' ? 'active' : ''}" onclick={() => switchTab('cancelled')}>Cancelled <span class="tab-count">2</span></div>
	</div>

	{#if activeTab === 'upcoming'}
		<div id="tab-upcoming">
			<div class="cancel-confirm" class:show={showCancelBox}>
				<div style="font-size:13px;font-weight:700;color:var(--red);margin-bottom:6px"><i class="ti ti-alert-triangle"></i> Cancel this session?</div>
				<div style="font-size:13px;color:var(--red);margin-bottom:10px">Cancelling within 24h deducts <strong>10 merit points</strong> from your score. Cancelling earlier deducts 3 points.</div>
				<div style="display:flex;gap:8px"><button class="btn btn-danger btn-sm" onclick={toggleCancelBox}>Yes, cancel session</button><button class="btn btn-ghost btn-sm" onclick={toggleCancelBox}>Keep booking</button></div>
			</div>

			<div class="booking-card" style="border-left:3px solid var(--saffron)">
				<div class="bc-avatar" style="background:#EEF2FF;color:#3B4FD8">AP</div>
				<div class="bc-body">
					<div class="bc-name">Aruna Perera <span class="badge badge-primary">Physics</span> <span class="badge badge-teal">Online</span></div>
					<div class="bc-meta"><span><i class="ti ti-calendar"></i> Tuesday, 24 Jun 2025</span><span><i class="ti ti-clock"></i> 9:00 – 10:00 AM</span><span><i class="ti ti-repeat"></i> Single session</span></div>
				</div>
				<div class="bc-time"><div class="bc-time-val">Today</div><div class="bc-time-val" style="font-size:11px;color:var(--saffron)">in 3h 20m</div></div>
				<div class="bc-actions">
					<a href="#" class="btn btn-teal btn-sm"><i class="ti ti-video"></i> Join</a>
					<button class="btn btn-ghost btn-sm" onclick={toggleCancelBox}><i class="ti ti-x"></i></button>
				</div>
			</div>

			<div class="booking-card" style="border-left:3px solid var(--teal)">
				<div class="bc-avatar" style="background:#FFF0E0;color:#A06000">DJ</div>
				<div class="bc-body">
					<div class="bc-name">Dilini Jayasuriya <span class="badge badge-primary">Combined Maths</span> <span class="badge badge-teal">Online</span></div>
					<div class="bc-meta"><span><i class="ti ti-calendar"></i> Wednesday, 25 Jun 2025</span><span><i class="ti ti-clock"></i> 2:00 – 3:00 PM</span><span><i class="ti ti-repeat"></i> Monthly pack · Session 2/4</span></div>
				</div>
				<div class="bc-time"><div class="bc-time-val">Tomorrow</div><div class="bc-time-day">14:00</div></div>
				<div class="bc-actions">
					<a href="/student/messages" class="btn btn-ghost btn-sm"><i class="ti ti-message"></i></a>
					<button class="btn btn-ghost btn-sm" onclick={toggleCancelBox}><i class="ti ti-x"></i></button>
				</div>
			</div>

			<div class="booking-card" style="border-left:3px solid var(--green)">
				<div class="bc-avatar" style="background:#F0FDF4;color:#166534">RS</div>
				<div class="bc-body">
					<div class="bc-name">Dr. Rohan Silva <span class="badge badge-primary">Chemistry</span> <span class="badge badge-saffron">In-person</span></div>
					<div class="bc-meta"><span><i class="ti ti-calendar"></i> Friday, 27 Jun 2025</span><span><i class="ti ti-clock"></i> 5:00 – 6:00 PM</span><span><i class="ti ti-map-pin"></i> Gampaha, teacher's location</span></div>
				</div>
				<div class="bc-time"><div class="bc-time-val">Fri</div><div class="bc-time-day">17:00</div></div>
				<div class="bc-actions">
					<a href="/student/messages" class="btn btn-ghost btn-sm"><i class="ti ti-message"></i></a>
					<button class="btn btn-ghost btn-sm" onclick={toggleCancelBox}><i class="ti ti-x"></i></button>
				</div>
			</div>
		</div>
	{/if}

	{#if activeTab === 'completed'}
		<div id="tab-completed">
			<div style="margin-bottom:10px">
				<div class="alert alert-info" style="margin-bottom:12px"><i class="ti ti-info-circle"></i> You can only leave a review within 7 days of a completed session.</div>
			</div>
			<div class="booking-card">
				<div class="bc-avatar" style="background:#EEF2FF;color:#3B4FD8">AP</div>
				<div class="bc-body">
					<div class="bc-name">Aruna Perera <span class="badge badge-primary">Physics</span> <span class="badge badge-green">Attended</span></div>
					<div class="bc-meta"><span><i class="ti ti-calendar"></i> Tuesday, 17 Jun 2025</span><span><i class="ti ti-clock"></i> 9:00 – 10:00 AM</span></div>
				</div>
				<div class="bc-time"><div class="bc-time-day">17 Jun</div></div>
				<div class="bc-actions">
					<button class="btn btn-saffron btn-sm"><i class="ti ti-star"></i> Leave review</button>
				</div>
			</div>
			<div class="booking-card">
				<div class="bc-avatar" style="background:#FFF0E0;color:#A06000">DJ</div>
				<div class="bc-body">
					<div class="bc-name">Dilini Jayasuriya <span class="badge badge-primary">Combined Maths</span> <span class="badge badge-green">Attended</span></div>
					<div class="bc-meta"><span><i class="ti ti-calendar"></i> Monday, 10 Jun 2025</span><span><i class="ti ti-clock"></i> 2:00 – 3:00 PM</span></div>
				</div>
				<div class="bc-time"><div class="bc-time-day">10 Jun</div></div>
				<div class="bc-actions"><span class="badge badge-teal"><i class="ti ti-check"></i> Reviewed</span></div>
			</div>
		</div>
	{/if}

	{#if activeTab === 'cancelled'}
		<div id="tab-cancelled">
			<div class="booking-card" style="opacity:.7">
				<div class="bc-avatar" style="background:var(--muted);color:var(--muted-fg)">AP</div>
				<div class="bc-body">
					<div class="bc-name">Aruna Perera <span class="badge badge-red">Cancelled by you</span></div>
					<div class="bc-meta"><span><i class="ti ti-calendar"></i> Monday, 3 Jun 2025</span><span style="color:var(--red)"><i class="ti ti-shield-x"></i> −10 merit points deducted</span></div>
				</div>
				<div class="bc-actions"><a href="/find-tutors" class="btn btn-ghost btn-sm">Book again</a></div>
			</div>
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
		position: relative;
	}
	.notif-btn:hover {
		border-color: var(--saffron);
		color: var(--saffron);
	}
	.booking-card {
		background: #fff;
		border-radius: var(--r);
		border: 1px solid var(--border-dk);
		padding: 18px 20px;
		margin-bottom: 10px;
		display: flex;
		align-items: center;
		gap: 14px;
		transition: box-shadow .15s;
	}
	.booking-card:hover {
		box-shadow: var(--sh-sm);
	}
	.bc-avatar {
		width: 48px;
		height: 48px;
		border-radius: var(--r-sm);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 16px;
		font-weight: 800;
		flex-shrink: 0;
	}
	.bc-body {
		flex: 1;
		min-width: 0;
	}
	.bc-name {
		font-size: 14px;
		font-weight: 700;
		margin-bottom: 2px;
		display: flex;
		align-items: center;
		gap: 8px;
	}
	.bc-meta {
		font-size: 12px;
		color: var(--muted-fg);
		display: flex;
		align-items: center;
		gap: 10px;
		flex-wrap: wrap;
	}
	.bc-meta i {
		font-size: 12px;
	}
	.bc-actions {
		display: flex;
		gap: 6px;
		flex-shrink: 0;
	}
	.bc-time {
		text-align: right;
		flex-shrink: 0;
		min-width: 80px;
	}
	.bc-time-val {
		font-size: 13px;
		font-weight: 700;
		color: var(--primary);
		font-family: var(--ff-mono);
	}
	.bc-time-day {
		font-size: 11px;
		color: var(--muted-fg);
	}
	.cancel-confirm {
		background: var(--red-lt);
		border: 1px solid #FECACA;
		border-radius: var(--r-sm);
		padding: 12px 14px;
		margin-bottom: 10px;
		display: none;
	}
	.cancel-confirm.show {
		display: block;
	}
</style>
