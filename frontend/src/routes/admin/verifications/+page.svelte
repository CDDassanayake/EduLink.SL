<script lang="ts">
	import { getAuthStore } from '$lib/stores/auth.svelte';
	import { getVerifications, approveVerification, rejectVerification, type TeacherVerification } from '$lib/api/admin';
	import { onMount } from 'svelte';

	let authStore = getAuthStore();
	let activeTab = $state('pending');
	let verifications = $state<TeacherVerification[]>([]);
	let isLoading = $state(true);
	let error = $state('');
	let processingId = $state<string | null>(null);

	const API_URL = 'http://localhost:8000/api/v1';

	onMount(async () => {
		await loadVerifications();
	});

	async function loadVerifications() {
		isLoading = true;
		error = '';
		try {
			const statusFilter = activeTab === 'pending' ? 'PENDING' : activeTab === 'approved' ? 'APPROVED' : 'REJECTED';
			verifications = await getVerifications(statusFilter);
		} catch (e: any) {
			error = e.message || 'Failed to load verifications';
			console.error('Error loading verifications:', e);
		} finally {
			isLoading = false;
		}
	}

	async function handleApprove(profileId: string) {
		processingId = profileId;
		try {
			await approveVerification(profileId);
			await loadVerifications();
		} catch (e: any) {
			error = e.message || 'Failed to approve verification';
			console.error('Error approving verification:', e);
		} finally {
			processingId = null;
		}
	}

	async function handleReject(profileId: string) {
		const reason = prompt('Rejection reason (optional):');
		if (reason === null) return; // User cancelled

		processingId = profileId;
		try {
			await rejectVerification(profileId, reason || undefined);
			await loadVerifications();
		} catch (e: any) {
			error = e.message || 'Failed to reject verification';
			console.error('Error rejecting verification:', e);
		} finally {
			processingId = null;
		}
	}

	function switchTab(tab: string) {
		activeTab = tab;
		loadVerifications();
	}

	function getInitials(name: string): string {
		return name.split(' ').map(n => n[0]).join('').toUpperCase();
	}

	function getAvatarColor(status: string): string {
		if (status === 'PENDING') return 'var(--saffron)';
		if (status === 'APPROVED') return 'var(--green)';
		return 'var(--red)';
	}

	function getBorderColor(status: string): string {
		if (status === 'PENDING') return 'var(--saffron)';
		if (status === 'APPROVED') return 'var(--green)';
		return 'var(--red)';
	}

	function parseDocumentUrls(urls: string | null): Array<{name: string, status: string, url: string, isBlob: boolean}> {
		if (!urls) return [];
		try {
			const docs = JSON.parse(urls);
			console.log('Parsed docs:', docs); // Debug logging
			return docs.map((doc: {name: string, url: string}, i: number) => {
				const isBlob = doc.url && doc.url.startsWith('blob:');
				let url = '';
				if (!isBlob && doc.url) {
					// If URL already starts with http, use as-is
					// If it starts with /api/v1, prepend just the base URL
					// Otherwise, prepend full API_URL
					if (doc.url.startsWith('http')) {
						url = doc.url;
					} else if (doc.url.startsWith('/api/v1')) {
						url = `http://localhost:8000${doc.url}`;
					} else {
						url = `${API_URL}${doc.url}`;
					}
				}
				const result = {
					name: doc.name || `Document ${i + 1}`,
					status: isBlob || !doc.url ? 'missing' : 'ok',
					url,
					isBlob
				};
				console.log('Processed doc:', result); // Debug logging
				return result;
			});
		} catch (e) {
			console.error('Error parsing document URLs:', e);
			return [];
		}
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
	{#if error}
		<div class="alert alert-error" style="margin: 16px 0">
			<i class="ti ti-alert-circle"></i>
			{error}
		</div>
	{/if}

	<div class="filter-bar">
		<div class="tabs" style="margin-bottom:0;border-bottom:none;background:#fff;border-radius:var(--r-sm);border:1px solid var(--border-dk);overflow:hidden">
			<div class="tab {activeTab === 'pending' ? 'active' : ''}" style="padding:7px 14px;font-size:12px" onclick={() => switchTab('pending')}>Pending <span class="tab-count">{verifications.length}</span></div>
			<div class="tab {activeTab === 'approved' ? 'active' : ''}" style="padding:7px 14px;font-size:12px" onclick={() => switchTab('approved')}>Approved</div>
			<div class="tab {activeTab === 'rejected' ? 'active' : ''}" style="padding:7px 14px;font-size:12px" onclick={() => switchTab('rejected')}>Rejected</div>
		</div>
		<div style="flex:1"></div>
	</div>

	{#if isLoading}
		<div style="text-align:center;padding:40px">
			<div class="loading-spinner"></div>
			<div style="margin-top:12px;color:var(--muted-fg)">Loading verifications...</div>
		</div>
	{:else if verifications.length === 0}
		<div class="section-card" style="text-align:center;padding:40px">
			<div style="font-size:48px;margin-bottom:16px">✓</div>
			<div style="font-size:16px;font-weight:700;margin-bottom:8px">No verifications</div>
			<div style="font-size:13px;color:var(--muted-fg)">No {activeTab} verifications to review</div>
		</div>
	{:else}
		{#each verifications as verif}
			{@const docs = parseDocumentUrls(verif.document_urls)}
			<div class="verif-card" style="border-left:3px solid {getBorderColor(verif.verification_status)}">
				<div class="vc-header">
					<div class="vc-avatar" style="background:#EEF2FF;color:#3B4FD8">{getInitials(verif.full_name)}</div>
					<div style="flex:1">
						<div class="vc-name">
							{verif.full_name}
							{#if verif.verification_status === 'PENDING'}
								<span class="badge badge-saffron">Pending</span>
							{/if}
							{#if verif.verification_status === 'APPROVED'}
								<span class="badge badge-green"><i class="ti ti-check"></i> Approved</span>
							{/if}
							{#if verif.verification_status === 'REJECTED'}
								<span class="badge badge-red"><i class="ti ti-x"></i> Rejected</span>
							{/if}
						</div>
						<div class="vc-creds">{verif.email}</div>
						<div class="vc-meta">
							{#if verif.city}
								<span class="badge badge-gray"><i class="ti ti-map-pin" style="font-size:10px"></i> {verif.city}</span>
							{/if}
							{#if verif.years_experience}
								<span class="badge badge-gray"><i class="ti ti-clock" style="font-size:10px"></i> {verif.years_experience} years experience</span>
							{/if}
						</div>
					</div>
				</div>
				{#if verif.bio}
					<div style="font-size:13px;color:var(--muted-fg);margin-bottom:12px;line-height:1.5">
						{verif.bio}
					</div>
				{/if}
				{#if docs.length > 0}
					<div style="font-size:12px;font-weight:700;color:var(--muted-fg);margin-bottom:8px;font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.4px">Submitted documents</div>
					<div class="vc-docs">
						{#each docs as doc}
							<div class="doc-chip {doc.status}">
								<i class="ti ti-file"></i> {doc.name}
								{#if !doc.isBlob}
									— <a href={doc.url} target="_blank" style="margin-left:4px;opacity:.6;text-decoration:underline"><i class="ti ti-eye" style="font-size:12px"></i> View</a>
								{:else}
									<span style="margin-left:4px;color:var(--red);font-size:11px;font-style:italic">(File not available - please resubmit)</span>
								{/if}
							</div>
						{/each}
					</div>
				{:else}
					<div style="font-size:12px;font-weight:700;color:var(--muted-fg);margin-bottom:12px;font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.4px">No documents submitted</div>
				{/if}
				{#if verif.verification_note}
					<div class="alert alert-warning" style="margin-bottom:12px"><i class="ti ti-info-circle"></i> {verif.verification_note}</div>
				{/if}
				{#if verif.verification_status === 'PENDING'}
					<div class="vc-actions">
						<button class="btn btn-success" onclick={() => handleApprove(verif.id)} disabled={processingId === verif.id}>
							{#if processingId === verif.id}
								Processing...
							{:else}
								<i class="ti ti-check"></i> Approve
							{/if}
						</button>
						<button class="btn btn-danger" onclick={() => handleReject(verif.id)} disabled={processingId === verif.id}>
							{#if processingId === verif.id}
								Processing...
							{:else}
								<i class="ti ti-x"></i> Reject
							{/if}
						</button>
					</div>
				{:else if verif.verification_status === 'APPROVED'}
					<div class="vc-actions">
						<span class="badge badge-green" style="font-size:13px;padding:6px 12px"><i class="ti ti-check"></i> Approved — Tutor can now post listings</span>
					</div>
				{:else if verif.verification_status === 'REJECTED'}
					<div class="vc-actions">
						<span class="badge badge-red" style="font-size:13px;padding:6px 12px"><i class="ti ti-x"></i> Rejected</span>
					</div>
				{/if}
			</div>
		{/each}
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
		opacity: 0.7;
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
