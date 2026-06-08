<script lang="ts">
	let showSuccess = $state(false);
	let cardNumber = $state('');
	let expiry = $state('');
	let cvv = $state('');
	let autoRenew = $state(true);

	function formatCardNumber(e: Event) {
		const input = e.target as HTMLInputElement;
		const value = input.value.replace(/\D/g, '').substring(0, 16);
		cardNumber = value.replace(/(.{4})/g, '$1 ').trim();
	}

	function handleImageError(e: Event) {
		const img = e.target as HTMLImageElement;
		img.style.display = 'none';
	}

	function activateListing() {
		showSuccess = true;
	}
</script>

<svelte:head>
	<title>Activate Listing — EduLink SL</title>
</svelte:head>

<div class="pay-page-wrapper">
<div class="pay-wrap">
	<div class="steps-bar" style="margin-bottom:28px">
		<div class="step-dot done">1</div><div class="step-line done"></div>
		<div class="step-dot done">2</div><div class="step-line done"></div>
		<div class="step-dot active">3</div>
		<span style="font-size:13px;color:var(--muted-fg);margin-left:8px">Activate your listing</span>
	</div>
	<div style="font-size:24px;font-weight:800;margin-bottom:4px">Activate your listing</div>
	<div style="font-size:14px;color:var(--muted-fg);margin-bottom:28px">Complete payment to make your A/L Physics listing visible to students.</div>

	<div class="pay-layout">
		<div class="pay-main">
			<!-- Order summary -->
			<div class="order-card">
				<div class="order-header">
					<div style="font-size:13px;font-weight:800;letter-spacing:.3px">ORDER SUMMARY</div>
				</div>
				<div class="order-item"><span>A/L Physics listing · Standard plan</span><span style="font-weight:700">LKR 1,200</span></div>
				<div class="order-item"><span style="color:var(--muted-fg)">Duration</span><span>90 days (until 22 Sep 2025)</span></div>
				<div class="order-item"><span style="color:var(--muted-fg)">Bookings included</span><span>Unlimited</span></div>
				<div class="order-item"><span style="color:var(--muted-fg)">Commission per session</span><span>10% of session fee</span></div>
				<div class="order-item"><span style="color:var(--muted-fg)">VAT (0%)</span><span>LKR 0</span></div>
				<div class="order-item total"><span>Total due today</span><span style="color:var(--saffron)">LKR 1,200</span></div>
			</div>

			<!-- Payment form -->
			<div class="section-card">
				<div style="font-size:15px;font-weight:700;margin-bottom:16px">Payment details</div>
				<div class="alert alert-info" style="margin-bottom:16px"><i class="ti ti-lock"></i> Secured by Stripe. Your card details are never stored on our servers.</div>
				<div class="form-group">
					<label class="form-label">Cardholder name</label>
					<input class="form-input" value="Aruna Perera">
				</div>
				<div class="form-group">
					<label class="form-label">Card number</label>
					<div style="position:relative">
						<input class="form-input" placeholder="1234 5678 9012 3456" bind:value={cardNumber} style="padding-right:80px" oninput={formatCardNumber}>
						<div style="position:absolute;right:12px;top:50%;transform:translateY(-50%);display:flex;gap:4px">
							<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/visa/visa-original.svg" style="width:28px;opacity:.6" onerror={handleImageError}>
						</div>
					</div>
				</div>
				<div class="card-row">
					<div class="form-group"><label class="form-label">Expiry</label><input class="form-input" placeholder="MM / YY" bind:value={expiry} maxlength="7"></div>
					<div class="form-group"><label class="form-label">CVV</label><input class="form-input" type="password" placeholder="•••" bind:value={cvv} maxlength="3"></div>
				</div>
				<div style="margin-top:4px">
					<label style="display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted-fg);cursor:pointer">
						<input type="checkbox" bind:checked={autoRenew} style="accent-color:var(--saffron)"> Auto-renew this listing when it expires
					</label>
				</div>
			</div>

			<!-- What happens next -->
			<div class="section-card" style="padding:16px 20px">
				<div style="font-size:13px;font-weight:700;margin-bottom:10px">What happens after payment?</div>
				<div style="display:flex;flex-direction:column;gap:8px">
					<div style="display:flex;gap:10px;font-size:13px;color:var(--muted-fg)"><i class="ti ti-check" style="color:var(--green);font-size:16px;flex-shrink:0"></i>Your listing goes live immediately and appears in student search results</div>
					<div style="display:flex;gap:10px;font-size:13px;color:var(--muted-fg)"><i class="ti ti-check" style="color:var(--green);font-size:16px;flex-shrink:0"></i>Students in your district and subject will see your profile first</div>
					<div style="display:flex;gap:10px;font-size:13px;color:var(--muted-fg)"><i class="ti ti-check" style="color:var(--green);font-size:16px;flex-shrink:0"></i>When a student books, you'll be notified by email and in-app</div>
					<div style="display:flex;gap:10px;font-size:13px;color:var(--muted-fg)"><i class="ti ti-check" style="color:var(--green);font-size:16px;flex-shrink:0"></i>Earnings are paid out weekly via bank transfer after platform commission</div>
				</div>
			</div>
		</div>

		<!-- Sticky panel -->
		<div class="pay-panel">
			<div class="listing-preview">
				<div style="font-size:10px;font-family:var(--ff-mono);font-weight:700;text-transform:uppercase;letter-spacing:.6px;color:var(--muted-fg);margin-bottom:8px">Activating</div>
				<div style="font-size:14px;font-weight:800;margin-bottom:2px">A/L Physics</div>
				<div style="font-size:12px;color:var(--muted-fg);margin-bottom:8px">Physical Science · Online · Individual</div>
				<div style="display:flex;align-items:center;justify-content:space-between">
					<span class="badge badge-saffron">Standard — 90 days</span>
					<span style="font-size:14px;font-weight:800">LKR 3,500/hr</span>
				</div>
			</div>
			<div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:6px;color:var(--muted-fg)"><span>Listing fee</span><span>LKR 1,200</span></div>
			<div style="display:flex;justify-content:space-between;font-size:15px;font-weight:800;border-top:1px solid var(--border-dk);padding-top:10px;margin-top:4px;margin-bottom:16px"><span>Total today</span><span style="color:var(--saffron)">LKR 1,200</span></div>
			<button class="btn btn-saffron btn-full btn-lg" onclick={activateListing}><i class="ti ti-lock"></i> Pay & Activate</button>
			<div style="display:flex;flex-direction:column;gap:6px;margin-top:12px">
				<div class="trust-item" style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted-fg)"><i class="ti ti-shield-check" style="color:var(--green)"></i> Secured by Stripe</div>
				<div class="trust-item" style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted-fg)"><i class="ti ti-refresh" style="color:var(--green)"></i> Cancel auto-renewal anytime</div>
				<div class="trust-item" style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted-fg)"><i class="ti ti-clock" style="color:var(--green)"></i> Goes live instantly after payment</div>
			</div>
		</div>
	</div>
