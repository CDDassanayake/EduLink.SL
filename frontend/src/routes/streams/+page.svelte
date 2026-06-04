<script lang="ts">
</script>

<svelte:head>
	<title>A/L Streams — EduLink SL</title>
</svelte:head>

<header class="pub-nav">
	<div class="container">
		<a href="/" class="nav-logo">EDULINK.SL</a>
		<nav class="nav-links">
			<a href="/find-tutors" class="nav-link">Find Tutors</a>
			<a href="/streams" class="nav-link" style="color: var(--saffron)">Streams</a>
			<a href="/career-guidance" class="nav-link">Career Guidance</a>
		</nav>
		<div class="nav-right">
			<a href="/auth/login" class="btn btn-ghost btn-sm">Log in</a>
			<a href="/auth/register?role=teacher" class="btn btn-primary btn-sm">Become a Tutor</a>
		</div>
	</div>
</header>

<!-- Hero -->
<section class="streams-hero">
	<div class="container">
		<div class="pill-badge" style="margin-bottom: 18px"><span class="pill-badge-dot"></span>Sri Lankan A/L Curriculum</div>
		<h1>Explore A/L <em>streams</em> & find the right tutor</h1>
		<p>Browse all four A/L streams and the O/L programme. Every tutor on EduLink SL is verified and matched to their subject qualifications.</p>
	</div>
</section>

<!-- Stream 01: Physical Science -->
<section class="stream-section">
	<div class="container">
		<div class="stream-header">
			<div>
				<div class="stream-num-label" style="color: var(--teal)">Stream 01</div>
				<div class="stream-name">Physical Science</div>
				<div class="stream-desc">The most competitive A/L stream, leading to Engineering, IT, and Physical Sciences degrees. Requires strong mathematical ability and logical thinking.</div>
				<div style="display: flex; gap: 10px; margin-top: 16px; flex-wrap: wrap">
					<a href="/find-tutors?stream=physical-science" class="btn btn-saffron">Find tutors →</a>
					<a href="/career-guidance" class="btn btn-outline">Career paths →</a>
				</div>
			</div>
			<div>
				<div style="font-size: 12px; font-weight: 700; color: var(--muted-fg); margin-bottom: 10px; font-family: var(--ff-mono); text-transform: uppercase; letter-spacing: 0.5px">Core subjects</div>
				<div class="subjects-grid">
					<div class="subject-card"><i class="ti ti-calculator" style="color: var(--teal)"></i><div><div class="subject-name">Combined Maths</div><div class="subject-sub">Pure + Applied</div></div></div>
					<div class="subject-card"><i class="ti ti-atom" style="color: var(--primary)"></i><div><div class="subject-name">Physics</div><div class="subject-sub">Mechanics + Waves</div></div></div>
					<div class="subject-card"><i class="ti ti-flask" style="color: var(--saffron)"></i><div><div class="subject-name">Chemistry</div><div class="subject-sub">Organic + Inorganic</div></div></div>
					<div class="subject-card"><i class="ti ti-device-laptop" style="color: var(--teal)"></i><div><div class="subject-name">ICT</div><div class="subject-sub">Optional</div></div></div>
				</div>
			</div>
		</div>
		<div style="font-size: 13px; font-weight: 700; color: var(--muted-fg); margin-bottom: 12px; font-family: var(--ff-mono); text-transform: uppercase; letter-spacing: 0.5px">Top rated tutors for this stream</div>
		<div class="tutors-mini">
			<a href="/tutor/1" class="tutor-mini-card">
				<div class="tmc-photo" style="background: #EEF2FF; color: #3B4FD8">AP</div>
				<div class="tmc-name">Aruna Perera</div>
				<div class="tmc-spec">Physics</div>
				<div style="color: var(--saffron); font-size: 12px; margin-bottom: 4px">★★★★★ 4.9</div>
				<span class="badge-merit tmc-merit">MERIT 98</span>
			</a>
			<a href="/tutor/2" class="tutor-mini-card">
				<div class="tmc-photo" style="background: #FFF0E0; color: #A06000">DJ</div>
				<div class="tmc-name">Dilini Jayasuriya</div>
				<div class="tmc-spec">Combined Maths</div>
				<div style="color: var(--saffron); font-size: 12px; margin-bottom: 4px">★★★★★ 5.0</div>
				<span class="badge-merit tmc-merit">MERIT 94</span>
			</a>
			<a href="/tutor/3" class="tutor-mini-card">
				<div class="tmc-photo" style="background: #F0FDF4; color: #166534">RS</div>
				<div class="tmc-name">Dr. Rohan Silva</div>
				<div class="tmc-spec">Chemistry</div>
				<div style="color: var(--saffron); font-size: 12px; margin-bottom: 4px">★★★★★ 4.9</div>
				<span class="badge-merit tmc-merit">MERIT 99</span>
			</a>
		</div>
	</div>
