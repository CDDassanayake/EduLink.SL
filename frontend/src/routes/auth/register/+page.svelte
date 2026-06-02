<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	let currentStep = $state(1);
	let selectedRole = $state('student');

	// Pre-select role from URL if provided
	if ($page.url.searchParams.get('role') === 'teacher') {
		selectedRole = 'teacher';
	}

	function pickRole(role: string) {
		selectedRole = role;
	}

	function goStep(n: number) {
		currentStep = n;
	}

	function finishRegistration() {
		// Redirect to appropriate dashboard based on selected role
		if (selectedRole === 'teacher') goto('/teacher/verification');
		else goto('/student/dashboard');
	}
</script>

<svelte:head>
	<title>Create Account — EduLink SL</title>
</svelte:head>

<header class="pub-nav">
	<div class="container">
		<a href="/" class="nav-logo">EDULINK.SL</a>
		<div class="nav-right">
			<a href="/auth/login" class="btn btn-ghost btn-sm">Already have an account?</a>
		</div>
	</div>
</header>

<div class="auth-wrap">
	<div class="auth-card">
		<div class="auth-logo">EDULINK.SL</div>

		<!-- Step indicator -->
		<div class="steps-bar" style="justify-content: center; margin-bottom: 24px">
			<div class="step-dot {currentStep >= 1 ? 'active' : ''} {currentStep > 1 ? 'done' : ''}">1</div>
			<div class="step-line {currentStep > 1 ? 'done' : ''}"></div>
			<div class="step-dot {currentStep >= 2 ? 'active' : ''} {currentStep > 2 ? 'done' : ''}">2</div>
			<div class="step-line {currentStep > 2 ? 'done' : ''}"></div>
			<div class="step-dot {currentStep >= 3 ? 'active' : ''} {currentStep > 3 ? 'done' : ''}">3</div>
		</div>

		<!-- Step 1: Role selection -->
		{#if currentStep === 1}
			<h1 class="auth-title">Create your account</h1>
			<p class="auth-sub">I am joining EduLink SL as a…</p>
			<div class="role-choice-grid">
				<button
					type="button"
					class="role-choice {selectedRole === 'student' ? 'sel' : ''}"
					onclick={() => pickRole('student')}
				>
					<div class="rc-icon" style="background: var(--color-teal-light)">
						<i class="ti ti-school" style="font-size: 22px; color: var(--color-teal)"></i>
					</div>
					<div class="rc-title">Student</div>
					<div class="rc-desc">Find tutors for O/L, A/L, or university. Book sessions online or in-person.</div>
				</button>
				<button
					type="button"
					class="role-choice {selectedRole === 'teacher' ? 'sel' : ''}"
					onclick={() => pickRole('teacher')}
				>
					<div class="rc-icon" style="background: var(--color-saffron-light)">
						<i class="ti ti-certificate" style="font-size: 22px; color: var(--color-saffron)"></i>
					</div>
					<div class="rc-title">Tutor</div>
					<div class="rc-desc">List your subjects, set your schedule, and earn by teaching students.</div>
				</button>
			</div>
			<button class="btn btn-primary btn-full" onclick={() => goStep(2)}>Continue →</button>
		{/if}

		<!-- Step 2: Account details -->
		{#if currentStep === 2}
			<h1 class="auth-title">Your details</h1>
			<p class="auth-sub">
				{selectedRole === 'teacher' ? 'Set up your tutor account' : 'Set up your student account'}
			</p>
			<div class="form-grid-2">
				<div class="form-group">
					<label class="form-label" for="firstName">First name</label>
					<input class="form-input" id="firstName" placeholder="Kasun" />
				</div>
				<div class="form-group">
					<label class="form-label" for="lastName">Last name</label>
					<input class="form-input" id="lastName" placeholder="Jayasuriya" />
				</div>
			</div>
			<div class="form-group">
				<label class="form-label" for="email">Email address</label>
				<input class="form-input" id="email" type="email" placeholder="you@email.com" />
			</div>
			<div class="form-group">
				<label class="form-label" for="phone">Phone number</label>
				<input class="form-input" id="phone" type="tel" placeholder="+94 77 123 4567" />
			</div>
			<div class="form-group">
				<label class="form-label" for="district">District</label>
				<select class="form-input" id="district">
					<option value="">Select your district</option>
					<option>Colombo</option>
					<option>Kandy</option>
					<option>Gampaha</option>
					<option>Negombo</option>
					<option>Matara</option>
					<option>Galle</option>
					<option>Kurunegala</option>
					<option>Anuradhapura</option>
					<option>Badulla</option>
					<option>Ratnapura</option>
				</select>
			</div>
			<div class="form-group">
				<label class="form-label" for="password">Password</label>
				<input class="form-input" id="password" type="password" placeholder="Minimum 8 characters" />
			</div>
			<div class="form-group" style="margin-bottom: 20px">
				<label class="form-label" for="confirmPassword">Confirm password</label>
				<input class="form-input" id="confirmPassword" type="password" placeholder="Repeat password" />
			</div>
			<div style="display: flex; gap: 10px">
				<button class="btn btn-ghost" onclick={() => goStep(1)}>← Back</button>
				<button class="btn btn-primary" style="flex: 1" onclick={() => goStep(3)}>Continue →</button>
			</div>
		{/if}

		<!-- Step 3: Confirm / Redirect -->
		{#if currentStep === 3}
			<div style="text-align: center; padding: 16px 0 24px">
				<div
					style="width: 64px; height: 64px; background: var(--color-green-light); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; font-size: 28px; color: var(--color-green)"
				>
					<i class="ti ti-check"></i>
				</div>
				<h1 class="auth-title">Account created!</h1>
				<p class="auth-sub">
					{selectedRole === 'teacher'
						? 'Next step: upload your verification documents to start listing classes.'
						: "You're all set. Continue to your student dashboard."}
				</p>
			</div>
			<button class="btn btn-primary btn-full" onclick={finishRegistration}>Go to my dashboard →</button>
		{/if}

		{#if currentStep < 3}
			<div class="auth-footer">Already have an account? <a href="/auth/login">Sign in</a></div>
		{/if}
	</div>
</div>

<style>
	:global(body) {
		background: radial-gradient(ellipse at 40% 60%, #FEF3E0 0%, #FAF9F4 55%);
		min-height: 100vh;
	}
	.auth-wrap {
		min-height: calc(100vh - 60px);
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 32px 24px;
	}
	.auth-card {
		background: #fff;
		border-radius: var(--radius-xl);
		border: 1px solid var(--color-border-dark);
		padding: 40px 36px;
		width: 100%;
		max-width: 460px;
		box-shadow: var(--shadow-lg);
	}
	.auth-logo {
		font-size: 17px;
		font-weight: 800;
		color: var(--color-primary);
		text-align: center;
		margin-bottom: 24px;
	}
	.auth-title {
		font-size: 22px;
		font-weight: 800;
		text-align: center;
		margin-bottom: 4px;
	}
	.auth-sub {
		font-size: 14px;
		color: var(--color-muted-fg);
		text-align: center;
		margin-bottom: 28px;
	}
	/* Step indicator styles */
	.steps-bar {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 28px;
	}
	.step-dot {
		width: 28px;
		height: 28px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 12px;
		font-weight: 700;
		border: 2px solid var(--color-border-dark);
		color: var(--color-muted-fg);
		flex-shrink: 0;
		font-family: var(--font-mono);
		transition: all 0.2s;
	}
	.step-dot.done {
		background: var(--color-green);
		border-color: var(--color-green);
		color: #fff;
	}
	.step-dot.active {
		background: var(--color-saffron);
		border-color: var(--color-saffron);
		color: #fff;
	}
	.step-line {
		flex: 1;
		height: 2px;
		background: var(--color-border-dark);
		max-width: 48px;
	}
	.step-line.done {
		background: var(--color-green);
	}
	.role-choice-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 14px;
		margin-bottom: 20px;
	}
	.role-choice {
		border: 2px solid var(--color-border-dark);
		border-radius: var(--radius-lg);
		padding: 22px 18px;
		cursor: pointer;
		transition: all 0.2s;
		background: #fff;
		text-align: left;
		font-family: var(--font-sans);
		font-size: inherit;
		width: 100%;
		display: block;
	}
	.role-choice:hover {
		border-color: var(--color-saffron);
		background: var(--color-saffron-light);
	}
	.role-choice.sel {
		border-color: var(--color-saffron);
		background: var(--color-saffron-light);
	}
	.rc-icon {
		width: 44px;
		height: 44px;
		border-radius: var(--radius);
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 12px;
	}
	.rc-title {
		font-size: 15px;
		font-weight: 700;
		margin-bottom: 4px;
	}
	.rc-desc {
		font-size: 12px;
		color: var(--color-muted-fg);
		line-height: 1.5;
	}
	.auth-footer {
		text-align: center;
		margin-top: 18px;
		font-size: 13px;
		color: var(--color-muted-fg);
	}
	.auth-footer a {
		color: var(--color-saffron);
		font-weight: 600;
		cursor: pointer;
	}
</style>
