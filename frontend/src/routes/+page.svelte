<script lang="ts">
	import { goto } from '$app/navigation';
</script>

<svelte:head>
	<title>EduLink SL — The standard for education in Sri Lanka</title>
</svelte:head>

<!-- ── NAVIGATION ────────────────────────────── -->
<header class="pub-nav">
	<div class="container">
		<a href="/" class="nav-logo">EDULINK.SL</a>
		<nav class="nav-links">
			<a href="/find-tutors" class="nav-link">Find Tutors</a>
			<a href="/streams" class="nav-link">Streams</a>
			<a href="/career-guidance" class="nav-link">Career Guidance</a>
		</nav>
		<div class="nav-right">
			<a href="/auth/login" class="btn btn-ghost btn-sm">Log in</a>
			<a href="/auth/register?role=teacher" class="btn btn-primary btn-sm">Become a Tutor</a>
		</div>
	</div>
</header>

<!-- ── HERO ──────────────────────────────────── -->
<section class="hero-section">
	<div class="container">
		<div class="hero-inner">
			<div class="pill-badge" style="margin-bottom: 20px">
				<span class="pill-badge-dot"></span>
				4,200+ Verified Sri Lankan Tutors
			</div>
			<h1 class="hero-h1">Master your future<br>with <em>precision.</em></h1>
			<p class="hero-sub">
				Sri Lanka's trusted marketplace for O/L, A/L and University students. Connect with merit-awarded educators in your district.
			</p>
			<div class="search-card">
				<div class="search-field">
					<label>Subject</label>
					<input type="text" placeholder="Combined Maths, Physics..." />
				</div>
				<div class="search-sep"></div>
				<div class="search-field">
					<label>District</label>
					<input type="text" placeholder="Colombo" />
				</div>
				<a href="/find-tutors" class="btn btn-saffron" style="flex-shrink: 0">Find Tutors →</a>
			</div>
			<div class="hero-stats">
				<div class="hstat">
					<div class="hstat-val">4,200+</div>
					<div class="hstat-lbl">Verified Tutors</div>
				</div>
				<div class="hstat">
					<div class="hstat-val">4.8 <span class="hstat-star">★</span></div>
					<div class="hstat-lbl">Avg. Rating</div>
				</div>
				<div class="hstat">
					<div class="hstat-val">25</div>
					<div class="hstat-lbl">Districts</div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- ── STREAMS + AI GUIDE ────────────────────── -->
<section class="streams-section">
	<div class="container">
		<div class="streams-grid">
			<!-- AI Career Guide card -->
			<div class="ai-card">
				<div class="ai-icon-wrap"><i class="ti ti-sparkles"></i></div>
				<div class="ai-card-title">Not sure which path to take?</div>
				<div class="ai-card-desc">
					Our AI Career Guide analyses your interests and subjects to recommend the perfect A/L stream or undergraduate degree — tuned for the Sri Lankan curriculum.
				</div>
				<a href="/auth/login?redirect=career-guidance" class="btn btn-outline-white" style="align-self: flex-start">Try AI Career Guide →</a>
			</div>
			<!-- Stream cards -->
			<div class="stream-cards">
				<a href="/find-tutors?stream=physical-science" class="stream-card sc-01">
					<div class="stream-num">Stream 01 <i class="ti ti-cpu"></i></div>
					<div class="stream-name">Physical Science</div>
					<div class="stream-subs">Maths, Physics, Chemistry, ICT</div>
					<div class="stream-cta">Explore tutors →</div>
				</a>
				<a href="/find-tutors?stream=biological-science" class="stream-card sc-02">
					<div class="stream-num">Stream 02 <i class="ti ti-book"></i></div>
					<div class="stream-name">Biological Science</div>
					<div class="stream-subs">Biology, Physics, Chemistry</div>
					<div class="stream-cta">Explore tutors →</div>
				</a>
				<a href="/find-tutors?stream=commerce" class="stream-card sc-03">
					<div class="stream-num">Stream 03 <i class="ti ti-briefcase"></i></div>
					<div class="stream-name">Commerce</div>
					<div class="stream-subs">Accounting, Econ, Business Studies</div>
					<div class="stream-cta">Explore tutors →</div>
				</a>
				<a href="/find-tutors?stream=arts" class="stream-card sc-04">
					<div class="stream-num">Stream 04 <i class="ti ti-palette"></i></div>
					<div class="stream-name">Arts & Languages</div>
					<div class="stream-subs">History, Political Science, Sinhala</div>
					<div class="stream-cta">Explore tutors →</div>
				</a>
			</div>
		</div>
	</div>