</section>

<!-- Stream 02: Biological Science -->
<section class="stream-section">
	<div class="container">
		<div class="stream-header">
			<div>
				<div class="stream-num-label" style="color: var(--saffron)">Stream 02</div>
				<div class="stream-name">Biological Science</div>
				<div class="stream-desc">Leads to Medicine, Dentistry, Nursing, Agriculture, and Veterinary Science. Requires strong memory and analytical skills in the life sciences.</div>
				<div style="display: flex; gap: 10px; margin-top: 16px; flex-wrap: wrap">
					<a href="/find-tutors?stream=biological-science" class="btn btn-saffron">Find tutors →</a>
					<a href="/career-guidance" class="btn btn-outline">Career paths →</a>
				</div>
			</div>
			<div>
				<div style="font-size: 12px; font-weight: 700; color: var(--muted-fg); margin-bottom: 10px; font-family: var(--ff-mono); text-transform: uppercase; letter-spacing: 0.5px">Core subjects</div>
				<div class="subjects-grid">
					<div class="subject-card"><i class="ti ti-dna" style="color: var(--green)"></i><div><div class="subject-name">Biology</div><div class="subject-sub">Botany + Zoology</div></div></div>
					<div class="subject-card"><i class="ti ti-atom" style="color: var(--primary)"></i><div><div class="subject-name">Physics</div><div class="subject-sub">Core concepts</div></div></div>
					<div class="subject-card"><i class="ti ti-flask" style="color: var(--saffron)"></i><div><div class="subject-name">Chemistry</div><div class="subject-sub">Biochemistry focus</div></div></div>
				</div>
			</div>
		</div>
		<div style="font-size: 13px; font-weight: 700; color: var(--muted-fg); margin-bottom: 12px; font-family: var(--ff-mono); text-transform: uppercase; letter-spacing: 0.5px">Top rated tutors for this stream</div>
		<div class="tutors-mini">
			<a href="/tutor/4" class="tutor-mini-card">
				<div class="tmc-photo" style="background: #FDF4FF; color: #7C3AED">NK</div>
				<div class="tmc-name">Nadeesha Kumari</div>
				<div class="tmc-spec">Biology</div>
				<div style="color: var(--saffron); font-size: 12px; margin-bottom: 4px">★★★★★ 4.7</div>
				<span class="badge-merit tmc-merit">MERIT 91</span>
			</a>
			<a href="/tutor/3" class="tutor-mini-card">
				<div class="tmc-photo" style="background: #F0FDF4; color: #166534">RS</div>
				<div class="tmc-name">Dr. Rohan Silva</div>
				<div class="tmc-spec">Chemistry</div>
				<div style="color: var(--saffron); font-size: 12px; margin-bottom: 4px">★★★★★ 4.9</div>
				<span class="badge-merit tmc-merit">MERIT 99</span>
			</a>
			<a href="/find-tutors?stream=biological-science" class="tutor-mini-card" style="display: flex; align-items: center; justify-content: center; flex-direction: column; background: var(--bg)">
				<i class="ti ti-search" style="font-size: 22px; color: var(--muted-fg); margin-bottom: 6px"></i>
				<div style="font-size: 12px; font-weight: 600; color: var(--saffron)">Browse all tutors →</div>
			</a>
		</div>
	</div>
</section>

