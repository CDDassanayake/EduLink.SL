<script lang="ts">
	import { getAuthStore } from '$lib/stores/auth.svelte';
	import { getPendingListings, approveListing, rejectListing } from '$lib/api/admin';
	import { onMount } from 'svelte';

	let authStore = getAuthStore();
	let listings = $state<any[]>([]);
	let isLoading = $state(true);
	let error = $state('');
	let processingId = $state<string | null>(null);

	onMount(async () => {
		if (authStore.user?.role !== 'ADMIN') {
			window.location.href = '/auth/login';
			return;
		}
		await loadPendingListings();
	});

	async function loadPendingListings() {
		isLoading = true;
		error = '';
		try {
			listings = await getPendingListings();
		} catch (e: any) {
			error = e.message || 'Failed to load pending listings';
			console.error('Error loading listings:', e);
		} finally {
			isLoading = false;
		}
	}

	async function handleApprove(listingId: string) {
		processingId = listingId;
		try {
			await approveListing(listingId);
			listings = listings.filter(l => l.id !== listingId);
		} catch (e: any) {
			error = e.message || 'Failed to approve listing';
			console.error('Error approving listing:', e);
		} finally {
			processingId = null;
		}
	}

	async function handleReject(listingId: string) {
		if (!confirm('Are you sure you want to reject this listing?')) return;
		
		processingId = listingId;
		try {
			await rejectListing(listingId);
			listings = listings.filter(l => l.id !== listingId);
		} catch (e: any) {
			error = e.message || 'Failed to reject listing';
			console.error('Error rejecting listing:', e);
		} finally {
			processingId = null;
		}
	}
</script>

<svelte:head>
	<title>Listing Approvals — EduLink SL</title>
</svelte:head>

<div class="app-topbar admin-topbar">
	<div class="app-topbar-title">Listing Approvals</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i><div class="notif-dot"></div></div>
	</div>
</div>

{#if error}
	<div class="alert alert-error" style="margin: 16px 0">
		<i class="ti ti-alert-circle"></i>
		{error}
	</div>
{/if}

<div class="app-content">
	{#if isLoading}
		<div style="text-align:center;padding:40px">
			<div class="loading-spinner"></div>
			<div style="margin-top:12px;color:var(--muted-fg)">Loading pending listings...</div>
		</div>
	{:else if listings.length === 0}
		<div class="section-card" style="text-align:center;padding:40px">
			<div style="font-size:48px;margin-bottom:16px">✓</div>
			<div style="font-size:16px;font-weight:700;margin-bottom:8px">All caught up!</div>
			<div style="font-size:13px;color:var(--muted-fg)">No pending listings to review</div>
		</div>
	{:else}
		<div style="display:flex;flex-direction:column;gap:16px">
			{#each listings as listing}
				<div class="section-card">
					<div style="display:flex;gap:16px;align-items:flex-start">
						<div style="width:48px;height:48px;border-radius:var(--r-sm);background:#EEF2FF;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800;color:#3B4FD8;flex-shrink:0">
							{listing.user?.full_name?.split(' ').map(n => n[0]).join('').toUpperCase() || 'T'}
						</div>
						<div style="flex:1">
							<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
								<div style="font-size:14px;font-weight:700">{listing.user?.full_name || 'Unknown'}</div>
								<span class="badge badge-saffron">PENDING</span>
							</div>
							<div style="font-size:12px;color:var(--muted-fg);margin-bottom:8px">
								{listing.subject?.name || 'Unknown Subject'} · {listing.mode} · {listing.class_type}
							</div>
							<div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px">
								<span class="badge badge-primary">{listing.subject?.category || 'N/A'}</span>
								<span class="badge badge-teal">{listing.mode}</span>
								<span class="badge badge-primary">{listing.class_type}</span>
							</div>
							<div style="font-size:13px;color:var(--muted-fg);margin-bottom:12px;line-height:1.5">
								{listing.description || 'No description provided'}
							</div>
							<div style="display:flex;align-items:center;justify-content:space-between">
								<div style="font-size:15px;font-weight:800">
									LKR {Number(listing.hourly_rate).toLocaleString()}
									<span style="font-size:11px;font-weight:400;color:var(--muted-fg)">/hr</span>
								</div>
								<div style="display:flex;gap:8px">
									<button 
										class="btn btn-outline btn-sm" 
										onclick={() => handleReject(listing.id)}
										disabled={processingId === listing.id}
									>
										{processingId === listing.id ? 'Processing...' : 'Reject'}
									</button>
									<button 
										class="btn btn-primary btn-sm" 
										onclick={() => handleApprove(listing.id)}
										disabled={processingId === listing.id}
									>
										{processingId === listing.id ? 'Processing...' : 'Approve'}
									</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