</section>

<!-- ── HIGHLY RATED EDUCATORS ───────────────── -->
<section class="tutors-section">
	<div class="container">
		<div class="sec-head">
			<div>
				<div class="sec-title">Highly rated educators</div>
				<div class="sec-sub" style="margin-top: 6px">Tutors with proven merit records and student success stories across Sri Lanka.</div>
			</div>
			<a href="/find-tutors" class="sec-action">View all verified tutors</a>
		</div>
		<div class="tutors-grid">
			<!-- Tutor 1 -->
			<a href="/auth/login?redirect=tutor-profile" class="tutor-card" style="display: block">
				<div class="tc-header">
					<div class="tc-photo" style="background: #EEF2FF; color: #4F6EF7; font-size: 22px; font-weight: 800">AP</div>
					<div>
						<div class="tc-name">Aruna Perera <span class="verified-tick"></span></div>
						<div class="tc-specialty">Physics Specialist (A/L)</div>
						<div class="tc-metrics">
							<span class="badge-merit">MERIT 98</span>
							<span class="tc-rating"><span class="star">★</span> 4.9</span>
							<span class="tc-count">(120)</span>
						</div>
					</div>
				</div>
				<div class="tc-tags">
					<span class="tag">Colombo 07</span>
					<span class="tag">Individual</span>
					<span class="tag">Theory + Revision</span>
				</div>
				<div class="tc-footer">
					<div class="tc-price">LKR 3,500<span>/hr</span></div>
					<span style="font-size: 13px; font-weight: 700; color: var(--fg)">View profile →</span>
				</div>
			</a>
			<!-- Tutor 2 -->
			<a href="/auth/login?redirect=tutor-profile" class="tutor-card" style="display: block">
				<div class="tc-header">
					<div class="tc-photo" style="background: #FFF0E0; color: #B06000; font-size: 22px; font-weight: 800">DJ</div>
					<div>
						<div class="tc-name">Dilini Jayasuriya <span class="verified-tick"></span></div>
						<div class="tc-specialty">Combined Maths (A/L)</div>
						<div class="tc-metrics">
							<span class="badge-merit">MERIT 94</span>
							<span class="tc-rating"><span class="star">★</span> 5.0</span>
							<span class="tc-count">(85)</span>
						</div>
					</div>
				</div>
				<div class="tc-tags">
					<span class="tag">Kandy</span>
					<span class="tag">Online</span>
					<span class="tag">Group Classes</span>
				</div>
				<div class="tc-footer">
					<div class="tc-price">LKR 2,000<span>/hr</span></div>
					<span style="font-size: 13px; font-weight: 700; color: var(--fg)">View profile →</span>
				</div>
			</a>
			<!-- Tutor 3 -->
			<a href="/auth/login?redirect=tutor-profile" class="tutor-card" style="display: block">
				<div class="tc-header">
					<div class="tc-photo" style="background: #F0FDF4; color: #166534; font-size: 22px; font-weight: 800">RS</div>
					<div>
						<div class="tc-name">Dr. Rohan Silva <span class="verified-tick"></span></div>
						<div class="tc-specialty">Chemistry Specialist (A/L)</div>
						<div class="tc-metrics">
							<span class="badge-merit">MERIT 99</span>
							<span class="tc-rating"><span class="star">★</span> 4.9</span>
							<span class="tc-count">(310)</span>
						</div>
					</div>
				</div>
				<div class="tc-tags">
					<span class="tag">Gampaha</span>
					<span class="tag">Physical</span>
					<span class="tag">Ex-Paper Marker</span>
				</div>
				<div class="tc-footer">
					<div class="tc-price">LKR 4,500<span>/hr</span></div>
					<span style="font-size: 13px; font-weight: 700; color: var(--fg)">View profile →</span>
				</div>
			</a>
		</div>
	</div>
</section>

<!-- ── HOW IT WORKS ───────────────────────────── -->
<section class="hiw-section">
	<div class="container">
		<div style="text-align: center; max-width: 540px; margin: 0 auto">
			<div class="sec-title">Simple. Trusted. Effective.</div>
			<div class="sec-sub" style="margin-top: 8px">Get from search to first session in under 5 minutes.</div>
		</div>
		<div class="hiw-grid">
			<div class="hiw-card">
				<div class="hiw-num">01</div>
				<div class="hiw-title">Search & Filter</div>
				<div class="hiw-desc">Browse verified tutors by subject, district, A/L stream, and budget. Filter by online or in-person.</div>
			</div>
			<div class="hiw-card">
				<div class="hiw-num">02</div>
				<div class="hiw-title">Book a Session</div>
				<div class="hiw-desc">Pick an available time slot, choose single session or monthly package, and pay securely through our platform.</div>
			</div>
			<div class="hiw-card">
				<div class="hiw-num">03</div>
				<div class="hiw-title">Learn & Track Progress</div>
				<div class="hiw-desc">Attend your class, track your sessions in your dashboard, and leave a verified review after completion.</div>
			</div>
		</div>
	</div>