</div>
</div>

{#if showSuccess}
	<div class="confirm-overlay" style="display:flex;position:fixed;inset:0;background:rgba(0,0,0,.4);backdrop-filter:blur(4px);z-index:200;align-items:center;justify-content:center">
		<div style="background:#fff;border-radius:var(--r-xl);padding:40px;max-width:400px;width:90%;text-align:center;box-shadow:var(--sh-lg)">
			<div style="width:72px;height:72px;background:var(--green-lt);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:32px;color:var(--green)"><i class="ti ti-check"></i></div>
			<h2 style="font-size:22px;font-weight:800;margin-bottom:6px">Listing activated!</h2>
			<p style="font-size:14px;color:var(--muted-fg);margin-bottom:20px">Your <strong>A/L Physics</strong> listing is now live and visible to students. You'll receive your first booking notification by email.</p>
			<a href="/teacher/dashboard" class="btn btn-primary btn-full btn-lg">Go to dashboard →</a>
		</div>
	</div>
{/if}

<style>
	.pay-page-wrapper {
		background: radial-gradient(ellipse at 50% 10%, var(--saffron-md) 0%, #FAF9F4 55%);
		min-height: 100vh;
	}
	.pay-wrap {
		max-width: 700px;
		margin: 0 auto;
		padding: 36px 24px 60px;
	}
	.pay-layout {
		display: grid;
		grid-template-columns: 1fr 280px;
		gap: 24px;
		align-items: start;
	}
	.pay-main {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}
	.order-card {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		overflow: hidden;
	}
	.order-header {
		background: var(--primary);
		padding: 16px 20px;
		color: #fff;
	}
	.order-item {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 13px 20px;
		border-bottom: 1px solid var(--border);
		font-size: 13px;
	}
	.order-item:last-child {
		border-bottom: none;
	}
	.order-item.total {
		font-weight: 800;
		font-size: 15px;
		background: var(--bg);
	}
	.pay-panel {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		padding: 22px;
		position: sticky;
		top: 80px;
	}
	.listing-preview {
		background: var(--bg);
		border-radius: var(--r-sm);
		padding: 14px;
		margin-bottom: 16px;
	}
	.card-row {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 12px;
	}
</style>
