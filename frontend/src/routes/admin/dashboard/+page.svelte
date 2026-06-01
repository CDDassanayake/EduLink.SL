<script lang="ts">
</script>

<svelte:head>
	<title>Admin Dashboard — EduLink SL</title>
</svelte:head>

<div class="app-topbar admin-topbar">
	<div class="app-topbar-title">Platform Analytics</div>
	<div class="app-topbar-right">
		<select class="form-input" style="width: auto; padding: 6px 12px; font-size: 12px; background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.1); color: rgba(255,255,255,0.8)">
			<option>Last 30 days</option>
			<option>Last 7 days</option>
			<option>Last 90 days</option>
			<option>This year</option>
		</select>
		<div class="notif-btn"><i class="ti ti-bell"></i><div class="notif-dot"></div></div>
		<button class="btn btn-ghost btn-sm" style="border-color: rgba(255,255,255,0.15); color: rgba(255,255,255,0.7)"><i class="ti ti-download"></i> Export</button>
	</div>
</div>

<div class="app-content">
	<!-- KPI cards -->
	<div class="kpi-grid">
		<div class="stat-box stat-teal">
			<div class="stat-label"><i class="ti ti-users"></i> Total users</div>
			<div class="stat-value">4,284</div>
			<div class="stat-sub" style="color: var(--green)"><i class="ti ti-trending-up" style="font-size: 11px"></i> +234 this month</div>
		</div>
		<div class="stat-box stat-saffron">
			<div class="stat-label"><i class="ti ti-calendar-check"></i> Bookings (Jun)</div>
			<div class="stat-value">1,847</div>
			<div class="stat-sub" style="color: var(--green)"><i class="ti ti-trending-up" style="font-size: 11px"></i> +18% vs May</div>
		</div>
		<div class="stat-box stat-green">
			<div class="stat-label"><i class="ti ti-coin"></i> GMV (Jun)</div>
			<div class="stat-value" style="font-size: 18px">LKR 4.2M</div>
			<div class="stat-sub" style="color: var(--green)"><i class="ti ti-trending-up" style="font-size: 11px"></i> +22% vs May</div>
		</div>
		<div class="stat-box stat-primary">
			<div class="stat-label"><i class="ti ti-building-bank"></i> Platform revenue</div>
			<div class="stat-value" style="font-size: 18px">LKR 420k</div>
			<div class="stat-sub">10% commission</div>
		</div>
	</div>

	<div class="grid-2" style="margin-bottom: 20px; align-items: start">
		<!-- Bookings chart -->
		<div class="section-card">
			<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px">
				<div style="font-size: 14px; font-weight: 700">Monthly bookings</div>
				<span class="badge badge-green"><i class="ti ti-trending-up"></i> +68% YTD</span>
			</div>
			<div class="chart-container">
				<div class="bar-col"><div class="bar-val">420</div><div class="bar-fill" style="height: 23%; background: #EEF2FF; border-top: 2px solid var(--primary)"></div><div class="bar-lbl">Jan</div></div>
				<div class="bar-col"><div class="bar-val">580</div><div class="bar-fill" style="height: 31%; background: #EEF2FF; border-top: 2px solid var(--primary)"></div><div class="bar-lbl">Feb</div></div>
				<div class="bar-col"><div class="bar-val">820</div><div class="bar-fill" style="height: 44%; background: #EEF2FF; border-top: 2px solid var(--primary)"></div><div class="bar-lbl">Mar</div></div>
				<div class="bar-col"><div class="bar-val">1,100</div><div class="bar-fill" style="height: 60%; background: #EEF2FF; border-top: 2px solid var(--primary)"></div><div class="bar-lbl">Apr</div></div>
				<div class="bar-col"><div class="bar-val">1,560</div><div class="bar-fill" style="height: 84%; background: #EEF2FF; border-top: 2px solid var(--primary)"></div><div class="bar-lbl">May</div></div>
				<div class="bar-col"><div class="bar-val" style="color: var(--saffron); font-weight: 800">1,847</div><div class="bar-fill" style="height: 100%; background: var(--saffron-lt); border-top: 2px solid var(--saffron)"></div><div class="bar-lbl" style="color: var(--saffron); font-weight: 700">Jun</div></div>
			</div>
		</div>

		<!-- Top tutors -->
		<div class="card" style="overflow: hidden">
			<div style="padding: 14px 16px; border-bottom: 1px solid var(--border-dk); font-size: 14px; font-weight: 700; display: flex; align-items: center; justify-content: space-between">
				Top tutors by revenue
				<a href="/admin/tutors" style="font-size: 12px; color: var(--saffron); font-weight: 600">View all</a>
			</div>
			<div class="top-tutor-row">
				<span class="rank">1</span>
				<div style="width: 30px; height: 30px; border-radius: 50%; background: #F0FDF4; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; color: #166534; flex-shrink: 0">RS</div>
				<div style="flex: 1"><div style="font-size: 12px; font-weight: 700">Dr. Rohan Silva</div><div style="font-size: 11px; color: var(--muted-fg)">Chemistry</div></div>
				<div style="text-align: right"><div style="font-size: 12px; font-weight: 800">LKR 84k</div><span class="badge-merit" style="font-size: 9px">MERIT 99</span></div>
			</div>
			<div class="top-tutor-row">
				<span class="rank">2</span>
				<div style="width: 30px; height: 30px; border-radius: 50%; background: #EEF2FF; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; color: #3B4FD8; flex-shrink: 0">AP</div>
				<div style="flex: 1"><div style="font-size: 12px; font-weight: 700">Aruna Perera</div><div style="font-size: 11px; color: var(--muted-fg)">Physics</div></div>
				<div style="text-align: right"><div style="font-size: 12px; font-weight: 800">LKR 72k</div><span class="badge-merit" style="font-size: 9px">MERIT 98</span></div>
			</div>
			<div class="top-tutor-row">
				<span class="rank">3</span>
				<div style="width: 30px; height: 30px; border-radius: 50%; background: #FFF0E0; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; color: #A06000; flex-shrink: 0">DJ</div>
				<div style="flex: 1"><div style="font-size: 12px; font-weight: 700">Dilini Jayasuriya</div><div style="font-size: 11px; color: var(--muted-fg)">Maths</div></div>
				<div style="text-align: right"><div style="font-size: 12px; font-weight: 800">LKR 58k</div><span class="badge-merit" style="font-size: 9px">MERIT 94</span></div>
			</div>
			<div class="top-tutor-row">
				<span class="rank">4</span>
				<div style="width: 30px; height: 30px; border-radius: 50%; background: #FDF4FF; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; color: #7C3AED; flex-shrink: 0">NK</div>
				<div style="flex: 1"><div style="font-size: 12px; font-weight: 700">Nadeesha Kumari</div><div style="font-size: 11px; color: var(--muted-fg)">Biology</div></div>
				<div style="text-align: right"><div style="font-size: 12px; font-weight: 800">LKR 41k</div><span class="badge-merit" style="font-size: 9px">MERIT 91</span></div>
			</div>
		</div>
	</div>

	<div class="grid-2" style="align-items: start">
		<!-- Subject breakdown -->
		<div class="section-card">
			<div style="font-size: 14px; font-weight: 700; margin-bottom: 14px">Bookings by subject (June)</div>
			<div style="display: flex; flex-direction: column; gap: 10px">
				<div><div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px"><span style="font-weight: 600">A/L Mathematics</span><span class="font-mono" style="font-weight: 700">487 <span style="color: var(--muted-fg); font-weight: 400">(26%)</span></span></div><div class="breakdown-bar"><div class="breakdown-fill" style="width: 26%; background: var(--teal)"></div></div></div>
				<div><div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px"><span style="font-weight: 600">Chemistry</span><span class="font-mono" style="font-weight: 700">342 <span style="color: var(--muted-fg); font-weight: 400">(19%)</span></span></div><div class="breakdown-bar"><div class="breakdown-fill" style="width: 19%; background: var(--saffron)"></div></div></div>
				<div><div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px"><span style="font-weight: 600">Physics</span><span class="font-mono" style="font-weight: 700">298 <span style="color: var(--muted-fg); font-weight: 400">(16%)</span></span></div><div class="breakdown-bar"><div class="breakdown-fill" style="width: 16%; background: var(--primary)"></div></div></div>
				<div><div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px"><span style="font-weight: 600">O/L Mathematics</span><span class="font-mono" style="font-weight: 700">256 <span style="color: var(--muted-fg); font-weight: 400">(14%)</span></span></div><div class="breakdown-bar"><div class="breakdown-fill" style="width: 14%; background: #7C3AED"></div></div></div>
				<div><div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px"><span style="font-weight: 600">English</span><span class="font-mono" style="font-weight: 700">210 <span style="color: var(--muted-fg); font-weight: 400">(11%)</span></span></div><div class="breakdown-bar"><div class="breakdown-fill" style="width: 11%; background: var(--green)"></div></div></div>
				<div><div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px"><span style="font-weight: 600">Others</span><span class="font-mono" style="font-weight: 700">254 <span style="color: var(--muted-fg); font-weight: 400">(14%)</span></span></div><div class="breakdown-bar"><div class="breakdown-fill" style="width: 14%; background: var(--muted-fg)"></div></div></div>
			</div>
		</div>

		<!-- Recent activity -->
		<div class="section-card">
			<div style="font-size: 14px; font-weight: 700; margin-bottom: 12px">Recent platform activity</div>
			<div class="activity-item">
				<div class="act-icon" style="background: var(--green-lt); color: var(--green)"><i class="ti ti-shield-check"></i></div>
				<div><div class="act-text"><strong>Sachini Wickramasinghe</strong> approved as verified tutor (ICT)</div><div class="act-time">8 minutes ago</div></div>
			</div>
			<div class="activity-item">
				<div class="act-icon" style="background: var(--saffron-lt); color: var(--saffron)"><i class="ti ti-calendar-check"></i></div>
				<div><div class="act-text"><strong>62 new bookings</strong> made in the last 24 hours</div><div class="act-time">Ongoing today</div></div>
			</div>
			<div class="activity-item">
				<div class="act-icon" style="background: var(--red-lt); color: var(--red)"><i class="ti ti-flag"></i></div>
				<div><div class="act-text">Review by <strong>anonymous</strong> flagged for inappropriate content on Dr. Rohan's profile</div><div class="act-time">2 hours ago</div></div>
			</div>
			<div class="activity-item">
				<div class="act-icon" style="background: var(--teal-lt); color: var(--teal)"><i class="ti ti-user-plus"></i></div>
				<div><div class="act-text"><strong>38 new registrations</strong> today — 26 students, 12 teachers</div><div class="act-time">Today</div></div>
			</div>
			<div class="activity-item">
				<div class="act-icon" style="background: #EEF2FF; color: var(--primary)"><i class="ti ti-coin"></i></div>
				<div><div class="act-text"><strong>Weekly payouts</strong> processed — LKR 1.8M disbursed to 142 teachers</div><div class="act-time">Yesterday</div></div>
			</div>
			<div class="activity-item">
				<div class="act-icon" style="background: var(--saffron-lt); color: var(--saffron-hv)"><i class="ti ti-alert-triangle"></i></div>
				<div><div class="act-text">New <strong>dispute raised</strong> — Kasun J. vs. booking #BK-8841</div><div class="act-time">3 hours ago · <a href="/admin/disputes" style="color: var(--saffron); font-weight: 600">Review</a></div></div>
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
	.admin-topbar {
		background: #0A0F2A;
		border-bottom: 1px solid rgba(255, 255, 255, 0.06);
	}
	.admin-topbar .app-topbar-title {
		color: #fff;
	}
	.admin-topbar .notif-btn {
		background: rgba(255, 255, 255, 0.06);
		border-color: rgba(255, 255, 255, 0.1);
		color: rgba(255, 255, 255, 0.6);
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
		background: var(--bg);
	}
	.kpi-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 14px;
		margin-bottom: 20px;
	}
	.activity-item {
		display: flex;
		align-items: flex-start;
		gap: 10px;
		padding: 10px 0;
		border-bottom: 1px solid var(--border);
	}
	.activity-item:last-child {
		border-bottom: none;
	}
	.act-icon {
		width: 30px;
		height: 30px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 13px;
		flex-shrink: 0;
		margin-top: 1px;
	}
	.act-text {
		flex: 1;
		font-size: 13px;
		color: var(--fg);
		line-height: 1.45;
	}
	.act-time {
		font-size: 11px;
		color: var(--muted-fg);
		margin-top: 2px;
	}
	.chart-container {
		height: 140px;
		display: flex;
		align-items: flex-end;
		gap: 6px;
		padding: 0 4px;
	}
	.bar-col {
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 3px;
	}
	.bar-fill {
		width: 100%;
		border-radius: 4px 4px 0 0;
		min-height: 4px;
	}
	.bar-val {
		font-size: 9px;
		font-family: var(--ff-mono);
		font-weight: 700;
		color: var(--muted-fg);
	}
	.bar-lbl {
		font-size: 9px;
		color: var(--muted-fg);
	}
	.top-tutor-row {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 10px 14px;
		border-bottom: 1px solid var(--border);
		font-size: 13px;
	}
	.top-tutor-row:last-child {
		border-bottom: none;
	}
	.rank {
		width: 20px;
		font-family: var(--ff-mono);
		font-size: 11px;
		font-weight: 700;
		color: var(--muted-fg);
		text-align: center;
	}
	.breakdown-bar {
		height: 6px;
		background: var(--muted);
		border-radius: 100px;
		overflow: hidden;
		flex: 1;
	}
	.breakdown-fill {
		height: 100%;
		border-radius: 100px;
	}
</style>