</section>

<!-- ── DARK CTA ───────────────────────────────── -->
<section class="cta-section">
	<div class="container">
		<h2 class="cta-title">The standard for education in Sri Lanka.</h2>
		<div class="cta-btns">
			<a href="/auth/register?role=student" class="btn btn-saffron btn-lg">Start learning</a>
			<a href="/auth/register?role=teacher" class="btn btn-outline-white btn-lg">Join as tutor</a>
		</div>
	</div>
</section>

<!-- ── FOOTER ─────────────────────────────────── -->
<footer class="pub-footer">
	<div class="container">
		<div class="footer-top">
			<div>
				<div class="footer-logo">EDULINK.SL</div>
				<div class="footer-tagline">Sri Lanka's trusted tutor marketplace, empowering students from O/L through university since 2025.</div>
			</div>
			<div>
				<div class="footer-col-title">Navigation</div>
				<a href="/find-tutors" class="footer-link">Search tutors</a>
				<a href="/streams" class="footer-link">A/L streams</a>
				<a href="/streams#ol" class="footer-link">O/L program</a>
				<a href="/career-guidance" class="footer-link">University entry</a>
			</div>
			<div>
				<div class="footer-col-title">Support</div>
				<a href="#" class="footer-link">Help center</a>
				<a href="#" class="footer-link">Safety</a>
				<a href="/auth/register?role=teacher" class="footer-link">Verification</a>
				<a href="#" class="footer-link">Contact</a>
			</div>
		</div>
		<div class="footer-bottom">
			<div class="footer-logo" style="font-size: 14px">EDULINK.SL</div>
			<div>© 2026 EduLink Sri Lanka. Empowering the next generation.</div>
		</div>
	</div>
</footer>

