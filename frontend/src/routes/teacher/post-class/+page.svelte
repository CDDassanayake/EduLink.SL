<script lang="ts">
	let currentStep = $state(1);
	let selectedPlan = $state('Standard');
	let subject = $state('A/L Physics');
	let level = $state('A/L — Physical Science');
	let classType = $state('Individual (1-on-1)');
	let teachingMode = $state('Online');
	let language = $state('English');
	let hourlyRate = $state('3500');
	let sessionDuration = $state('1.5 hours');
	let classDescription = $state('Comprehensive A/L Physics covering all theory topics with extensive past paper practice. I focus on building conceptual clarity before moving to problem-solving. Special emphasis on the National Exam question patterns for the past 10 years.');
	let freeTrial = $state('no');

	const stepLabels = ['', 'Class details', 'Choose a plan', 'Payment'];

	function goStep(n: number) {
		currentStep = n;
	}

	function selectPlan(plan: string) {
		selectedPlan = plan;
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
					<div class="form-group">
						<label class="form-label">Subject</label>
						<select class="form-input" bind:value={subject}>
							<option>Select a subject</option>
							<option>A/L Physics</option>
							<option>Combined Mathematics</option>
							<option>O/L Mathematics</option>
							<option>O/L Science</option>
							<option>Chemistry</option>
							<option>Biology</option>
							<option>English Language</option>
							<option>Accounting</option>
							<option>Economics</option>
							<option>ICT</option>
						</select>
					</div>
					<div class="form-grid-2">
						<div class="form-group">
							<label class="form-label">Level / Stream</label>
							<select class="form-input" bind:value={level}>
								<option>A/L — Physical Science</option>
								<option>A/L — Biological Science</option>
								<option>A/L — Commerce</option>
								<option>A/L — Arts</option>
								<option>O/L (Grade 9–11)</option>
								<option>University</option>
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
								<div style="font-size:14px;font-weight:700;margin-bottom:2px">Aruna Perera <span class="verified-tick"></span></div>
								<div style="font-size:12px;color:var(--muted-fg);margin-bottom:8px">{subject} · {level}</div>
								<div style="display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px">
									<span class="badge badge-primary">A/L Science</span>
									<span class="badge badge-teal">Online</span>
									<span class="badge badge-primary">Individual</span>
									<span class="badge-merit">MERIT 98</span>
								</div>
								<div style="display:flex;align-items:center;justify-content:space-between">
									<div style="font-size:15px;font-weight:800">LKR {Number(hourlyRate).toLocaleString()}<span style="font-size:11px;font-weight:400;color:var(--muted-fg)">/hr</span></div>
									<span class="btn btn-outline btn-sm" style="border-radius:100px">View profile →</span>
								</div>
							</div>
						</div>
					</div>
				</div>

				<button class="btn btn-primary btn-lg" onclick={() => goStep(2)}>Continue to choose a plan →</button>
			</div>
		{/if}

		<!-- Step 2: Choose plan -->
		{#if currentStep === 2}
			<div>
				<div class="section-card" style="margin-bottom:16px">
					<div style="font-size:15px;font-weight:700;margin-bottom:6px">Choose a listing plan</div>
					<div style="font-size:13px;color:var(--muted-fg);margin-bottom:18px">Your listing will be shown to students searching for your subject in your district. Choose how long you want it active.</div>
					<div class="plan-grid">
						<div class="plan-card {selectedPlan === 'Basic' ? 'sel' : ''}" onclick={() => selectPlan('Basic')}>
							<div class="plan-name">Basic</div>
							<div class="plan-price">LKR 500</div>
							<div class="plan-period">per month</div>
							<ul class="plan-features">
								<li><i class="ti ti-check"></i>Listed for 30 days</li>
								<li><i class="ti ti-check"></i>Up to 10 bookings/month</li>
								<li><i class="ti ti-check"></i>Standard search ranking</li>
							</ul>
						</div>
						<div class="plan-card popular {selectedPlan === 'Standard' ? 'sel' : ''}" onclick={() => selectPlan('Standard')}>
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
						<div class="plan-card {selectedPlan === 'Premium' ? 'sel' : ''}" onclick={() => selectPlan('Premium')}>
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
					<button class="btn btn-primary btn-lg" onclick={() => goStep(3)}>Proceed to payment →</button>
				</div>
			</div>
		{/if}

		<!-- Step 3: Success (goes to payment page) -->
		{#if currentStep === 3}
			<div style="text-align:center;padding:20px 0">
				<div style="width:64px;height:64px;background:var(--saffron-lt);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:28px;color:var(--saffron)"><i class="ti ti-credit-card"></i></div>
				<div style="font-size:20px;font-weight:800;margin-bottom:6px">Almost there!</div>
				<div style="font-size:14px;color:var(--muted-fg);margin-bottom:24px">Complete payment to activate your listing and start receiving student bookings.</div>
				<a href="/teacher/post-payment" class="btn btn-saffron btn-lg"><i class="ti ti-lock"></i> Complete payment — LKR 1,200</a>
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
</style>