<!-- Stream 03 & 04 compact -->
<section style="padding: 52px 0; background: var(--bg)">
	<div class="container">
		<div class="grid-2">
			<div>
				<div class="stream-num-label" style="color: var(--muted-fg)">Stream 03</div>
				<div style="font-size: 22px; font-weight: 800; margin-bottom: 8px">Commerce</div>
				<div style="font-size: 14px; color: var(--muted-fg); line-height: 1.6; margin-bottom: 14px">Leads to Accountancy, Finance, Management, and Business degrees. Strong analytical and numerical skills required.</div>
				<div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px">
					<div class="subject-card" style="padding: 10px 12px"><i class="ti ti-report-money" style="color: var(--saffron); font-size: 16px"></i><div><div class="subject-name" style="font-size: 12px">Accounting</div></div></div>
					<div class="subject-card" style="padding: 10px 12px"><i class="ti ti-trending-up" style="color: var(--green); font-size: 16px"></i><div><div class="subject-name" style="font-size: 12px">Economics</div></div></div>
					<div class="subject-card" style="padding: 10px 12px"><i class="ti ti-briefcase" style="color: var(--primary); font-size: 16px"></i><div><div class="subject-name" style="font-size: 12px">Business Studies</div></div></div>
				</div>
				<a href="/find-tutors?stream=commerce" class="btn btn-saffron btn-sm">Find Commerce tutors →</a>
			</div>
			<div>
				<div class="stream-num-label" style="color: var(--muted-fg)">Stream 04</div>
				<div style="font-size: 22px; font-weight: 800; margin-bottom: 8px">Arts & Languages</div>
				<div style="font-size: 14px; color: var(--muted-fg); line-height: 1.6; margin-bottom: 14px">Leads to Law, Social Sciences, Arts, and Humanities degrees. Strong language and critical thinking skills valued.</div>
				<div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px">
					<div class="subject-card" style="padding: 10px 12px"><i class="ti ti-history" style="color: var(--primary); font-size: 16px"></i><div><div class="subject-name" style="font-size: 12px">History</div></div></div>
					<div class="subject-card" style="padding: 10px 12px"><i class="ti ti-writing" style="color: var(--saffron); font-size: 16px"></i><div><div class="subject-name" style="font-size: 12px">Sinhala</div></div></div>
					<div class="subject-card" style="padding: 10px 12px"><i class="ti ti-language" style="color: var(--teal); font-size: 16px"></i><div><div class="subject-name" style="font-size: 12px">English Lit.</div></div></div>
				</div>
				<a href="/find-tutors?stream=arts" class="btn btn-saffron btn-sm">Find Arts tutors →</a>
			</div>
		</div>
	</div>
</section>

<!-- O/L section -->
<section class="ol-section" id="ol">
	<div class="container">
		<div style="margin-bottom: 28px">
			<div class="pill-badge" style="margin-bottom: 12px"><span class="pill-badge-dot"></span>O/L Programme · Grade 9–11</div>
			<div style="font-size: 26px; font-weight: 800; margin-bottom: 8px">O/L subjects</div>
			<div style="font-size: 14px; color: var(--muted-fg); max-width: 520px">Build a strong foundation for A/L success. Our O/L tutors are verified specialists in the national curriculum.</div>
		</div>
		<div class="ol-grid">
			<a href="/find-tutors?subject=ol-maths" class="ol-card"><i class="ti ti-calculator" style="color: var(--teal)"></i><div class="ol-card-name">Mathematics</div><div class="ol-card-sub">Full syllabus coverage</div></a>
			<a href="/find-tutors?subject=ol-science" class="ol-card"><i class="ti ti-flask" style="color: var(--saffron)"></i><div class="ol-card-name">Science</div><div class="ol-card-sub">Physics, Chemistry, Biology</div></a>
			<a href="/find-tutors?subject=ol-english" class="ol-card"><i class="ti ti-language" style="color: var(--primary)"></i><div class="ol-card-name">English</div><div class="ol-card-sub">Language & Literature</div></a>
			<a href="/find-tutors?subject=ol-sinhala" class="ol-card"><i class="ti ti-writing" style="color: var(--green)"></i><div class="ol-card-name">Sinhala</div><div class="ol-card-sub">First language</div></a>
			<a href="/find-tutors?subject=ol-history" class="ol-card"><i class="ti ti-history" style="color: var(--muted-fg)"></i><div class="ol-card-name">History</div><div class="ol-card-sub">Local & World</div></a>
			<a href="/find-tutors?subject=ol-ict" class="ol-card"><i class="ti ti-device-laptop" style="color: var(--teal)"></i><div class="ol-card-name">ICT</div><div class="ol-card-sub">Theory & practical</div></a>
			<a href="/find-tutors?subject=ol-commerce" class="ol-card"><i class="ti ti-briefcase" style="color: var(--saffron)"></i><div class="ol-card-name">Commerce</div><div class="ol-card-sub">Accounts & Economics</div></a>
			<a href="/find-tutors?subject=ol-religion" class="ol-card"><i class="ti ti-book" style="color: var(--muted-fg)"></i><div class="ol-card-name">Religion</div><div class="ol-card-sub">Buddhism & others</div></a>
		</div>
	</div>
