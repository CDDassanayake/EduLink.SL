<script lang="ts">
	import { page } from '$app/stores';

	let { children } = $props();
</script>

<div class="app-wrap">
	<nav class="sidebar admin-sidebar">
		<div class="sb-logo">
			<div class="sb-logo-txt">EDULINK.SL</div>
			<div class="sb-logo-role" style="color: #E8930E">Admin Console</div>
		</div>
		<div class="sb-section">Platform</div>
		<a href="/admin/dashboard" class="sb-link {$page.url.pathname === '/admin/dashboard' ? 'active' : ''}">
			<i class="ti ti-chart-bar"></i>Analytics
		</a>
		<a href="/admin/verifications" class="sb-link">
			<i class="ti ti-shield-check"></i>Verifications
			<span style="background: var(--saffron); color: #fff; font-size: 9px; font-weight: 800; padding: 1px 6px; border-radius: 100px; margin-left: auto">4</span>
		</a>
		<a href="/admin/users" class="sb-link">
			<i class="ti ti-users"></i>Users
		</a>
		<a href="/admin/disputes" class="sb-link">
			<i class="ti ti-alert-triangle"></i>Disputes
		</a>
		<a href="/admin/reviews" class="sb-link">
			<i class="ti ti-flag"></i>Flagged reviews
		</a>
		<div class="sb-spacer"></div>
		<div class="sb-section">System</div>
		<a href="/admin/settings" class="sb-link">
			<i class="ti ti-settings"></i>Settings
		</a>
		<a href="/auth/login" class="sb-link">
			<i class="ti ti-logout"></i>Log out
		</a>
		<div class="sb-user">
			<div class="sb-avatar" style="background: rgba(220, 38, 38, 0.2); color: #FCA5A5">AD</div>
			<div class="sb-user-info">
				<div class="sb-user-name">Admin</div>
				<div class="sb-user-sub">Super admin</div>
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
	.admin-sidebar {
		background: #0A0F2A;
		border-right: 1px solid rgba(255, 255, 255, 0.06);
	}
	.sb-logo {
		margin-bottom: 24px;
	}
	.sb-logo-txt {
		font-size: 16px;
		font-weight: 800;
		color: #fff;
		letter-spacing: -0.3px;
	}
	.sb-logo-role {
		font-size: 11px;
		color: rgba(255, 255, 255, 0.5);
		margin-top: 2px;
	}
	.sb-section {
		font-size: 10px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.8px;
		color: rgba(255, 255, 255, 0.4);
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
		color: rgba(255, 255, 255, 0.6);
		text-decoration: none;
		transition: all 0.15s;
		margin-bottom: 2px;
	}
	.sb-link:hover {
		background: rgba(255, 255, 255, 0.06);
		color: #fff;
	}
	.sb-link.active {
		background: rgba(232, 147, 14, 0.15);
		color: var(--saffron);
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
		border-top: 1px solid rgba(255, 255, 255, 0.06);
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
		color: #fff;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	.sb-user-sub {
		font-size: 11px;
		color: rgba(255, 255, 255, 0.5);
	}
	.app-main {
		flex: 1;
		display: flex;
		flex-direction: column;
		overflow: hidden;
	}
</style>
