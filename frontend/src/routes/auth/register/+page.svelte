<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { getAuthStore } from '$lib/stores/auth.svelte.ts';
	import { register } from '$lib/api/auth';

	let currentStep = $state(1);
	let selectedRole = $state('student');
	let isLoading = $state(false);
	let error = $state('');

	// Form fields
	let firstName = $state('');
	let lastName = $state('');
	let email = $state('');
	let phone = $state('');
	let district = $state('');
	let password = $state('');
	let confirmPassword = $state('');

	// Validation errors
	let emailError = $state('');
	let phoneError = $state('');
	let passwordError = $state('');
	let confirmPasswordError = $state('');

	// Pre-select role from URL if provided
	if ($page.url.searchParams.get('role') === 'teacher') {
		selectedRole = 'teacher';
	}

	const authStore = getAuthStore();

	function pickRole(role: string) {
		selectedRole = role;
	}

	function goStep(n: number) {
		currentStep = n;
		error = '';
		// Clear validation errors when moving between steps
		if (n !== 2) {
			emailError = '';
			phoneError = '';
			passwordError = '';
			confirmPasswordError = '';
		}
	}

	// Validation functions
	function validateEmail(email: string): boolean {
		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		return emailRegex.test(email);
	}

	function validatePhone(phone: string): boolean {
		// Sri Lankan phone number validation (starts with 0 or +94, 9-10 digits)
		const phoneRegex = /^(0\d{9}|\+94\d{9})$/;
		return phoneRegex.test(phone.replace(/\s/g, ''));
	}

	function validatePassword(password: string): { valid: boolean; message: string } {
		if (password.length < 8) {
			return { valid: false, message: 'Password must be at least 8 characters long.' };
		}
		return { valid: true, message: '' };
	}

	async function handleRegistration() {
		try {
			isLoading = true;
			error = '';
			emailError = '';
			phoneError = '';
			passwordError = '';
			confirmPasswordError = '';

			// Validation
			if (!firstName || !lastName || !email || !password) {
				error = 'Please fill in all required fields.';
				return;
			}

			// Email validation
			if (!validateEmail(email)) {
				emailError = 'Please enter a valid email address (e.g., user@example.com).';
				return;
			}

			// Phone validation (if provided)
			if (phone && !validatePhone(phone)) {
				phoneError = 'Please enter a valid Sri Lankan phone number (e.g., 0771234567 or +94771234567).';
				return;
			}

			// Password validation
			const passwordValidation = validatePassword(password);
			if (!passwordValidation.valid) {
				passwordError = passwordValidation.message;
				return;
			}

			// Confirm password validation
			if (password !== confirmPassword) {
				confirmPasswordError = 'Passwords do not match.';
				return;
			}

			// Map role to backend format
			const roleMap = {
				'student': 'STUDENT',
				'teacher': 'TEACHER'
			};

			const userData = {
				email,
				password,
				full_name: `${firstName} ${lastName}`,
				role: roleMap[selectedRole] as 'STUDENT' | 'TEACHER',
				city: district || undefined,
				phone: phone || undefined
			};

			await register(userData);

			// Auto-login after registration
			await authStore.login(email, password);

			// Redirect to appropriate dashboard
			if (selectedRole === 'teacher') goto('/teacher/verification');
			else goto('/student/dashboard');

		} catch (err: any) {
			// Convert technical errors to user-friendly messages
			if (err?.response?.status === 400 && err?.response?.data?.detail === 'REGISTER_USER_ALREADY_EXISTS') {
				error = 'An account with this email already exists. Please sign in instead.';
			} else if (err?.response?.status === 400) {
				error = 'Please check your information and try again.';
			} else if (err?.message && !err?.response) {
				error = err.message;
			} else {
				error = 'Registration failed. Please try again later.';
			}
		} finally {
			isLoading = false;
		}
	}

	function finishRegistration() {
		// This is now handled by handleRegistration
		// Keep this for the final step redirect
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

			{#if error}
				<div class="error-message">{error}</div>
			{/if}

			<div class="form-grid-2">
				<div class="form-group">
					<label class="form-label" for="firstName">First name</label>
					<input 
						class="form-input" 
						id="firstName" 
						placeholder="Kasun" 
						bind:value={firstName}
						disabled={isLoading}
					/>
				</div>
				<div class="form-group">
					<label class="form-label" for="lastName">Last name</label>
					<input 
						class="form-input" 
						id="lastName" 
						placeholder="Jayasuriya" 
						bind:value={lastName}
						disabled={isLoading}
					/>
				</div>
			</div>
			<div class="form-group">
				<label class="form-label" for="email">Email address</label>
				<input 
					class="form-input {emailError ? 'input-error' : ''}" 
					id="email" 
					type="email" 
					placeholder="you@email.com" 
					bind:value={email}
					disabled={isLoading}
				/>
				{#if emailError}
					<div class="field-error">{emailError}</div>
				{/if}
			</div>
			<div class="form-group">
				<label class="form-label" for="phone">Phone number (optional)</label>
				<input 
					class="form-input {phoneError ? 'input-error' : ''}" 
					id="phone" 
					type="tel" 
					placeholder="+94 77 123 4567" 
					bind:value={phone}
					disabled={isLoading}
				/>
				{#if phoneError}
					<div class="field-error">{phoneError}</div>
				{/if}
			</div>
			<div class="form-group">
				<label class="form-label" for="district">District</label>
				<select 
					class="form-input" 
					id="district" 
					bind:value={district}
					disabled={isLoading}
				>
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
					<option>Ampara</option>
					<option>Batticaloa</option>
					<option>Jaffna</option>
					<option>Kilinochchi</option>
					<option>Mannar</option>
					<option>Mullaitivu</option>
					<option>Polonnaruwa</option>
					<option>Puttalam</option>
					<option>Trincomalee</option>
					<option>Vavuniya</option>
				</select>
			</div>
			<div class="form-group">
				<label class="form-label" for="password">Password</label>
				<input 
					class="form-input {passwordError ? 'input-error' : ''}" 
					id="password" 
					type="password" 
					placeholder="Minimum 8 characters" 
					bind:value={password}
					disabled={isLoading}
				/>
				{#if passwordError}
					<div class="field-error">{passwordError}</div>
				{/if}
			</div>
			<div class="form-group" style="margin-bottom: 20px">
				<label class="form-label" for="confirmPassword">Confirm password</label>
				<input 
					class="form-input {confirmPasswordError ? 'input-error' : ''}" 
					id="confirmPassword" 
					type="password" 
					placeholder="Repeat password" 
					bind:value={confirmPassword}
					disabled={isLoading}
				/>
				{#if confirmPasswordError}
					<div class="field-error">{confirmPasswordError}</div>
				{/if}
			</div>
			<div style="display: flex; gap: 10px">
				<button class="btn btn-ghost" onclick={() => goStep(1)} disabled={isLoading}>← Back</button>
				<button class="btn btn-primary" style="flex: 1" onclick={handleRegistration} disabled={isLoading}>
					{isLoading ? 'Creating account...' : 'Create Account →'}
				</button>
			</div>
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
	.error-message {
		background: #fee2e2;
		border: 1px solid #fecaca;
		color: #dc2626;
		padding: 10px 14px;
		border-radius: var(--radius-sm);
		font-size: 13px;
		margin-bottom: 16px;
	}
	.field-error {
		color: #dc2626;
		font-size: 12px;
		margin-top: 4px;
	}
	.input-error {
		border-color: #dc2626 !important;
		background: #fef2f2;
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
