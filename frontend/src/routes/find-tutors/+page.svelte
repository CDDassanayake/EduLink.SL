<script lang="ts">
	import { searchTutors, type Tutor, type TutorSearchParams } from '$lib/api/tutors';
	import { getAuthStore } from '$lib/stores/auth.svelte';

	let searchSubject = $state('');
	let selectedDistrict = $state('All Districts');
	let selectedStream = $state('');
	let selectedMode = $state('');
	let minRating = $state(4.5);
	let maxPrice = $state(5000);
	let availableToday = $state(false);
	let verifiedOnly = $state(true);
	
	let tutors = $state<Tutor[]>([]);
	let isLoading = $state(false);
	let error = $state('');

	const authStore = getAuthStore();

	async function performSearch() {
		try {
			isLoading = true;
			error = '';
			
			const params: TutorSearchParams = {
				city: selectedDistrict !== 'All Districts' ? selectedDistrict : undefined,
				stream: selectedStream || undefined,
				mode: selectedMode as any || undefined,
				min_rating: minRating > 0 ? minRating : undefined,
				max_price: maxPrice > 0 ? maxPrice : undefined,
				available_today: availableToday || undefined
			};
			
			tutors = await searchTutors(params);
		} catch (err: any) {
			error = err.message || 'Failed to search tutors. Please try again.';
			console.error('Search error:', err);
		} finally {
			isLoading = false;
		}
	}

	// Initial search on load
	performSearch();
</script>

<svelte:head>
	<title>Find Tutors — EduLink SL</title>
</svelte:head>

<header class="pub-nav">
	<div class="container">
		<a href="/" class="nav-logo">EDULINK.SL</a>
		<nav class="nav-links">
			<a href="/find-tutors" class="nav-link" style="color: var(--saffron)">Find Tutors</a>
			<a href="/streams" class="nav-link">Streams</a>
			<a href="/career-guidance" class="nav-link">Career Guidance</a>
		</nav>
		<div class="nav-right">
			<a href="/auth/login" class="btn btn-ghost btn-sm">Log in</a>
			<a href="/auth/register?role=teacher" class="btn btn-primary btn-sm">Become a Tutor</a>
		</div>
	</div>
</header>

<!-- Search bar -->
<div class="search-bar-strip">
	<div class="container">
		<div class="search-bar-inner">
			<div class="sb-field" style="flex: 2">
				<i class="ti ti-search"></i>
				<input type="text" placeholder="Subject, e.g. Combined Maths, Physics..." bind:value={searchSubject} />
			</div>
			<div class="sb-field">
				<i class="ti ti-map-pin"></i>
				<select bind:value={selectedDistrict}>
					<option>All Districts</option>
					<option>Colombo</option>
					<option>Kandy</option>
					<option>Gampaha</option>
					<option>Negombo</option>
					<option>Matara</option>
					<option>Galle</option>
					<option>Kurunegala</option>
				</select>
			</div>
			<button class="btn btn-saffron btn-sm" onclick={performSearch} disabled={isLoading}>Search</button>
		</div>
	</div>
</div>

