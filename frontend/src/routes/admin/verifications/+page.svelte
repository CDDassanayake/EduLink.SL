<script lang="ts">
	let activeTab = $state('pending');

	let verifications = $state([
		{
			id: 1,
			name: 'Sachini Wickramasinghe',
			avatar: 'SW',
			avatarBg: 'var(--saffron-lt)',
			avatarColor: 'var(--saffron-hv)',
			creds: 'BSc IT, University of Moratuwa · Wants to teach: ICT, Computer Science',
			meta: ['Malabe, Colombo', 'Applied 2 days ago', '3 years experience'],
			docs: [
				{ name: 'NIC front', status: 'ok' },
				{ name: 'NIC back', status: 'ok' },
				{ name: 'Degree certificate', status: 'ok' },
				{ name: 'Transcript', status: 'missing' }
			],
			status: 'pending',
			borderColor: 'var(--saffron)'
		},
		{
			id: 2,
			name: 'Pradeep Abeysekara',
			avatar: 'PA',
			avatarBg: '#EEF9F7',
			avatarColor: 'var(--teal)',
			creds: 'BSc Chemistry, University of Kelaniya · Wants to teach: Chemistry, Biology',
			meta: ['Gampaha', 'Applied 3 days ago', '5 years experience'],
			docs: [
				{ name: 'NIC front', status: 'ok' },
				{ name: 'NIC back', status: 'ok' },
				{ name: 'Degree certificate', status: 'ok' },
				{ name: 'A/L results sheet', status: 'ok' }
			],
			status: 'pending',
			borderColor: 'var(--saffron)'
		},
		{
			id: 3,
			name: 'Lakmali Fernando',
			avatar: 'LF',
			avatarBg: '#FDF4FF',
			avatarColor: '#7C3AED',
			creds: 'BA English, University of Sri Jayewardenepura · Wants to teach: English Language & Literature',
			meta: ['Kandy', 'Applied 5 days ago'],
			docs: [
				{ name: 'NIC front', status: 'ok' },
				{ name: 'NIC back', status: 'ok' },
				{ name: 'Degree certificate', status: 'missing' },
				{ name: 'A/L results', status: 'missing' }
			],
			status: 'pending',
			borderColor: 'var(--red)',
			hasWarning: true
		},
		{
			id: 4,
			name: 'Malith Ratnayake',
			avatar: 'MR',
			avatarBg: '#F0FDF4',
			avatarColor: '#166534',
			creds: 'BBA (Hons), University of Sri Jayewardenepura · Wants to teach: Accounting, Economics, Business Studies',
			meta: ['Dehiwala', 'Applied today', '4 years experience'],
			docs: [
				{ name: 'NIC front', status: 'ok' },
				{ name: 'NIC back', status: 'ok' },
				{ name: 'Degree certificate', status: 'ok' },
				{ name: 'Employment letter', status: 'pending' }
			],
			status: 'pending',
			borderColor: 'var(--saffron)'
		}
	]);

	function approveVerif(id: number) {
		verifications = verifications.map(v => 
			v.id === id 
				? { ...v, status: 'approved', borderColor: 'var(--green)' }
				: v
		);
	}

	function rejectVerif(id: number) {
		verifications = verifications.map(v => 
			v.id === id 
				? { ...v, status: 'rejected', borderColor: 'var(--red)' }
				: v
		);
	}

	function switchTab(tab: string) {
		activeTab = tab;
	}
</script>

<svelte:head>
	<title>Verifications — EduLink SL</title>
</svelte:head>

<div class="app-topbar admin-topbar">
	<div class="app-topbar-title">Teacher Verifications</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i><div class="notif-dot"></div></div>
		<button class="btn btn-ghost btn-sm" style="border-color:rgba(255,255,255,.15);color:rgba(255,255,255,.7)"><i class="ti ti-download"></i> Export</button>
	</div>
</div>

