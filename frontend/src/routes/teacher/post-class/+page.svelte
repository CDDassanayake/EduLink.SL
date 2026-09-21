<script lang="ts">
	import { getAuthStore } from '$lib/stores/auth.svelte';
	import { getSubjects, createListing } from '$lib/api/tutors';
	import { createListingPayment } from '$lib/api/payments';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { loadStripe } from '@stripe/stripe-js';

	console.log('=== Component script running ===');

	let authStore = getAuthStore();
	let currentStep = $state(1);
	let selectedPlan = $state('STANDARD');
	let subjects = $state<any[]>([]);
	let isLoading = $state(false);
	let error = $state('');
	let createdListingId = $state<string | null>(null);
	let paymentClientSecret = $state<string | null>(null);
	let paymentIntentId = $state<string | null>(null);
	let stripe: any = null;
	let cardElement: any = null;

	// Form fields
	let subjectId = $state('');
	let subjectSearch = $state('');
	let subjectName = $state('');
	let level = $state('AL_SCIENCE');
	let classType = $state('Individual (1-on-1)');
	let teachingMode = $state('Online');
	let language = $state('English');
	let hourlyRate = $state('3500');
	let sessionDuration = $state('1.5 hours');
	let classDescription = $state('Comprehensive A/L Physics covering all theory topics with extensive past paper practice. I focus on building conceptual clarity before moving to problem-solving. Special emphasis on the National Exam question patterns for the past 10 years.');
	let freeTrial = $state(false);
	let showSubjectDropdown = $state(false);

	const stepLabels = ['', 'Class details', 'Choose a plan', 'Payment'];

	// Initialize Stripe
	onMount(async () => {
		const key = import.meta.env.PUBLIC_STRIPE_PUBLISHABLE_KEY || 'pk_test_51UBU9rDGNHZe2KSIYINoqkGmhHFTg80twLKQUJSbfQkTlKZz7aj8GchFinWgu5i1CNfAmCrN19YqFfu3kj08z6X500yHxj09Za';
		console.log('=== onMount called ===');
		console.log('Stripe key:', key?.substring(0, 20) + '...');
		try {
			stripe = await loadStripe(key);
			console.log('Stripe loaded:', !!stripe);
		} catch (e) {
			console.error('Failed to load Stripe:', e);
		}
	});

	// Load subjects on mount
	async function loadSubjects() {
		try {
			subjects = await getSubjects();
			console.log('Subjects loaded:', subjects);
		} catch (e) {
			console.error('Failed to load subjects:', e);
		}
	}

	loadSubjects();

	// Initialize Stripe Elements when payment client secret is available
	$effect(async () => {
		console.log('Effect check:', { paymentClientSecret: !!paymentClientSecret, stripe: !!stripe, currentStep });
		if (paymentClientSecret && stripe && currentStep === 3) {
			console.log('Initializing Stripe Elements with client secret:', paymentClientSecret);

			const elements = stripe.elements({
				clientSecret: paymentClientSecret,
				appearance: {
					theme: 'stripe',
					variables: {
						colorPrimary: '#FF8C42',
						colorBackground: '#ffffff',
						colorText: '#1a1a1a',
						colorDanger: '#df1b41',
						fontFamily: 'system-ui, sans-serif',
						spacingUnit: '4px',
						borderRadius: '8px',
					}
				}
			});

			cardElement = elements.create('payment', {
				layout: 'tabs'
			});

			cardElement.mount('#stripe-card-element');
			console.log('Stripe Elements mounted');

			const submitButton = document.getElementById('stripe-submit-button');
			console.log('Submit button found:', !!submitButton);

			if (submitButton) {
				submitButton.addEventListener('click', async () => {
					console.log('Pay button clicked');
					submitButton.disabled = true;
					submitButton.textContent = 'Processing...';

					// Submit the elements first
					const { error: submitError } = await elements.submit();
					if (submitError) {
						submitButton.disabled = false;
						submitButton.textContent = `Pay LKR ${getPlanPrice(selectedPlan)}`;
						error = submitError.message || 'Payment failed';
						return;
					}

					// Then confirm payment
					const { error: stripeError, paymentIntent } = await stripe.confirmPayment({
						elements,
						clientSecret: paymentClientSecret,
						confirmParams: {
							return_url: `${window.location.origin}/teacher/dashboard`,
						},
					});

					console.log('Stripe confirmPayment result:', { stripeError, paymentIntent });

					if (stripeError) {
						submitButton.disabled = false;
						submitButton.textContent = `Pay LKR ${getPlanPrice(selectedPlan)}`;
						error = stripeError.message || 'Payment failed';
					}
				});
			}
		}
	});

	function goStep(n: number) {
		currentStep = n;
	}

	function selectPlan(plan: string) {
		selectedPlan = plan;
	}

	function selectSubject(subject: any) {
		subjectId = subject.id;
		subjectSearch = subject.name;
		subjectName = subject.name;
		showSubjectDropdown = false;
	}

	const filteredSubjects = $derived(
		subjectSearch
			? subjects.filter(s => s.name.toLowerCase().includes(subjectSearch.toLowerCase()))
			: subjects
	);

	$effect(() => {
		console.log('Dropdown state:', { showSubjectDropdown, filteredSubjects: filteredSubjects.length, subjects: subjects.length });
	});

	async function createListingAndProceed() {
		if (!authStore.user) {
			goto('/auth/login');
			return;
		}

		if (!subjectId) {
			error = 'Please select a subject';
			return;
		}

		isLoading = true;
		error = '';

		try {
			// Map form values to API
			const modeMap: Record<string, any> = {
				'Online': 'ONLINE',
				'In-person (student comes to me)': 'IN_PERSON',
				'Home visit (I go to student)': 'HOME_VISIT',
				'Both online & in-person': 'FLEXIBLE'
			};

			const classTypeMap: Record<string, any> = {
				'Individual (1-on-1)': 'INDIVIDUAL',
				'Small group (2–5)': 'GROUP',
				'Group class (6–20)': 'GROUP',
				'Large group (20+)': 'GROUP'
			};

			const payload = {
				subject_id: subjectId,
				mode: modeMap[teachingMode] || 'ONLINE',
				class_type: classTypeMap[classType] || 'INDIVIDUAL',
				hourly_rate: parseFloat(hourlyRate),
				description: classDescription,
				trial_available: freeTrial,
				trial_rate: freeTrial ? parseFloat(hourlyRate) * 0.5 : undefined,
				max_group_size: classType.includes('group') ? 20 : undefined
			};

			console.log('Creating listing with payload:', payload);

			const listing = await createListing(payload);

			console.log('Listing created successfully:', listing);

			createdListingId = listing.id;
			goStep(2);
		} catch (e: any) {
			error = e.message || 'Failed to create listing';
			console.error('Listing creation error:', e);
		} finally {
			isLoading = false;
		}
	}

	async function proceedToPayment() {
		if (!createdListingId) return;

		isLoading = true;
		error = '';

		try {
			console.log('Creating payment for listing:', createdListingId, 'plan:', selectedPlan);

			const payment = await createListingPayment({
				listing_id: createdListingId,
				plan: selectedPlan as any
			});

			console.log('Payment created successfully:', payment);

			paymentClientSecret = payment.client_secret;
			paymentIntentId = payment.payment_intent_id;
			console.log('Setting paymentClientSecret:', paymentClientSecret);
			console.log('Current step before goStep:', currentStep);
			goStep(3);
			console.log('Current step after goStep:', currentStep);
		} catch (e: any) {
			error = e.message || 'Failed to create payment';
			console.error('Payment creation error:', e);
		} finally {
			isLoading = false;
		}
	}

	function getPlanPrice(plan: string): string {
		switch (plan) {
			case 'BASIC': return '500';
			case 'STANDARD': return '1,200';
			case 'PREMIUM': return '2,000';
			default: return '1,200';
		}
	}
