<script lang="ts">
	import { goto } from '$app/navigation';

	let selectedDate = $state(1);
	let selectedTime = $state(0);
	let selectedSessionType = $state(0);
	let activeTab = $state(0);

	const dates = [
		{ day: 'Mon', date: 23, disabled: true },
		{ day: 'Tue', date: 24 },
		{ day: 'Wed', date: 25 },
		{ day: 'Thu', date: 26 }
	];

	const times = ['9:00 AM', '2:00 PM', '5:00 PM', '7:00 PM'];

	const sessionTypes = [
		{ name: 'Single', sub: '1 class' },
		{ name: 'Monthly', sub: '4 classes · save 10%' }
	];

	function selectDate(index: number) {
		if (!dates[index].disabled) selectedDate = index;
	}

	function selectTime(index: number) {
		selectedTime = index;
	}

	function selectSessionType(index: number) {
		selectedSessionType = index;
	}

	function selectTab(index: number) {
		activeTab = index;
	}

	function bookSession() {
		goto('/student/book');
	}

	function messageTutor() {
		goto('/student/messages');
	}
</script>

<svelte:head>
	<title>Aruna Perera — Physics Tutor · EduLink SL</title>
</svelte:head>

<header class="pub-nav">
	<div class="container">
		<a href="/" class="nav-logo">EDULINK.SL</a>
		<nav class="nav-links">
			<a href="/find-tutors" class="nav-link">← Back to search</a>
		</nav>
		<div class="nav-right">
			<a href="/student/dashboard" class="btn btn-ghost btn-sm"><i class="ti ti-layout-dashboard"></i> Dashboard</a>
			<a href="/student/messages" class="btn btn-ghost btn-sm"><i class="ti ti-message"></i></a>
		</div>
	</div>
</header>

<!-- Profile hero -->
<div class="profile-hero">
	<div class="container">
		<div class="ph-inner">
			<div class="ph-avatar">AP</div>
			<div style="flex:1">
				<div class="ph-name">Aruna Perera <span class="verified-tick" style="width:20px;height:20px"></span></div>
				<div class="ph-spec">Physics Specialist (A/L) · BSc Physics (Hons), University of Peradeniya · 12 years experience</div>
				<div class="ph-metas">
					<span class="ph-meta"><i class="ti ti-map-pin"></i>Colombo 07</span>
					<span class="ph-meta"><i class="ti ti-device-laptop"></i>Online</span>
					<span class="ph-meta"><i class="ti ti-building"></i>In-person</span>
					<span class="ph-meta"><i class="ti ti-language"></i>English, Sinhala</span>
					<span class="badge-merit">MERIT 98</span>
				</div>
				<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px">
					<span style="color:var(--saffron);font-size:15px">★★★★★</span>
					<span style="font-weight:800;font-size:16px">4.9</span>
					<span style="color:var(--muted-fg);font-size:13px">(120 reviews)</span>
					<span style="color:var(--muted-fg);font-size:13px">·</span>
					<span style="font-size:13px;color:var(--muted-fg)"><i class="ti ti-users" style="font-size:13px"></i> 340 students taught</span>
				</div>
				<div class="ph-stats">
					<div><div class="ph-stat-val">12</div><div class="ph-stat-lbl">Years exp.</div></div>
					<div style="width:1px;background:var(--border-dk);margin:0 4px"></div>
					<div><div class="ph-stat-val">340</div><div class="ph-stat-lbl">Students</div></div>
					<div style="width:1px;background:var(--border-dk);margin:0 4px"></div>
					<div><div class="ph-stat-val">98%</div><div class="ph-stat-lbl">Merit score</div></div>
				</div>
			</div>
			<div>
				<div style="display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted-fg)">
					<span>Merit score</span>
					<div class="merit-bar" style="width:80px"><div class="merit-fill" style="width:98%"></div></div>
					<span style="font-weight:700;color:var(--green)">98/100</span>
				</div>
			</div>
		</div>
	</div>
</div>