</section>

<footer class="pub-footer">
	<div class="container">
		<div class="footer-bottom">
			<div class="footer-logo" style="font-size: 14px">EDULINK.SL</div>
			<div>© 2026 EduLink Sri Lanka. Empowering the next generation.</div>
		</div>
	</div>
</footer>

<style>
	.streams-hero {
		background: radial-gradient(ellipse at 70% 40%, #FDE8C0 0%, #FEF4E0 35%, #FAF9F4 65%);
		padding: 60px 0 52px;
	}
	.streams-hero h1 {
		font-size: 40px;
		font-weight: 800;
		max-width: 520px;
		line-height: 1.1;
		margin-bottom: 12px;
	}
	.streams-hero h1 em {
		font-family: var(--ff-serif);
		font-style: italic;
		color: var(--saffron);
		font-weight: 600;
	}
	.streams-hero p {
		font-size: 16px;
		color: var(--muted-fg);
		max-width: 460px;
		line-height: 1.65;
	}
	.stream-section {
		padding: 52px 0;
	}
	.stream-section:nth-child(even) {
		background: #fff;
	}
	.stream-header {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 32px;
		align-items: start;
		margin-bottom: 32px;
	}
	.stream-num-label {
		font-family: var(--ff-mono);
		font-size: 11px;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.8px;
		margin-bottom: 8px;
	}
	.stream-name {
		font-size: 28px;
		font-weight: 800;
		margin-bottom: 8px;
	}
	.stream-desc {
		font-size: 14px;
		color: var(--muted-fg);
		line-height: 1.65;
	}
	.subjects-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 10px;
	}
	.subject-card {
		background: #fff;
		border-radius: var(--r);
		border: 1.5px solid var(--border-dk);
		padding: 14px 16px;
		display: flex;
		align-items: center;
		gap: 10px;
		cursor: pointer;
		transition: all 0.2s;
	}
	.subject-card:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
		transform: translateY(-1px);
	}
	.subject-card i {
		font-size: 20px;
		flex-shrink: 0;
	}
	.subject-name {
		font-size: 13px;
		font-weight: 700;
	}
	.subject-sub {
		font-size: 11px;
		color: var(--muted-fg);
	}
	.tutors-mini {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 12px;
		margin-top: 14px;
	}
	.tutor-mini-card {
		background: #fff;
		border-radius: var(--r);
		border: 1px solid var(--border-dk);
		padding: 14px;
		text-align: center;
		cursor: pointer;
		transition: all 0.2s;
	}
	.tutor-mini-card:hover {
		border-color: var(--saffron);
		box-shadow: var(--sh-sm);
		transform: translateY(-2px);
	}
	.tmc-photo {
		width: 44px;
		height: 44px;
		border-radius: 50%;
		margin: 0 auto 8px;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 14px;
		font-weight: 800;
	}
	.tmc-name {
		font-size: 12px;
		font-weight: 700;
		margin-bottom: 2px;
	}
	.tmc-spec {
		font-size: 11px;
		color: var(--muted-fg);
		margin-bottom: 5px;
	}
	.tmc-merit {
		font-size: 9px;
	}
	.ol-section {
		background: var(--muted);
		padding: 52px 0;
	}
	.ol-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 14px;
	}
	.ol-card {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		padding: 18px;
		cursor: pointer;
		transition: all 0.2s;
	}
	.ol-card:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
		transform: translateY(-2px);
	}
	.ol-card i {
		font-size: 24px;
		margin-bottom: 10px;
		display: block;
	}
	.ol-card-name {
		font-size: 14px;
		font-weight: 700;
		margin-bottom: 4px;
	}
	.ol-card-sub {
		font-size: 12px;
		color: var(--muted-fg);
	}
</style>