<!-- Login notice -->
{#if !authStore.user}
<div class="container" style="padding-top: 16px">
	<div class="login-gate">
		<div class="login-gate-txt"><i class="ti ti-lock" style="font-size: 14px; margin-right: 5px"></i>Log in to view full tutor profiles, check availability, and book sessions.</div>
		<a href="/auth/login?redirect=/find-tutors" class="btn btn-saffron btn-sm">Log in to book</a>
	</div>
</div>
{/if}

<div class="page-layout" style="max-width: 1100px; margin: 0 auto; padding: 0 24px">
	<!-- Filters -->
	<div class="filter-col">
		<div class="fl-head">
			<div class="fl-title">Filters</div>
			<span class="fl-clear">Clear all</span>
		</div>
		<div class="fl-section">
			<div class="fl-section-title">A/L Stream</div>
			<label class="fl-option"><input type="checkbox" checked />Physical Science<span class="fl-count">142</span></label>
			<label class="fl-option"><input type="checkbox" />Biological Science<span class="fl-count">98</span></label>
			<label class="fl-option"><input type="checkbox" />Commerce<span class="fl-count">87</span></label>
			<label class="fl-option"><input type="checkbox" />Arts & Languages<span class="fl-count">64</span></label>
			<label class="fl-option"><input type="checkbox" />O/L (Grade 9–11)<span class="fl-count">210</span></label>
			<label class="fl-option"><input type="checkbox" />University<span class="fl-count">43</span></label>
		</div>
		<div class="fl-section">
			<div class="fl-section-title">Mode</div>
			<label class="fl-option"><input type="checkbox" checked />Online<span class="fl-count">284</span></label>
			<label class="fl-option"><input type="checkbox" checked />In-person<span class="fl-count">196</span></label>
			<label class="fl-option"><input type="checkbox" />Home visit<span class="fl-count">78</span></label>
			<label class="fl-option"><input type="checkbox" />Group classes<span class="fl-count">115</span></label>
		</div>
		<div class="fl-section">
			<div class="fl-section-title">Min rating</div>
			<label class="fl-option"><input type="radio" name="rating" checked />4.5+ ★★★★★</label>
			<label class="fl-option"><input type="radio" name="rating" />4.0+ ★★★★</label>
			<label class="fl-option"><input type="radio" name="rating" />Any rating</label>
		</div>
		<div class="fl-section">
			<div class="fl-section-title">Price per hour</div>
			<div style="font-size: 12px; color: var(--muted-fg); margin-bottom: 6px">Up to LKR <strong style="color: var(--fg)">5,000</strong></div>
			<input type="range" min="500" max="10000" value="5000" style="width: 100%; accent-color: var(--saffron)" />
			<div style="display: flex; justify-content: space-between; font-size: 10px; color: var(--muted-fg); margin-top: 4px"><span>LKR 500</span><span>LKR 10,000</span></div>
		</div>
		<div class="fl-section">
			<div class="fl-section-title">Availability</div>
			<label class="fl-option"><input type="checkbox" />Available today</label>
			<label class="fl-option"><input type="checkbox" checked />Available this week</label>
			<label class="fl-option"><input type="checkbox" />Weekends only</label>
		</div>
		<div class="fl-section">
			<div class="fl-section-title">Verified only</div>
			<label class="fl-option"><input type="checkbox" checked />Show verified tutors only</label>
		</div>
	</div>

	<!-- Results -->
	<div class="results-col">
		<div class="results-header">
			<div class="results-count"><strong>{tutors.length} tutors</strong> found</div>
			<select class="sort-select">
				<option>Sort: Top Rated</option>
				<option>Sort: Price — Low to High</option>
				<option>Sort: Most Reviews</option>
				<option>Sort: Nearest</option>
			</select>
		</div>
		
		{#if isLoading}
			<div style="text-align: center; padding: 40px;">
				<div style="width: 40px; height: 40px; border: 3px solid var(--border); border-top-color: var(--saffron); border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 16px;"></div>
				<div style="color: var(--muted-fg);">Searching for tutors...</div>
			</div>
		{:else if error}
			<div style="text-align: center; padding: 40px; color: var(--error-fg);">
				<div style="font-size: 14px; margin-bottom: 8px;">{error}</div>
				<button class="btn btn-saffron btn-sm" onclick={performSearch}>Try again</button>
			</div>
		{:else if tutors.length === 0}
			<div style="text-align: center; padding: 40px; color: var(--muted-fg);">
				<div style="font-size: 16px; margin-bottom: 8px;">No tutors found matching your criteria</div>
				<div style="font-size: 13px;">Try adjusting your filters or search terms</div>
			</div>
		{:else}
			<div class="tutors-list">
				{#each tutors as tutor}
					<a href="/tutor/{tutor.id}" style="display: block">
						<div class="tutor-list-card">
							<div class="tlc-photo" style="background: #EEF2FF; color: #3B4FD8">
								{#if tutor.profile_photo_url}
									<img src={tutor.profile_photo_url} alt={tutor.full_name} style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--r-sm);" />
								{:else}
									{tutor.full_name.split(' ').map(n => n[0]).join('')}
								{/if}
							</div>
							<div class="tlc-body">
								<div class="tlc-top">
									<div>
										<div class="tlc-name">{tutor.full_name}</div>
										<div class="tlc-specialty">
											{#each tutor.listings.slice(0, 2) as listing}
												{listing.mode} · {listing.class_type}
											{/each}
										</div>
										<div class="tlc-metrics">
											<span class="badge-merit">MERIT {tutor.merit_score}</span>
											<span class="tlc-rating">
												<span style="color: var(--saffron)">★</span> {tutor.average_rating?.toFixed(1) || 'N/A'}
											</span>
											<span style="font-size: 12px; color: var(--muted-fg)">({tutor.review_count} reviews)</span>
										</div>
									</div>
									<div class="tlc-right">
										<div class="tlc-price">
											LKR {tutor.listings[0]?.hourly_rate.toLocaleString() || 'N/A'}<span>/hr</span>
										</div>
										<span class="btn btn-outline btn-sm" style="border-radius: 100px">View profile →</span>
									</div>
								</div>
								<div class="tlc-tags">
									{#each tutor.listings.slice(0, 3) as listing}
										<span class="tag">{listing.mode}</span>
									{/each}
									{#if tutor.listings.length > 3}
										<span class="tag">+{tutor.listings.length - 3} more</span>
									{/if}
								</div>
							</div>
						</div>
					</a>
				{/each}
			</div>
		{/if}
	</div>
</div>

<footer class="pub-footer" style="margin-top: 0">
	<div class="container">
		<div class="footer-bottom">
			<div class="footer-logo" style="font-size: 14px">EDULINK.SL</div>
			<div>© 2026 EduLink Sri Lanka. Empowering the next generation.</div>
		</div>
	</div>
</footer>

<style>
	.search-bar-strip {
		background: #fff;
		border-bottom: 1px solid var(--border-dk);
		padding: 16px 0;
	}
	.search-bar-inner {
		display: flex;
		gap: 8px;
		align-items: center;
	}
	.sb-field {
		display: flex;
		align-items: center;
		gap: 8px;
		background: var(--bg);
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		padding: 9px 14px;
		flex: 1;
		transition: border-color 0.15s;
	}
	.sb-field:focus-within {
		border-color: var(--saffron);
	}
	.sb-field i {
		font-size: 16px;
		color: var(--muted-fg);
		flex-shrink: 0;
	}
	.sb-field input,
	.sb-field select {
		border: none;
		outline: none;
		font-size: 13px;
		color: var(--fg);
		font-family: var(--ff);
		background: transparent;
		width: 100%;
	}
	.page-layout {
		display: grid;
		grid-template-columns: 240px 1fr;
		gap: 0;
		min-height: calc(100vh - 60px);
	}
	.filter-col {
		background: #fff;
		border-right: 1px solid var(--border-dk);
		padding: 20px;
		overflow-y: auto;
	}
	.fl-head {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20px;
	}
	.fl-title {
		font-size: 13px;
		font-weight: 700;
		color: var(--fg);
	}
	.fl-clear {
		font-size: 12px;
		color: var(--saffron);
		font-weight: 600;
		cursor: pointer;
	}
	.fl-section {
		margin-bottom: 20px;
	}
	.fl-section-title {
		font-size: 10px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.6px;
		color: var(--muted-fg);
		margin-bottom: 10px;
	}
	.fl-option {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 5px 0;
		cursor: pointer;
		font-size: 13px;
		color: var(--fg);
	}
	.fl-option input {
		accent-color: var(--saffron);
		cursor: pointer;
	}
	.fl-count {
		margin-left: auto;
		font-size: 11px;
		font-family: var(--ff-mono);
		background: var(--muted);
		color: var(--muted-fg);
		padding: 1px 7px;
		border-radius: 100px;
		font-weight: 600;
	}
	.results-col {
		background: var(--bg);
		padding: 20px 24px;
	}
	.results-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 16px;
	}
	.results-count {
		font-size: 13px;
		color: var(--muted-fg);
	}
	.results-count strong {
		color: var(--fg);
		font-weight: 700;
	}
	.sort-select {
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		padding: 7px 12px;
		font-size: 13px;
		font-family: var(--ff);
		color: var(--fg);
		background: #fff;
	}
	.tutors-list {
		display: flex;
		flex-direction: column;
		gap: 12px;
	}
	.tutor-list-card {
		background: #fff;
		border-radius: var(--r);
		border: 1px solid var(--border-dk);
		padding: 20px;
		display: flex;
		gap: 16px;
		align-items: flex-start;
		transition: all 0.2s;
		cursor: pointer;
	}
	.tutor-list-card:hover {
		box-shadow: var(--sh-md);
		border-color: rgba(232, 147, 14, 0.3);
		transform: translateY(-1px);
	}
	.tlc-photo {
		width: 64px;
		height: 64px;
		border-radius: var(--r-sm);
		background: var(--muted);
		flex-shrink: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 22px;
		font-weight: 800;
		color: var(--primary);
	}
	.tlc-body {
		flex: 1;
		min-width: 0;
	}
	.tlc-top {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		gap: 12px;
		margin-bottom: 6px;
	}
	.tlc-name {
		font-size: 16px;
		font-weight: 700;
		display: flex;
		align-items: center;
		gap: 6px;
	}
	.tlc-specialty {
		font-size: 13px;
		color: var(--muted-fg);
		margin-bottom: 8px;
	}
	.tlc-metrics {
		display: flex;
		align-items: center;
		gap: 10px;
		margin-bottom: 8px;
		flex-wrap: wrap;
	}
	.tlc-rating {
		display: flex;
		align-items: center;
		gap: 4px;
		font-size: 13px;
		font-weight: 600;
	}
	.tlc-tags {
		display: flex;
		flex-wrap: wrap;
		gap: 6px;
	}
	.tlc-right {
		text-align: right;
		flex-shrink: 0;
	}
	.tlc-price {
		font-size: 17px;
		font-weight: 800;
		color: var(--fg);
		margin-bottom: 8px;
	}
	.tlc-price span {
		font-size: 12px;
		font-weight: 400;
		color: var(--muted-fg);
	}
	.login-gate {
		background: var(--saffron-lt);
		border: 1.5px solid rgba(232, 147, 14, 0.3);
		border-radius: var(--r);
		padding: 14px 18px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 12px;
		margin-bottom: 16px;
	}
	.login-gate-txt {
		font-size: 13px;
		color: var(--saffron-hv);
		font-weight: 500;
	}
	@keyframes spin {
		to { transform: rotate(360deg); }
	}
</style>