<!-- Profile body -->
<div class="profile-body">
	<div class="container">
		<div class="profile-layout">
			<div class="profile-main">
				<!-- Tabs -->
				<div class="tabs" style="background:#fff;border-radius:var(--r);padding:0 4px;border:1px solid var(--border-dk)">
					<div class="tab {activeTab === 0 ? 'active' : ''}" onclick={() => selectTab(0)}>About</div>
					<div class="tab {activeTab === 1 ? 'active' : ''}" onclick={() => selectTab(1)}>Schedule</div>
					<div class="tab {activeTab === 2 ? 'active' : ''}" onclick={() => selectTab(2)}>Subjects &amp; Pricing</div>
					<div class="tab {activeTab === 3 ? 'active' : ''}" onclick={() => selectTab(3)}>Reviews (120)</div>
				</div>

				<!-- About -->
				<div class="section-card">
					<div style="font-size:14px;font-weight:700;margin-bottom:12px">About Aruna</div>
					<p style="font-size:14px;color:var(--muted-fg);line-height:1.7;margin-bottom:12px">I hold a BSc (Hons) in Physics from the University of Peradeniya and have over 12 years of teaching experience at A/L level. My approach combines strong theoretical foundations with rigorous problem-solving practice.</p>
					<p style="font-size:14px;color:var(--muted-fg);line-height:1.7">I specialise in preparing students for the national A/L examination, with a strong focus on past paper analysis and exam technique. I offer both individual and group sessions and provide comprehensive revision materials.</p>
					<div class="divider"></div>
					<div style="display:flex;flex-wrap:wrap;gap:8px">
						<span class="badge badge-primary">A/L Physics</span>
						<span class="badge badge-primary">Combined Maths</span>
						<span class="badge badge-teal">Individual sessions</span>
						<span class="badge badge-teal">Group classes</span>
						<span class="badge badge-saffron">Past paper specialist</span>
					</div>
				</div>

				<!-- Availability grid -->
				<div class="section-card">
					<div style="font-size:14px;font-weight:700;margin-bottom:14px">Weekly availability — click to book</div>
					<div style="overflow-x:auto">
						<table class="sched-grid" style="min-width:420px">
							<thead>
								<tr><th style="width:60px">Time</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>
							</thead>
							<tbody>
								<tr><td class="sched-time">8–9 AM</td><td class="sched-open">Open</td><td class="sched-blocked">—</td><td class="sched-open">Open</td><td class="sched-open">Open</td><td class="sched-blocked">—</td><td class="sched-open">Open</td></tr>
								<tr><td class="sched-time">9–10 AM</td><td class="sched-booked">Booked</td><td class="sched-open">Open</td><td class="sched-blocked">—</td><td class="sched-open">Open</td><td class="sched-open">Open</td><td class="sched-booked">Booked</td></tr>
								<tr><td class="sched-time">2–3 PM</td><td class="sched-open">Open</td><td class="sched-booked">Booked</td><td class="sched-open">Open</td><td class="sched-blocked">—</td><td class="sched-open">Open</td><td class="sched-open">Open</td></tr>
								<tr><td class="sched-time">5–6 PM</td><td class="sched-blocked">—</td><td class="sched-open">Open</td><td class="sched-booked">Booked</td><td class="sched-open">Open</td><td class="sched-booked">Booked</td><td class="sched-blocked">—</td></tr>
								<tr><td class="sched-time">7–8 PM</td><td class="sched-open">Open</td><td class="sched-open">Open</td><td class="sched-open">Open</td><td class="sched-booked">Booked</td><td class="sched-open">Open</td><td class="sched-open">Open</td></tr>
							</tbody>
						</table>
					</div>
					<div style="display:flex;gap:14px;margin-top:12px">
						<span style="display:flex;align-items:center;gap:5px;font-size:11px;color:var(--muted-fg)"><span style="width:10px;height:10px;border-radius:2px;background:#EEF9F7;border:1px solid var(--teal-md);display:inline-block"></span>Available</span>
						<span style="display:flex;align-items:center;gap:5px;font-size:11px;color:var(--muted-fg)"><span style="width:10px;height:10px;border-radius:2px;background:#EEF2FF;display:inline-block"></span>Booked</span>
						<span style="display:flex;align-items:center;gap:5px;font-size:11px;color:var(--muted-fg)"><span style="width:10px;height:10px;border-radius:2px;background:var(--muted);display:inline-block"></span>Unavailable</span>
					</div>
				</div>

				<!-- Reviews -->
				<div class="section-card">
					<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
						<div style="font-size:14px;font-weight:700">Student reviews</div>
						<span style="font-size:12px;color:var(--muted-fg)">120 verified reviews</span>
					</div>
					<div class="review-card">
						<div class="avatar av-teal av-sm">TW</div>
						<div class="rev-content">
							<div class="rev-header"><span class="rev-name">Tharaka Wijesinghe</span><span style="color:var(--saffron);font-size:12px">★★★★★</span></div>
							<div class="rev-text">Mr. Aruna's explanations are crystal clear. I moved from a C to an A in Physics in one term. His past paper sessions are gold.</div>
							<div class="rev-meta"><span class="badge badge-teal" style="font-size:9px">Verified booking</span> A/L Physics · 2 weeks ago</div>
						</div>
					</div>
					<div class="review-card">
						<div class="avatar av-saffron av-sm">KP</div>
						<div class="rev-content">
							<div class="rev-header"><span class="rev-name">Kasun Perera</span><span style="color:var(--saffron);font-size:12px">★★★★★</span></div>
							<div class="rev-text">Very structured approach. He never cancels, always on time, and genuinely cares about your understanding. Highly recommended.</div>
							<div class="rev-meta"><span class="badge badge-teal" style="font-size:9px">Verified booking</span> A/L Physics · 1 month ago</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Booking panel -->
			<div class="booking-panel">
				<div style="display:flex;align-items:baseline;gap:6px;margin-bottom:4px">
					<div class="bp-price">LKR 3,500<span>/hr</span></div>
				</div>
				<div style="display:flex;align-items:center;gap:6px;margin-bottom:16px">
					<span style="color:var(--saffron)">★★★★★</span>
					<span style="font-weight:700;font-size:13px">4.9</span>
					<span style="color:var(--muted-fg);font-size:12px">(120 reviews)</span>
				</div>
				<div class="divider" style="margin:12px 0"></div>

				<div class="form-label" style="margin-bottom:6px">Choose a date</div>
				<div class="date-grid">
					{#each dates as date, i}
						<div class="date-btn {selectedDate === i ? 'sel' : ''} {date.disabled ? 'dis' : ''}" onclick={() => selectDate(i)}>
							<div>{date.day}</div>
							<div>{date.date}</div>
						</div>
					{/each}
				</div>

				<div class="form-label" style="margin-top:14px;margin-bottom:6px">Available times</div>
				<div class="time-slots">
					{#each times as time, i}
						<div class="time-btn {selectedTime === i ? 'sel' : ''}" onclick={() => selectTime(i)}>{time}</div>
					{/each}
				</div>

				<div class="form-label" style="margin-top:14px;margin-bottom:6px">Session type</div>
				<div class="stype-grid">
					{#each sessionTypes as st, i}
						<div class="stype-btn {selectedSessionType === i ? 'sel' : ''}" onclick={() => selectSessionType(i)}>{st.name}<span class="stype-sub">{st.sub}</span></div>
					{/each}
				</div>

				<div class="price-summary">
					<div class="pr-row"><span>1 session × LKR 3,500</span><span>LKR 3,500</span></div>
					<div class="pr-row"><span>Service fee</span><span>LKR 350</span></div>
					<div class="pr-row total"><span>Total</span><span style="color:var(--primary)">LKR 3,850</span></div>
				</div>

				<button class="btn btn-primary btn-full btn-lg" onclick={bookSession}><i class="ti ti-lock"></i> Confirm &amp; Pay</button>
				<p style="font-size:11px;text-align:center;color:var(--muted-fg);margin-top:8px">Free cancellation up to 24h before · Secure Stripe payment</p>

				<div class="divider" style="margin:16px 0"></div>
				<button class="btn btn-ghost btn-full" onclick={messageTutor}><i class="ti ti-message"></i> Message Aruna</button>
			</div>
		</div>
	</div>
</div>

<style>
	.profile-hero {
		background: #fff;
		border-bottom: 1px solid var(--border-dk);
		padding: 28px 0;
	}
	.ph-inner {
		display: flex;
		gap: 20px;
		align-items: flex-start;
	}
	.ph-avatar {
		width: 96px;
		height: 96px;
		border-radius: var(--r-lg);
		background: #EEF2FF;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 32px;
		font-weight: 800;
		color: #3B4FD8;
		flex-shrink: 0;
	}
	.ph-name {
		font-size: 26px;
		font-weight: 800;
		display: flex;
		align-items: center;
		gap: 10px;
		margin-bottom: 4px;
	}
	.ph-spec {
		font-size: 15px;
		color: var(--muted-fg);
		margin-bottom: 10px;
	}
	.ph-metas {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
		margin-bottom: 12px;
	}
	.ph-meta {
		display: flex;
		align-items: center;
		gap: 4px;
		font-size: 13px;
		color: var(--muted-fg);
	}
	.ph-meta i {
		font-size: 14px;
	}
	.ph-stats {
		display: flex;
		gap: 16px;
	}
	.ph-stat-val {
		font-size: 18px;
		font-weight: 800;
		color: var(--fg);
	}
	.ph-stat-lbl {
		font-size: 11px;
		color: var(--muted-fg);
		font-family: var(--ff-mono);
		text-transform: uppercase;
		letter-spacing: .4px;
	}
	.profile-body {
		padding: 28px 0 48px;
		background: var(--bg);
	}
	.profile-layout {
		display: grid;
		grid-template-columns: 1fr 300px;
		gap: 24px;
		align-items: start;
	}
	.profile-main {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}
	.booking-panel {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		padding: 24px;
		position: sticky;
		top: 88px;
	}
	.bp-price {
		font-size: 28px;
		font-weight: 800;
		color: var(--fg);
	}
	.bp-price span {
		font-size: 14px;
		font-weight: 500;
		color: var(--muted-fg);
	}
	.date-grid {
		display: grid;
		grid-template-columns: repeat(4,1fr);
		gap: 6px;
		margin-top: 8px;
	}
	.date-btn {
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		padding: 8px 4px;
		text-align: center;
		cursor: pointer;
		font-size: 11px;
		font-weight: 600;
		background: #fff;
		transition: all .15s;
		color: var(--muted-fg);
	}
	.date-btn:hover {
		border-color: var(--saffron);
		color: var(--saffron);
	}
	.date-btn.sel {
		background: var(--primary);
		border-color: var(--primary);
		color: #fff;
	}
	.date-btn.dis {
		opacity: .3;
		cursor: not-allowed;
	}
	.time-slots {
		display: flex;
		flex-wrap: wrap;
		gap: 6px;
		margin-top: 8px;
	}
	.time-btn {
		padding: 6px 12px;
		border-radius: var(--r-sm);
		border: 1.5px solid var(--border-dk);
		font-size: 12px;
		font-weight: 600;
		cursor: pointer;
		background: #fff;
		transition: all .15s;
		color: var(--muted-fg);
	}
	.time-btn:hover {
		border-color: var(--saffron);
		color: var(--saffron);
	}
	.time-btn.sel {
		background: var(--saffron);
		border-color: var(--saffron);
		color: #fff;
	}
	.stype-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 8px;
		margin-top: 8px;
	}
	.stype-btn {
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		padding: 10px 8px;
		text-align: center;
		cursor: pointer;
		font-size: 12px;
		font-weight: 600;
		background: #fff;
		transition: all .15s;
		color: var(--muted-fg);
		line-height: 1.4;
	}
	.stype-btn:hover {
		border-color: var(--saffron);
		color: var(--saffron);
	}
	.stype-btn.sel {
		background: var(--saffron-lt);
		border-color: var(--saffron);
		color: var(--saffron-hv);
	}
	.stype-sub {
		font-size: 10px;
		font-weight: 400;
		color: var(--muted-fg);
		display: block;
		margin-top: 2px;
	}
	.price-summary {
		background: var(--bg);
		border-radius: var(--r-sm);
		padding: 12px;
		margin: 12px 0;
	}
	.pr-row {
		display: flex;
		justify-content: space-between;
		font-size: 13px;
		margin-bottom: 5px;
		color: var(--muted-fg);
	}
	.pr-row.total {
		font-weight: 700;
		color: var(--fg);
		font-size: 14px;
		border-top: 1px solid var(--border-dk);
		padding-top: 8px;
		margin-top: 8px;
		margin-bottom: 0;
	}
	.review-card {
		display: flex;
		gap: 12px;
		padding: 14px 0;
		border-bottom: 1px solid var(--border);
	}
	.review-card:last-child {
		border-bottom: none;
	}
	.rev-content {
		flex: 1;
	}
	.rev-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 5px;
	}
	.rev-name {
		font-size: 13px;
		font-weight: 700;
	}
	.rev-text {
		font-size: 13px;
		color: var(--muted-fg);
		line-height: 1.55;
	}
	.rev-meta {
		font-size: 11px;
		color: var(--muted-fg);
		margin-top: 5px;
		display: flex;
		align-items: center;
		gap: 6px;
	}
	.merit-bar {
		height: 5px;
		background: var(--muted);
		border-radius: 100px;
		overflow: hidden;
		flex: 1;
	}
	.merit-fill {
		height: 100%;
		background: linear-gradient(90deg,var(--green),#34D399);
		border-radius: 100px;
	}
</style>