</script>

<svelte:head>
	<title>Post a Class — EduLink SL</title>
</svelte:head>

<div class="app-topbar">
	<div class="app-topbar-title">Post a Class</div>
	<div class="app-topbar-right">
		<div class="notif-btn"><i class="ti ti-bell"></i></div>
	</div>
</div>

{#if error}
	<div class="alert alert-error" style="margin: 16px 0">
		<i class="ti ti-alert-circle"></i>
		{error}
	</div>
{/if}

<div class="app-content">
	<div class="post-wrap">
		<div class="steps-bar" style="margin-bottom:24px">
			<div class="step-dot {currentStep >= 1 ? 'active' : ''} {currentStep > 1 ? 'done' : ''}">1</div>
			<div class="step-line {currentStep > 1 ? 'done' : ''}"></div>
			<div class="step-dot {currentStep >= 2 ? 'active' : ''} {currentStep > 2 ? 'done' : ''}">2</div>
			<div class="step-line {currentStep > 2 ? 'done' : ''}"></div>
			<div class="step-dot {currentStep >= 3 ? 'active' : ''} {currentStep > 3 ? 'done' : ''}">3</div>
			<span style="font-size:13px;color:var(--muted-fg);margin-left:8px">{stepLabels[currentStep]}</span>
		</div>

		<!-- Step 1: Class details -->
		{#if currentStep === 1}
			<div>
				<div class="section-card" style="margin-bottom:16px">
					<div style="font-size:15px;font-weight:700;margin-bottom:16px">Class details</div>
					<div class="form-group" style="position:relative">
						<label class="form-label">Subject</label>
						<input
							class="form-input"
							bind:value={subjectSearch}
							onfocus={() => showSubjectDropdown = true}
							oninput={() => showSubjectDropdown = true}
							placeholder="Type to search subjects..."
						/>
						{#if showSubjectDropdown && filteredSubjects.length > 0}
							<div class="dropdown-list">
								{#each filteredSubjects as subject}
									<div class="dropdown-item" onclick={() => selectSubject(subject)}>
										{subject.name}
									</div>
								{/each}
							</div>
						{/if}
						<!-- Click outside to close -->
						{#if showSubjectDropdown}
							<div
								style="position:fixed;top:0;left:0;right:0;bottom:0;z-index:99"
								onclick={() => showSubjectDropdown = false}
							></div>
						{/if}
					</div>
					<div class="form-grid-2">
						<div class="form-group">
							<label class="form-label">Level / Stream</label>
							<select class="form-input" bind:value={level}>
								<option value="AL_SCIENCE">A/L — Physical Science</option>
								<option value="AL_ARTS">A/L — Arts</option>
								<option value="AL_COMMERCE">A/L — Commerce</option>
								<option value="AL_TECHNOLOGY">A/L — Technology</option>
								<option value="OL">O/L (Grade 9–11)</option>
								<option value="UNIVERSITY">University</option>
								<option value="LANGUAGE">Language</option>
								<option value="OTHER">Other</option>
							</select>
						</div>
						<div class="form-group">
							<label class="form-label">Class type</label>
							<select class="form-input" bind:value={classType}>
								<option>Individual (1-on-1)</option>
								<option>Small group (2–5)</option>
								<option>Group class (6–20)</option>
								<option>Large group (20+)</option>
							</select>
						</div>
					</div>
					<div class="form-grid-2">
						<div class="form-group">
							<label class="form-label">Teaching mode</label>
							<select class="form-input" bind:value={teachingMode}>
								<option>Online</option>
								<option>In-person (student comes to me)</option>
								<option>Home visit (I go to student)</option>
								<option>Both online & in-person</option>
							</select>
						</div>
						<div class="form-group">
							<label class="form-label">Language of instruction</label>
							<select class="form-input" bind:value={language}>
								<option>English</option>
								<option>Sinhala</option>
								<option>Tamil</option>
								<option>English & Sinhala</option>
							</select>
						</div>
					</div>
					<div class="form-grid-2">
						<div class="form-group">
							<label class="form-label">Hourly rate (LKR)</label>
							<input class="form-input" type="number" bind:value={hourlyRate} placeholder="e.g. 3500" />
							<div class="form-hint">Platform takes 10% commission per completed session.</div>
						</div>
						<div class="form-group">
							<label class="form-label">Session duration</label>
							<select class="form-input" bind:value={sessionDuration}>
								<option>1 hour</option>
								<option>1.5 hours</option>
								<option>2 hours</option>
							</select>
						</div>
					</div>
					<div class="form-group">
						<label class="form-label">Class description</label>
						<textarea class="form-input" rows="4" bind:value={classDescription} placeholder="Describe what students will learn, your teaching approach, and what makes your class special..."></textarea>
					</div>
					<div class="form-group" style="margin-bottom:0">
						<label class="form-label">Offer a free trial class?</label>
						<div style="display:flex;gap:10px;margin-top:4px">
							<label style="display:flex;align-items:center;gap:6px;font-size:13px;cursor:pointer">
								<input type="radio" name="trial" value="yes" bind:group={freeTrial} style="accent-color:var(--saffron)" />Yes — 30 min free trial
							</label>
							<label style="display:flex;align-items:center;gap:6px;font-size:13px;cursor:pointer">
								<input type="radio" name="trial" value="no" bind:group={freeTrial} style="accent-color:var(--saffron)" />No trial
							</label>
						</div>
						<div class="form-hint">Offering a free trial significantly increases bookings for new listings.</div>
					</div>
				</div>

				<!-- Preview -->
				<div class="section-card" style="margin-bottom:16px">
					<div style="font-size:15px;font-weight:700;margin-bottom:14px">Preview — how students will see this listing</div>
					<div class="preview-card">
						<div class="preview-label">Listing preview</div>
						<div style="display:flex;gap:12px;align-items:flex-start">
							<div style="width:48px;height:48px;border-radius:var(--r-sm);background:#EEF2FF;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800;color:#3B4FD8">AP</div>
							<div style="flex:1">
								<div style="font-size:14px;font-weight:700;margin-bottom:2px">{authStore.user?.full_name || 'Teacher Name'} <span class="verified-tick"></span></div>
								<div style="font-size:12px;color:var(--muted-fg);margin-bottom:8px">{subjectName || 'Select a subject'} · {level}</div>
								<div style="display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px">
									<span class="badge badge-primary">{level}</span>
									<span class="badge badge-teal">{teachingMode}</span>
									<span class="badge badge-primary">{classType}</span>
									<span class="badge-merit">MERIT {authStore.user?.merit_score || 100}</span>
								</div>
								<div style="display:flex;align-items:center;justify-content:space-between">
									<div style="font-size:15px;font-weight:800">LKR {Number(hourlyRate).toLocaleString()}<span style="font-size:11px;font-weight:400;color:var(--muted-fg)">/hr</span></div>
									<span class="btn btn-outline btn-sm" style="border-radius:100px">View profile →</span>
								</div>
							</div>
						</div>
					</div>
				</div>

				<button class="btn btn-primary btn-lg" onclick={createListingAndProceed} disabled={isLoading}>
					{isLoading ? 'Creating listing...' : 'Continue to choose a plan →'}
				</button>
			</div>
		{/if}

		<!-- Step 2: Choose plan -->
		{#if currentStep === 2}
			<div>
				<div class="section-card" style="margin-bottom:16px">
					<div style="font-size:15px;font-weight:700;margin-bottom:6px">Choose a listing plan</div>
					<div style="font-size:13px;color:var(--muted-fg);margin-bottom:18px">Your listing will be shown to students searching for your subject in your district. Choose how long you want it active.</div>
					<div class="plan-grid">
						<div class="plan-card {selectedPlan === 'BASIC' ? 'sel' : ''}" onclick={() => selectPlan('BASIC')}>
							<div class="plan-name">Basic</div>
							<div class="plan-price">LKR 500</div>
							<div class="plan-period">per month</div>
							<ul class="plan-features">
								<li><i class="ti ti-check"></i>Listed for 30 days</li>
								<li><i class="ti ti-check"></i>Up to 10 bookings/month</li>
								<li><i class="ti ti-check"></i>Standard search ranking</li>
							</ul>
						</div>
						<div class="plan-card popular {selectedPlan === 'STANDARD' ? 'sel' : ''}" onclick={() => selectPlan('STANDARD')}>
							<div class="plan-popular-tag">Most popular</div>
							<div class="plan-name">Standard</div>
							<div class="plan-price">LKR 1,200</div>
							<div class="plan-period">per 3 months</div>
							<ul class="plan-features">
								<li><i class="ti ti-check"></i>Listed for 90 days</li>
								<li><i class="ti ti-check"></i>Unlimited bookings</li>
								<li><i class="ti ti-check"></i>Boosted search ranking</li>
								<li><i class="ti ti-check"></i>Save LKR 300 vs monthly</li>
							</ul>
						</div>
						<div class="plan-card {selectedPlan === 'PREMIUM' ? 'sel' : ''}" onclick={() => selectPlan('PREMIUM')}>
							<div class="plan-name">Premium</div>
							<div class="plan-price">LKR 2,000</div>
							<div class="plan-period">per 6 months</div>
							<ul class="plan-features">
								<li><i class="ti ti-check"></i>Listed for 180 days</li>
								<li><i class="ti ti-check"></i>Unlimited bookings</li>
								<li><i class="ti ti-check"></i>Priority search placement</li>
								<li><i class="ti ti-check"></i>Featured tutor badge</li>
								<li><i class="ti ti-check"></i>Best value</li>
							</ul>
						</div>
					</div>
				</div>
				<div style="display:flex;gap:10px">
					<button class="btn btn-ghost" onclick={() => goStep(1)}>← Back</button>
					<button class="btn btn-primary btn-lg" onclick={proceedToPayment} disabled={isLoading}>
						{isLoading ? 'Creating payment...' : 'Proceed to payment →'}
					</button>
				</div>
			</div>
		{/if}

		<!-- Step 3: Payment -->
		{#if currentStep === 3}
			<div>
				<div class="section-card" style="margin-bottom:16px">
					<div style="font-size:15px;font-weight:700;margin-bottom:6px">Complete payment</div>
					<div style="font-size:13px;color:var(--muted-fg);margin-bottom:18px">Pay LKR {getPlanPrice(selectedPlan)} to activate your listing for the selected plan.</div>
					
					{#if paymentClientSecret}
						<div id="stripe-card-element" style="margin-bottom:16px"></div>
						<button id="stripe-submit-button" class="btn btn-primary btn-lg" style="width:100%">
							Pay LKR {getPlanPrice(selectedPlan)}
						</button>
						<div class="form-hint" style="text-align:center;margin-top:12px">
							<i class="ti ti-lock"></i> Secure payment powered by Stripe
						</div>
					{:else}
						<div style="text-align:center;padding:20px">
							<div class="loading-spinner"></div>
						</div>
					{/if}
				</div>
				<div style="display:flex;gap:10px">
					<button class="btn btn-ghost" onclick={() => goStep(2)}>← Back</button>
				</div>
			</div>
		{/if}
	</div>
</div>

<style>
	.post-wrap {
		max-width: 680px;
	}
	.plan-grid {
		display: grid;
		grid-template-columns: repeat(3,1fr);
		gap: 12px;
		margin-bottom: 0;
	}
	.plan-card {
		border: 2px solid var(--border-dk);
		border-radius: var(--r-lg);
		padding: 18px;
		cursor: pointer;
		transition: all .2s;
		background: #fff;
	}
	.plan-card:hover {
		border-color: var(--saffron);
	}
	.plan-card.sel {
		border-color: var(--saffron);
		background: var(--saffron-lt);
	}
	.plan-card.popular {
		border-color: var(--saffron);
	}
	.plan-popular-tag {
		background: var(--saffron);
		color: #fff;
		font-size: 9px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: .5px;
		padding: 2px 8px;
		border-radius: 100px;
		margin-bottom: 10px;
		display: inline-block;
	}
	.plan-name {
		font-size: 14px;
		font-weight: 800;
		margin-bottom: 4px;
	}
	.plan-price {
		font-size: 20px;
		font-weight: 800;
		color: var(--saffron);
		margin-bottom: 2px;
	}
	.plan-period {
		font-size: 11px;
		color: var(--muted-fg);
		margin-bottom: 10px;
	}
	.plan-features {
		font-size: 12px;
		color: var(--muted-fg);
		display: flex;
		flex-direction: column;
		gap: 4px;
	}
	.plan-features li {
		display: flex;
		align-items: center;
		gap: 5px;
	}
	.plan-features li i {
		font-size: 12px;
		color: var(--green);
	}
	.preview-card {
		background: var(--bg);
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-lg);
		padding: 18px;
	}
	.preview-label {
		font-size: 10px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: .6px;
		color: var(--muted-fg);
		margin-bottom: 12px;
	}
	.dropdown-list {
		position: absolute;
		top: 100%;
		left: 0;
		right: 0;
		background: #fff;
		border: 1px solid var(--border-dk);
		border-radius: var(--r-md);
		max-height: 200px;
		overflow-y: auto;
		z-index: 100;
		box-shadow: 0 4px 12px rgba(0,0,0,0.1);
		margin-top: 4px;
	}
	.dropdown-item {
		padding: 10px 12px;
		cursor: pointer;
		font-size: 13px;
		border-bottom: 1px solid var(--border-lt);
	}
	.dropdown-item:hover {
		background: var(--bg);
	}
	.dropdown-item:last-child {
		border-bottom: none;
	}
</style>
