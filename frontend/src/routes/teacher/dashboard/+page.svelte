<script lang="ts">
	import { goto } from '$app/navigation';
</script>

<svelte:head>
	<title>Teacher Dashboard — EduLink SL</title>
</svelte:head>

<div class="app-topbar">
	<div class="app-topbar-title">Teacher Dashboard</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i><div class="notif-dot"></div></div>
		<a href="/teacher/post-class" class="btn btn-saffron btn-sm"><i class="ti ti-plus"></i> Post a class</a>
	</div>
</div>

<div class="app-content">
	<!-- Earnings hero -->
	<div class="earn-hero">
		<div class="earn-lbl">June 2025 earnings</div>
		<div class="earn-val">LKR 48,500</div>
		<div style="display: flex; align-items: center; gap: 8px; margin-top: 4px">
			<span style="background: rgba(255,255,255,0.12); border-radius: 100px; padding: 3px 10px; font-size: 11px; display: flex; align-items: center; gap: 4px"><i class="ti ti-trending-up" style="font-size: 11px"></i> +22% vs last month</span>
		</div>
		<div class="earn-row">
			<div class="earn-mini">
				<div class="earn-mini-val">LKR 12,000</div>
				<div class="earn-mini-lbl">Pending payout</div>
			</div>
			<div class="earn-mini">
				<div class="earn-mini-val">14</div>
				<div class="earn-mini-lbl">Sessions this month</div>
			</div>
		</div>
	</div>

	<!-- Stats -->
	<div class="stats-row stats-4" style="margin-bottom: 20px">
		<div class="stat-box stat-saffron">
			<div class="stat-label"><i class="ti ti-star"></i> Avg rating</div>
			<div class="stat-value" style="color: var(--saffron)">4.9</div>
			<div class="stat-sub" style="color: var(--green)">Top 3% platform</div>
		</div>
		<div class="stat-box stat-teal">
			<div class="stat-label"><i class="ti ti-users"></i> Active students</div>
			<div class="stat-value">22</div>
			<div class="stat-sub" style="color: var(--green)">+4 this month</div>
		</div>
		<div class="stat-box stat-primary">
			<div class="stat-label"><i class="ti ti-list-check"></i> Active listings</div>
			<div class="stat-value">3</div>
			<div class="stat-sub">Physics, Maths, O/L</div>
		</div>
		<div class="stat-box stat-green">
			<div class="stat-label"><i class="ti ti-shield"></i> Merit score</div>
			<div class="stat-value" style="color: var(--green)">98</div>
			<div class="stat-sub" style="color: var(--green)">Excellent</div>
		</div>
	</div>

	<div class="grid-2" style="align-items: start">
		<!-- Today's classes -->
		<div class="section-card">
			<div class="sec-head" style="margin-bottom: 12px">
				<div style="font-size: 14px; font-weight: 700">Today's classes</div>
				<a href="/teacher/schedule" class="sec-action">Full schedule</a>
			</div>
			<div class="class-item">
				<div class="ci-time"><div class="ci-time-val">9:00</div><div class="ci-time-day">AM</div></div>
				<div class="ci-sep"></div>
				<div style="width: 32px; height: 32px; border-radius: 50%; background: #EEF2FF; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 800; color: #3B4FD8; flex-shrink: 0">KJ</div>
				<div class="ci-info"><div class="ci-student">Kasun Jayasuriya</div><div class="ci-subject"><i class="ti ti-atom" style="font-size: 10px"></i> A/L Physics</div></div>
				<span class="badge badge-primary">Online</span>
			</div>
			<div class="class-item">
				<div class="ci-time"><div class="ci-time-val">2:00</div><div class="ci-time-day">PM</div></div>
				<div class="ci-sep"></div>
				<div style="width: 32px; height: 32px; border-radius: 50%; background: #FDF4FF; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 800; color: #7C3AED; flex-shrink: 0">NW</div>
				<div class="ci-info"><div class="ci-student">Nadia Wickramasinghe</div><div class="ci-subject"><i class="ti ti-atom" style="font-size: 10px"></i> A/L Physics</div></div>
				<span class="badge badge-saffron">In-person</span>
			</div>
			<div class="class-item">
				<div class="ci-time"><div class="ci-time-val">5:00</div><div class="ci-time-day">PM</div></div>
				<div class="ci-sep"></div>
				<div style="width: 32px; height: 32px; border-radius: 50%; background: #F0FDF4; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 800; color: #166534; flex-shrink: 0">TB</div>
				<div class="ci-info"><div class="ci-student">Tharaka Bandara</div><div class="ci-subject"><i class="ti ti-calculator" style="font-size: 10px"></i> Combined Maths</div></div>
				<span class="badge badge-primary">Online</span>
			</div>
			<a href="/teacher/schedule" class="btn btn-ghost btn-full" style="margin-top: 12px"><i class="ti ti-calendar"></i> Manage schedule</a>
		</div>

		<!-- Quick actions -->
		<div>
			<div style="font-size: 14px; font-weight: 700; margin-bottom: 12px">Quick actions</div>
			<a href="/teacher/post-class" class="qa-btn">
				<i class="ti ti-plus"></i>
				<div><div class="qa-txt">Post a new class listing</div><div class="qa-sub">Reach more students by adding a subject</div></div>
				<i class="ti ti-chevron-right" style="font-size: 16px; color: var(--muted-fg); margin-left: auto"></i>
			</a>
			<a href="/teacher/schedule" class="qa-btn">
				<i class="ti ti-calendar-event"></i>
				<div><div class="qa-txt">Update your availability</div><div class="qa-sub">Set open slots for students to book</div></div>
				<i class="ti ti-chevron-right" style="font-size: 16px; color: var(--muted-fg); margin-left: auto"></i>
			</a>
			<a href="/teacher/messages" class="qa-btn">
				<i class="ti ti-message-circle"></i>
				<div><div class="qa-txt">Check messages</div><div class="qa-sub">3 unread from students</div></div>
				<span style="background: var(--saffron); color: #fff; font-size: 10px; font-weight: 800; padding: 2px 7px; border-radius: 100px; margin-left: auto">3</span>
			</a>
			<a href="/teacher/earnings" class="qa-btn">
				<i class="ti ti-wallet"></i>
				<div><div class="qa-txt">View earnings & payouts</div><div class="qa-sub">LKR 12,000 pending this week</div></div>
				<i class="ti ti-chevron-right" style="font-size: 16px; color: var(--muted-fg); margin-left: auto"></i>
			</a>
			<div style="background: var(--saffron-lt); border: 1.5px solid rgba(232,147,14,0.25); border-radius: var(--r-sm); padding: 13px 14px; margin-top: 6px">
				<div style="font-size: 12px; font-weight: 700; color: var(--saffron-hv); margin-bottom: 3px"><i class="ti ti-info-circle"></i> Listing renewal due in 3 days</div>
				<div style="font-size: 12px; color: var(--saffron-hv); opacity: 0.8; margin-bottom: 8px">Your A/L Physics listing expires on 27 June. Renew to keep it visible.</div>
				<a href="/teacher/post-payment" class="btn btn-saffron btn-sm">Renew now</a>
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
	.app-content {
		flex: 1;
		padding: 24px;
		overflow-y: auto;
	}
	.earn-hero {
		background: linear-gradient(135deg, #0E163A 0%, #161F4E 55%, #0D3B6E 100%);
		border-radius: var(--r-lg);
		padding: 22px;
		color: #fff;
		margin-bottom: 18px;
		position: relative;
		overflow: hidden;
	}
	.earn-hero::after {
		content: '';
		position: absolute;
		top: -30px;
		right: -30px;
		width: 120px;
		height: 120px;
		background: rgba(255, 255, 255, 0.04);
		border-radius: 50%;
	}
	.earn-val {
		font-size: 30px;
		font-weight: 800;
		margin: 4px 0;
	}
	.earn-lbl {
		font-size: 10px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.6px;
		opacity: 0.7;
	}
	.earn-row {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 12px;
		margin-top: 16px;
	}
	.earn-mini {
		background: rgba(255, 255, 255, 0.08);
		border-radius: var(--r-sm);
		padding: 12px;
	}
	.earn-mini-val {
		font-size: 16px;
		font-weight: 800;
	}
	.earn-mini-lbl {
		font-size: 10px;
		opacity: 0.7;
		font-family: var(--ff-mono);
		text-transform: uppercase;
		letter-spacing: 0.4px;
		margin-top: 2px;
	}
	.class-item {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 11px 0;
		border-bottom: 1px solid var(--border);
	}
	.class-item:last-child {
		border-bottom: none;
	}
	.ci-time {
		text-align: center;
		min-width: 50px;
	}
	.ci-time-val {
		font-size: 12px;
		font-weight: 800;
		color: var(--primary);
		font-family: var(--ff-mono);
	}
	.ci-time-day {
		font-size: 10px;
		color: var(--muted-fg);
	}
	.ci-sep {
		width: 1px;
		height: 30px;
		background: var(--border-dk);
	}
	.ci-info {
		flex: 1;
	}
	.ci-student {
		font-size: 13px;
		font-weight: 700;
	}
	.ci-subject {
		font-size: 11px;
		color: var(--muted-fg);
	}
	.qa-btn {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 12px 14px;
		background: #fff;
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		cursor: pointer;
		transition: all 0.15s;
		margin-bottom: 8px;
		text-decoration: none;
		color: var(--fg);
	}
	.qa-btn:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
	}
	.qa-btn i {
		font-size: 18px;
		color: var(--saffron);
		flex-shrink: 0;
	}
	.qa-txt {
		font-size: 13px;
		font-weight: 600;
	}
	.qa-sub {
		font-size: 11px;
		color: var(--muted-fg);
	}
</style>