<div class="app-content">
	<div class="filter-bar">
		<div class="tabs" style="margin-bottom:0;border-bottom:none;background:#fff;border-radius:var(--r-sm);border:1px solid var(--border-dk);overflow:hidden">
			<div class="tab {activeTab === 'pending' ? 'active' : ''}" style="padding:7px 14px;font-size:12px" onclick={() => switchTab('pending')}>Pending <span class="tab-count">4</span></div>
			<div class="tab {activeTab === 'approved' ? 'active' : ''}" style="padding:7px 14px;font-size:12px" onclick={() => switchTab('approved')}>Approved <span style="background:var(--green-lt);color:var(--green);font-size:10px;font-weight:700;padding:1px 6px;border-radius:100px;margin-left:4px;font-family:var(--ff-mono)">142</span></div>
			<div class="tab {activeTab === 'rejected' ? 'active' : ''}" style="padding:7px 14px;font-size:12px" onclick={() => switchTab('rejected')}>Rejected <span style="background:var(--red-lt);color:var(--red);font-size:10px;font-weight:700;padding:1px 6px;border-radius:100px;margin-left:4px;font-family:var(--ff-mono)">18</span></div>
		</div>
		<div style="flex:1"></div>
		<div style="position:relative">
			<i class="ti ti-search" style="position:absolute;left:10px;top:50%;transform:translateY(-50%);font-size:14px;color:var(--muted-fg)"></i>
			<input class="form-input" placeholder="Search by name, subject..." style="padding-left:34px;width:220px;padding-top:8px;padding-bottom:8px" />
		</div>
	</div>

	{#each verifications as verif}
		<div class="verif-card" style="border-left:3px solid {verif.borderColor}">
			<div class="vc-header">
				<div class="vc-avatar" style="background:{verif.avatarBg};color:{verif.avatarColor}">{verif.avatar}</div>
				<div style="flex:1">
					<div class="vc-name">
						{verif.name}
						{#if verif.status === 'pending'}
							<span class="badge badge-saffron">Pending</span>
						{/if}
						{#if verif.status === 'approved'}
							<span class="badge badge-green"><i class="ti ti-check"></i> Approved</span>
						{/if}
						{#if verif.status === 'rejected'}
							<span class="badge badge-red"><i class="ti ti-x"></i> Rejected</span>
						{/if}
						{#if verif.hasWarning}
							<span class="badge badge-red"><i class="ti ti-alert-circle" style="font-size:10px"></i> Docs missing</span>
						{/if}
					</div>
					<div class="vc-creds">{verif.creds}</div>
					<div class="vc-meta">
						{#each verif.meta as m}
							<span class="badge badge-gray"><i class="ti ti-map-pin" style="font-size:10px"></i> {m}</span>
						{/each}
					</div>
				</div>
			</div>
			<div style="font-size:12px;font-weight:700;color:var(--muted-fg);margin-bottom:8px;font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.4px">Submitted documents</div>
			<div class="vc-docs">
				{#each verif.docs as doc}
					<div class="doc-chip {doc.status}">
						{#if doc.status === 'ok'}
							<i class="ti ti-id-badge"></i> {doc.name} — Uploaded <i class="ti ti-eye" style="font-size:12px;margin-left:4px;opacity:.6"></i>
						{/if}
						{#if doc.status === 'missing'}
							<i class="ti ti-file-unknown"></i> {doc.name} — Not submitted
						{/if}
						{#if doc.status === 'pending'}
							<i class="ti ti-clock"></i> {doc.name} — Under review
						{/if}
					</div>
				{/each}
			</div>
			{#if verif.hasWarning}
				<div class="alert alert-warning" style="margin-bottom:12px"><i class="ti ti-clock"></i> Already requested documents on 20 Jun. No response yet. Consider rejecting if no response by 27 Jun.</div>
			{/if}
			{#if verif.status === 'pending'}
				<div class="vc-actions">
					<button class="btn btn-success" onclick={() => approveVerif(verif.id)}><i class="ti ti-check"></i> Approve</button>
					<button class="btn btn-danger" onclick={() => rejectVerif(verif.id)}><i class="ti ti-x"></i> Reject</button>
					<button class="btn btn-ghost btn-sm"><i class="ti ti-message"></i> Request more docs</button>
					<button class="btn btn-ghost btn-sm"><i class="ti ti-eye"></i> View documents</button>
				</div>
			{:else if verif.status === 'approved'}
				<div class="vc-actions">
					<span class="badge badge-green" style="font-size:13px;padding:6px 12px"><i class="ti ti-check"></i> Approved — Tutor notified by email</span>
				</div>
			{:else if verif.status === 'rejected'}
				<div class="vc-actions">
					<span class="badge badge-red" style="font-size:13px;padding:6px 12px"><i class="ti ti-x"></i> Rejected — Tutor notified</span>
				</div>
			{/if}
		</div>
	{/each}
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
		border-bottom: 1px solid rgba(255,255,255,.06);
	}
	.admin-topbar .app-topbar-title {
		color: #fff;
	}
	.admin-topbar .notif-btn {
		background: rgba(255,255,255,.06);
		border-color: rgba(255,255,255,.1);
		color: rgba(255,255,255,.6);
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
	.verif-card {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		padding: 18px 20px;
		margin-bottom: 12px;
		transition: box-shadow .15s;
	}
	.verif-card:hover {
		box-shadow: var(--sh-sm);
	}
	.vc-header {
		display: flex;
		gap: 14px;
		align-items: flex-start;
		margin-bottom: 12px;
	}
	.vc-avatar {
		width: 52px;
		height: 52px;
		border-radius: var(--r-sm);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 17px;
		font-weight: 800;
		flex-shrink: 0;
	}
	.vc-name {
		font-size: 15px;
		font-weight: 800;
		margin-bottom: 2px;
		display: flex;
		align-items: center;
		gap: 8px;
	}
	.vc-creds {
		font-size: 13px;
		color: var(--muted-fg);
	}
	.vc-meta {
		display: flex;
		flex-wrap: wrap;
		gap: 6px;
		margin-top: 6px;
	}
	.vc-docs {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
		margin-bottom: 14px;
	}
	.doc-chip {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 6px 12px;
		border-radius: var(--r-sm);
		font-size: 12px;
		font-weight: 500;
		border: 1.5px solid var(--border-dk);
		cursor: pointer;
		transition: all .15s;
		background: #fff;
	}
	.doc-chip:hover {
		border-color: var(--primary);
		background: var(--bg);
	}
	.doc-chip.ok {
		background: var(--green-lt);
		border-color: #A7F3D0;
		color: var(--green);
	}
	.doc-chip.missing {
		background: var(--red-lt);
		border-color: #FECACA;
		color: var(--red);
	}
	.doc-chip.pending {
		background: var(--saffron-lt);
		border-color: #FDE68A;
		color: var(--saffron-hv);
	}
	.vc-actions {
		display: flex;
		gap: 8px;
		align-items: center;
	}
	.filter-bar {
		display: flex;
		gap: 10px;
		align-items: center;
		margin-bottom: 20px;
		flex-wrap: wrap;
	}
</style>