<style>
	/* Hero */
	.hero-section {
		background: radial-gradient(ellipse at 75% 55%, #FBDCAA 0%, #FEF3E0 35%, #FAF9F4 68%);
		padding: 72px 0 80px;
	}
	.hero-inner {
		max-width: 680px;
	}
	.hero-h1 {
		font-size: 52px;
		font-weight: 800;
		line-height: 1.05;
		color: var(--fg);
		margin-bottom: 14px;
	}
	.hero-h1 em {
		font-family: var(--ff-serif);
		font-style: italic;
		color: var(--saffron);
		font-weight: 600;
	}
	.hero-sub {
		font-size: 16px;
		color: var(--muted-fg);
		line-height: 1.65;
		max-width: 520px;
		margin-bottom: 28px;
	}
	.search-card {
		background: #fff;
		border-radius: var(--r-xl);
		padding: 8px 8px 8px 16px;
		display: flex;
		align-items: center;
		gap: 12px;
		max-width: 560px;
		box-shadow: 0 8px 32px rgba(28,34,64,.14);
		margin-bottom: 36px;
	}
	.search-field {
		flex: 1;
	}
	.search-field label {
		display: block;
		font-size: 10px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: .6px;
		color: var(--muted-fg);
		margin-bottom: 2px;
	}
	.search-field input {
		border: none;
		outline: none;
		font-size: 14px;
		color: var(--fg);
		font-family: var(--ff);
		width: 100%;
		background: transparent;
	}
	.search-sep {
		width: 1px;
		height: 36px;
		background: var(--border-dk);
		flex-shrink: 0;
	}
	.hero-stats {
		display: flex;
		gap: 32px;
	}
	.hstat {
		display: flex;
		flex-direction: column;
	}
	.hstat-val {
		font-size: 22px;
		font-weight: 800;
		color: var(--fg);
		display: flex;
		align-items: center;
		gap: 5px;
	}
	.hstat-star {
		color: var(--saffron);
	}
	.hstat-lbl {
		font-size: 10px;
		font-family: var(--ff-mono);
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: .6px;
		color: var(--muted-fg);
		margin-top: 2px;
	}

	/* Streams section */
	.streams-section {
		padding: 72px 0;
		background: var(--bg);
	}
	.streams-grid {
		display: grid;
		grid-template-columns: 1fr 1.5fr;
		gap: 20px;
	}
	.ai-card {
		background: var(--primary);
		border-radius: var(--r-lg);
		padding: 32px 28px;
		display: flex;
		flex-direction: column;
		gap: 16px;
	}
	.ai-icon-wrap {
		width: 44px;
		height: 44px;
		background: rgba(255,255,255,.1);
		border-radius: var(--r);
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.ai-icon-wrap i {
		font-size: 22px;
		color: var(--saffron);
	}
	.ai-card-title {
		font-size: 22px;
		font-weight: 800;
		color: #fff;
		line-height: 1.25;
	}
	.ai-card-desc {
		font-size: 14px;
		color: rgba(255,255,255,.65);
		line-height: 1.6;
		flex: 1;
	}
	.stream-cards {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 14px;
	}
	.stream-card {
		border-radius: var(--r-lg);
		padding: 22px 20px;
		border: 1.5px solid var(--border-dk);
		cursor: pointer;
		transition: all .2s;
	}
	.stream-card:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
		box-shadow: var(--sh-sm);
	}
	.stream-num {
		font-family: var(--ff-mono);
		font-size: 10px;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: .6px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-bottom: 12px;
	}
	.stream-num i {
		font-size: 18px;
	}
	.stream-name {
		font-size: 18px;
		font-weight: 800;
		color: var(--fg);
		margin-bottom: 5px;
	}
	.stream-subs {
		font-size: 12px;
		color: var(--muted-fg);
		margin-bottom: 14px;
	}
	.stream-cta {
		font-size: 13px;
		font-weight: 700;
		color: var(--fg);
		display: flex;
		align-items: center;
		gap: 5px;
	}

	/* stream colors */
	.sc-01 {
		background: #EEF9F7;
		border-color: rgba(43,139,124,.2);
	}
	.sc-01 .stream-num {
		color: var(--teal);
	}
	.sc-01 .stream-num i {
		color: var(--teal);
	}
	.sc-02 {
		background: var(--saffron-lt);
		border-color: rgba(232,147,14,.2);
	}
	.sc-02 .stream-num {
		color: var(--saffron-hv);
	}
	.sc-02 .stream-num i {
		color: var(--saffron);
	}
	.sc-03 {
		background: var(--muted);
		border-color: var(--border-dk);
	}
	.sc-03 .stream-num {
		color: var(--muted-fg);
	}
	.sc-04 {
		background: var(--muted);
		border-color: var(--border-dk);
	}
	.sc-04 .stream-num {
		color: var(--muted-fg);
	}

	/* Tutors section */
	.tutors-section {
		padding: 72px 0;
		background: #fff;
	}
	.tutors-grid {
		display: grid;
		grid-template-columns: repeat(3,1fr);
		gap: 20px;
		margin-top: 28px;
	}

	/* How it works */
	.hiw-section {
		padding: 72px 0;
		background: var(--bg);
	}
	.hiw-grid {
		display: grid;
		grid-template-columns: repeat(3,1fr);
		gap: 28px;
		margin-top: 36px;
	}
	.hiw-card {
		background: var(--card);
		border-radius: var(--r-lg);
		padding: 28px 24px;
		border: 1px solid var(--border-dk);
	}
	.hiw-num {
		width: 36px;
		height: 36px;
		background: var(--saffron);
		border-radius: var(--r-sm);
		display: flex;
		align-items: center;
		justify-content: center;
		font-family: var(--ff-mono);
		font-size: 14px;
		font-weight: 800;
		color: #fff;
		margin-bottom: 16px;
	}
	.hiw-title {
		font-size: 17px;
		font-weight: 700;
		margin-bottom: 8px;
	}
	.hiw-desc {
		font-size: 13px;
		color: var(--muted-fg);
		line-height: 1.6;
	}

	/* Dark CTA section */
	.cta-section {
		background: var(--primary);
		padding: 80px 0;
		position: relative;
		overflow: hidden;
	}
	.cta-section::before {
		content: '';
		position: absolute;
		top: -50%;
		right: -10%;
		width: 600px;
		height: 600px;
		background: radial-gradient(ellipse, rgba(100,20,50,.35) 0%, transparent 65%);
	}
	.cta-section .container {
		position: relative;
		z-index: 1;
	}
	.cta-title {
		font-size: 44px;
		font-weight: 800;
		color: #fff;
		max-width: 500px;
		line-height: 1.1;
		margin-bottom: 24px;
	}
	.cta-btns {
		display: flex;
		gap: 14px;
		align-items: center;
	}
</style>
