<script lang="ts">
	import { page } from '$app/stores';

	let { children } = $props();

	function isActive(path: string) {
		return $page.url.pathname === path || $page.url.pathname.startsWith(path + '/');
	}
</script>

<div class="app-wrap">
	<nav class="sidebar">
		<div class="sb-logo">
			<div class="sb-logo-txt">EDULINK.SL</div>
			<div class="sb-logo-role">Teacher Portal</div>
		</div>
		<div class="sb-section">Manage</div>
		<a href="/teacher/dashboard" class="sb-link {isActive('/teacher/dashboard') ? 'active' : ''}">
			<i class="ti ti-layout-dashboard"></i>Dashboard
		</a>
		<a href="/teacher/post-class" class="sb-link {isActive('/teacher/post-class') ? 'active' : ''}">
			<i class="ti ti-plus"></i>Post a Class
		</a>
		<a href="/teacher/schedule" class="sb-link {isActive('/teacher/schedule') ? 'active' : ''}">
			<i class="ti ti-calendar"></i>Schedule
		</a>
		<a href="/teacher/messages" class="sb-link {isActive('/teacher/messages') ? 'active' : ''}">
			<i class="ti ti-message-circle"></i>Messages
			<span style="background: var(--saffron); color: #fff; font-size: 9px; font-weight: 800; padding: 1px 6px; border-radius: 100px; margin-left: auto">3</span>
		</a>
		<a href="/teacher/earnings" class="sb-link {isActive('/teacher/earnings') ? 'active' : ''}">
			<i class="ti ti-wallet"></i>Earnings
		</a>
		<div class="sb-spacer"></div>
		<div class="sb-section">Account</div>
		<a href="/teacher/verification" class="sb-link {isActive('/teacher/verification') ? 'active' : ''}">
			<i class="ti ti-shield-check"></i>Verification
			<span class="badge badge-green" style="font-size: 9px; margin-left: auto">Verified</span>
		</a>
		<a href="/auth/login" class="sb-link">
			<i class="ti ti-logout"></i>Log out
		</a>
		<div class="sb-user">
			<div class="sb-avatar" style="background: var(--saffron-lt); color: var(--saffron-hv)">AP</div>
			<div class="sb-user-info">
				<div class="sb-user-name">Aruna Perera</div>
				<div class="sb-user-sub">Merit: 98/100</div>
			</div>
		</div>
	</nav>

	<div class="app-main">
		{@render children()}
	</div>
</div>

<style>
	.app-wrap {
		display: flex;
		min-height: 100vh;
		background: var(--bg);
	}
	.sidebar {
		width: 240px;
		background: #fff;
		border-right: 1px solid var(--border-dk);
		display: flex;
		flex-direction: column;
		padding: 20px 16px;
		flex-shrink: 0;
	}
	.sb-logo {
		margin-bottom: 24px;
	}
	.sb-logo-txt {
		font-size: 16px;
		font-weight: 800;
		color: var(--primary);
		letter-spacing: -0.3px;
	}
	.sb-logo-role {
		font-size: 11px;
		color: var(--muted-fg);
		margin-top: 2px;
	}
	.sb-section {
		font-size: 10px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.8px;
		color: var(--muted-fg);
		margin: 16px 0 8px;
	}
	.sb-link {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 10px 12px;
		border-radius: var(--r-sm);
		font-size: 13px;
		font-weight: 600;
		color: var(--muted-fg);
		text-decoration: none;
		transition: all 0.15s;
		margin-bottom: 2px;
	}
	.sb-link:hover {
		background: var(--muted);
		color: var(--fg);
	}
	.sb-link.active {
		background: var(--saffron-lt);
		color: var(--saffron-hv);
	}
	.sb-link i {
		font-size: 18px;
	}
	.sb-spacer {
		flex: 1;
	}
	.sb-user {
		display: flex;
		align-items: center;
		gap: 10px;
		padding-top: 16px;
		border-top: 1px solid var(--border-dk);
		margin-top: 8px;
	}
	.sb-avatar {
		width: 36px;
		height: 36px;
		border-radius: 50%;
		background: var(--primary);
		color: #fff;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 13px;
		font-weight: 800;
		flex-shrink: 0;
	}
	.sb-user-info {
		flex: 1;
		min-width: 0;
	}
	.sb-user-name {
		font-size: 13px;
		font-weight: 700;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	.sb-user-sub {
		font-size: 11px;
		color: var(--muted-fg);
	}
	.app-main {
		flex: 1;
		display: flex;
		flex-direction: column;
		overflow: hidden;
	}
</style>
