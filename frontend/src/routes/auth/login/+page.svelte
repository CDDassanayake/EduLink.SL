<script lang="ts">
	import { goto } from '$app/navigation';

	let selectedRole = $state('student');

	function selectRole(role: string) {
		selectedRole = role;
	}

	function handleLogin() {
		const params = new URLSearchParams(window.location.search);
		const redirect = params.get('redirect');
		if (redirect) {
			goto(`/${redirect}`);
			return;
		}
		// Redirect to appropriate dashboard based on selected role
		if (selectedRole === 'student') goto('/student/dashboard');
		else if (selectedRole === 'teacher') goto('/teacher/dashboard');
		else goto('/admin/dashboard');
	}
</script>

<svelte:head>
	<title>Log In — EduLink SL</title>
</svelte:head>

<header class="pub-nav">
	<div class="container">
		<a href="/" class="nav-logo">EDULINK.SL</a>
		<div class="nav-right">
			<a href="/auth/register" class="btn btn-ghost btn-sm">Create account</a>
		</div>
	</div>
</header>

<div class="auth-wrap">
	<div class="auth-card">
		<div class="auth-logo">EDULINK.SL</div>
		<h1 class="auth-title">Welcome back</h1>
		<p class="auth-sub">Sign in to continue to your account</p>

		<button class="social-btn">
			<svg width="18" height="18" viewBox="0 0 24 24">
				<path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
				<path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
				<path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
				<path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
			</svg>
			Continue with Google
		</button>

		<div class="divider-text">or sign in with email</div>

		<!-- Demo: role selector -->
		<div class="role-demo">
			<div class="role-demo-lbl">Demo: Log in as</div>
			<div class="role-grid">
				<button
					type="button"
					class="role-opt {selectedRole === 'student' ? 'sel' : ''}"
					onclick={() => selectRole('student')}
				>
					<i class="ti ti-school"></i>Student
				</button>
				<button
					type="button"
					class="role-opt {selectedRole === 'teacher' ? 'sel' : ''}"
					onclick={() => selectRole('teacher')}
				>
					<i class="ti ti-certificate"></i>Teacher
				</button>
				<button
					type="button"
					class="role-opt {selectedRole === 'admin' ? 'sel' : ''}"
					onclick={() => selectRole('admin')}
				>
					<i class="ti ti-shield"></i>Admin
				</button>
			</div>
		</div>

		<div class="form-group">
			<label class="form-label" for="email">Email address</label>
			<input class="form-input" id="email" type="email" placeholder="kasun@email.com" value="kasun@example.com" />
		</div>
		<div class="form-group" style="margin-bottom: 6px">
			<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px">
				<label class="form-label" for="password" style="margin-bottom: 0">Password</label>
				<a href="/auth/forgot-password" style="font-size: 12px; color: var(--color-saffron); font-weight: 600">Forgot password?</a>
			</div>
			<input class="form-input" id="password" type="password" value="••••••••••" />
		</div>
		<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 20px">
			<input type="checkbox" id="remember" checked style="accent-color: var(--color-saffron); cursor: pointer" />
			<label for="remember" style="font-size: 13px; color: var(--color-muted-fg)">Remember me for 30 days</label>
		</div>
		<button class="btn btn-primary btn-full" onclick={handleLogin}>Sign In →</button>
		<div class="auth-footer">Don't have an account? <a href="/auth/register">Sign up free</a></div>
	</div>
</div>

<style>
	:global(body) {
		background: radial-gradient(ellipse at 60% 30%, #FEF3E0 0%, #FAF9F4 55%);
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
		max-width: 400px;
		box-shadow: var(--shadow-lg);
	}
	.auth-logo {
		font-size: 17px;
		font-weight: 800;
		color: var(--color-primary);
		text-align: center;
		margin-bottom: 28px;
		letter-spacing: -0.3px;
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
	.social-btn {
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 10px;
		padding: 11px 16px;
		border-radius: var(--radius-sm);
		border: 1.5px solid var(--color-border-dark);
		background: #fff;
		font-size: 14px;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.15s;
		font-family: var(--font-sans);
		margin-bottom: 10px;
	}
	.social-btn:hover {
		background: var(--color-muted);
	}
	.role-demo {
		background: var(--color-muted);
		border-radius: var(--radius);
		padding: 14px;
		margin-bottom: 20px;
	}
	.role-demo-lbl {
		font-size: 10px;
		font-family: var(--font-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.6px;
		color: var(--color-muted-fg);
		margin-bottom: 8px;
	}
	.role-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 6px;
	}
	.role-opt {
		background: #fff;
		border: 1.5px solid var(--color-border-dark);
		border-radius: var(--radius-sm);
		padding: 8px 6px;
		text-align: center;
		cursor: pointer;
		transition: all 0.15s;
		font-size: 11px;
		font-weight: 600;
		color: var(--color-muted-fg);
		width: 100%;
	}
	.role-opt:hover {
		border-color: var(--color-saffron);
		color: var(--color-saffron);
	}
	.role-opt.sel {
		border-color: var(--color-saffron);
		background: var(--color-saffron-light);
		color: var(--color-saffron-hover);
	}
	.role-opt i {
		display: block;
		font-size: 18px;
		margin-bottom: 3px;
	}
	.auth-footer {
		text-align: center;
		margin-top: 20px;
		font-size: 13px;
		color: var(--color-muted-fg);
	}
	.auth-footer a {
		color: var(--color-saffron);
		font-weight: 600;
		cursor: pointer;
	}
</style>
