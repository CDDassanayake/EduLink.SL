<script lang="ts">
	let showSuccess = false;
	let selectedSubjects = ['A/L Physics', 'Combined Maths'];
	let yearsOfExperience = '3–5 years';
	let teachingMode = 'Both online & in-person';
	let bio = 'I hold a BSc (Hons) in Physics from the University of Peradeniya with over 12 years of A/L teaching experience. My approach focuses on building strong fundamentals and exam technique.';

	function toggleSubject(subject: string) {
		if (selectedSubjects.includes(subject)) {
			selectedSubjects = selectedSubjects.filter(s => s !== subject);
		} else {
			selectedSubjects = [...selectedSubjects, subject];
		}
	}

	function submitVerif() {
		showSuccess = true;
	}
</script>

<svelte:head>
	<title>Account Verification — EduLink SL</title>
</svelte:head>

<div class="verif-page-wrapper">
<div class="verif-wrap">
	<div class="steps-bar" style="margin-bottom:28px">
		<div class="step-dot done">1</div>
		<div class="step-line done"></div>
		<div class="step-dot active">2</div>
		<div class="step-line"></div>
		<div class="step-dot">3</div>
	</div>

	<div class="verif-hero">
		<div class="verif-hero-icon"><i class="ti ti-shield-check"></i></div>
		<div>
			<div style="font-size:20px;font-weight:800;margin-bottom:4px">Verify your tutor account</div>
			<div style="font-size:14px;opacity:.8;line-height:1.6">Upload your identification and qualifications so our team can verify your account. This usually takes 1–2 business days. You cannot list classes until verification is approved.</div>
		</div>
	</div>

	<!-- Step 1: Identity -->
	<div class="section-card" style="margin-bottom:16px">
		<div style="font-size:15px;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px">
			<span style="width:24px;height:24px;background:var(--saffron);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#fff">1</span>
			National Identity Card (NIC)
		</div>
		<div style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Upload a clear photo of both sides of your NIC. PNG or JPG, max 5MB per file.</div>
		<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
			<div>
				<div style="font-size:12px;font-weight:600;color:var(--muted-fg);margin-bottom:6px;font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.4px">Front side</div>
				<div class="upload-box done">
					<i class="ti ti-check" style="color:var(--green)"></i>
					<div class="upload-box-title" style="color:var(--green)">NIC_front.jpg uploaded</div>
					<div class="upload-box-sub">Click to replace</div>
				</div>
			</div>
			<div>
				<div style="font-size:12px;font-weight:600;color:var(--muted-fg);margin-bottom:6px;font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.4px">Back side</div>
				<div class="upload-box">
					<i class="ti ti-upload" style="color:var(--muted-fg)"></i>
					<div class="upload-box-title">Upload back of NIC</div>
					<div class="upload-box-sub"><strong style="color:var(--saffron)">Click to browse</strong> or drag & drop</div>
				</div>
			</div>
		</div>
	</div>

	<!-- Step 2: Qualifications -->
	<div class="section-card" style="margin-bottom:16px">
		<div style="font-size:15px;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px">
			<span style="width:24px;height:24px;background:var(--saffron);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#fff">2</span>
			Academic qualifications
		</div>
		<div style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Upload your degree certificate, A/L results, or any other relevant qualification. You can upload multiple files.</div>
		<div class="dropzone" style="margin-bottom:14px">
			<i class="ti ti-file-certificate" style="font-size:36px;color:var(--muted-fg);display:block;margin-bottom:8px"></i>
			<div class="dropzone-txt"><strong style="color:var(--saffron)">Click to upload</strong> or drag & drop files here</div>
			<div style="font-size:11px;color:var(--muted-fg);margin-top:4px">PDF, JPG, PNG — Max 10MB each</div>
		</div>
		<div class="file-item">
			<div class="fi-icon" style="background:#FEF2F2;color:#DC2626"><i class="ti ti-file-type-pdf"></i></div>
			<div class="fi-name">BSc_Physics_UoP_Certificate.pdf</div>
			<div class="fi-size">2.4 MB</div>
			<i class="fi-remove ti ti-x"></i>
		</div>
		<div class="file-item">
			<div class="fi-icon" style="background:#EFF6FF;color:#2563EB"><i class="ti ti-file-type-jpg"></i></div>
			<div class="fi-name">AL_Results_Sheet_2012.jpg</div>
			<div class="fi-size">1.1 MB</div>
			<i class="fi-remove ti ti-x"></i>
		</div>
	</div>

	<!-- Step 3: Subjects -->
	<div class="section-card" style="margin-bottom:16px">
		<div style="font-size:15px;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px">
			<span style="width:24px;height:24px;background:var(--saffron);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#fff">3</span>
			Subjects you will teach
		</div>
		<div style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Select all subjects you intend to teach. Only subjects matching your uploaded qualifications will be approved.</div>
		<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">
			<label class="subject-checkbox {selectedSubjects.includes('A/L Physics') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('A/L Physics')} onchange={() => toggleSubject('A/L Physics')} />A/L Physics
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('Combined Maths') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('Combined Maths')} onchange={() => toggleSubject('Combined Maths')} />Combined Maths
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('A/L Chemistry') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('A/L Chemistry')} onchange={() => toggleSubject('A/L Chemistry')} />A/L Chemistry
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('O/L Mathematics') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('O/L Mathematics')} onchange={() => toggleSubject('O/L Mathematics')} />O/L Mathematics
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('O/L Science') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('O/L Science')} onchange={() => toggleSubject('O/L Science')} />O/L Science
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('O/L English') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('O/L English')} onchange={() => toggleSubject('O/L English')} />O/L English
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('ICT') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('ICT')} onchange={() => toggleSubject('ICT')} />ICT
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('A/L Biology') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('A/L Biology')} onchange={() => toggleSubject('A/L Biology')} />A/L Biology
			</label>
			<label class="subject-checkbox {selectedSubjects.includes('University Maths') ? 'checked' : ''}">
				<input type="checkbox" checked={selectedSubjects.includes('University Maths')} onchange={() => toggleSubject('University Maths')} />University Maths
			</label>
		</div>
	</div>

	<!-- Step 4: Teaching info -->
	<div class="section-card" style="margin-bottom:16px">
		<div style="font-size:15px;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px">
			<span style="width:24px;height:24px;background:var(--saffron);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#fff">4</span>
			Teaching experience
		</div>
		<div style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Tell us about your experience. This will appear on your public profile.</div>
		<div class="form-grid-2" style="margin-bottom:14px">
			<div class="form-group">
				<label class="form-label">Years of teaching experience</label>
				<select class="form-input" value={yearsOfExperience} onchange={(e) => yearsOfExperience = e.target.value}><option>Less than 1 year</option><option>1–3 years</option><option>3–5 years</option><option>5–10 years</option><option>10+ years</option></select>
			</div>
			<div class="form-group">
				<label class="form-label">Preferred teaching mode</label>
				<select class="form-input" value={teachingMode} onchange={(e) => teachingMode = e.target.value}><option>Online only</option><option>Both online & in-person</option><option>In-person only</option></select>
			</div>
		</div>
		<div class="form-group">
			<label class="form-label">Short bio (shown on your profile)</label>
			<textarea class="form-input" rows="3" value={bio} oninput={(e) => bio = e.target.value} placeholder="Describe your teaching approach, specialisations, and what makes you a great tutor..."></textarea>
		</div>
	</div>

	<!-- Submit -->
	<div class="submit-section">
		<div class="alert alert-warning" style="margin-bottom:16px"><i class="ti ti-info-circle"></i> By submitting, you confirm all uploaded documents are genuine. Fraudulent submissions result in permanent account ban.</div>
		<div style="display:flex;gap:12px;align-items:center">
			<button class="btn btn-primary btn-lg" onclick={submitVerif}><i class="ti ti-send"></i> Submit for verification</button>
			<div style="font-size:12px;color:var(--muted-fg)">Review takes 1–2 business days. We'll email you with the result.</div>
		</div>
	</div>
</div>
</div>

{#if showSuccess}
	<div class="confirm-overlay" style="display:flex;position:fixed;inset:0;background:rgba(0,0,0,.4);backdrop-filter:blur(4px);z-index:200;align-items:center;justify-content:center">
		<div style="background:#fff;border-radius:var(--r-xl);padding:40px;max-width:400px;width:100%;text-align:center;box-shadow:var(--sh-lg)">
			<div style="width:64px;height:64px;background:var(--saffron-lt);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:28px;color:var(--saffron)"><i class="ti ti-clock"></i></div>
			<h2 style="font-size:20px;font-weight:800;margin-bottom:6px">Application submitted!</h2>
			<p style="font-size:14px;color:var(--muted-fg);margin-bottom:20px">Our team will review your documents within 1–2 business days. You'll be notified by email once approved. You can explore your dashboard while you wait.</p>
			<a href="/teacher/dashboard" class="btn btn-primary btn-full">Go to teacher dashboard →</a>
		</div>
	</div>
{/if}

<style>
	.verif-page-wrapper {
		background: radial-gradient(ellipse at 50% 10%, #FEF3E0 0%, #FAF9F4 55%);
		min-height: 100vh;
	}
	.verif-wrap {
		max-width: 720px;
		margin: 0 auto;
		padding: 40px 24px 60px;
	}
	.verif-hero {
		background: var(--primary);
		border-radius: var(--r-xl);
		padding: 28px;
		color: #fff;
		margin-bottom: 28px;
		display: flex;
		gap: 16px;
		align-items: flex-start;
	}
	.verif-hero-icon {
		width: 48px;
		height: 48px;
		background: rgba(255,255,255,.1);
		border-radius: var(--r);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 24px;
		color: var(--saffron);
		flex-shrink: 0;
	}
	.upload-box {
		border: 2px dashed var(--border-dk);
		border-radius: var(--r);
		padding: 24px;
		text-align: center;
		cursor: pointer;
		transition: all .2s;
		margin-bottom: 8px;
		background: #fff;
	}
	.upload-box:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
	}
	.upload-box.done {
		border-color: var(--green);
		border-style: solid;
		background: var(--green-lt);
	}
	.upload-box i {
		font-size: 32px;
		display: block;
		margin-bottom: 8px;
	}
	.upload-box-title {
		font-size: 13px;
		font-weight: 700;
		margin-bottom: 3px;
	}
	.upload-box-sub {
		font-size: 12px;
		color: var(--muted-fg);
	}
	.file-item {
		display: flex;
		align-items: center;
		gap: 10px;
		background: #fff;
		border: 1px solid var(--border-dk);
		border-radius: var(--r-sm);
		padding: 10px 14px;
		margin-bottom: 6px;
	}
	.fi-icon {
		width: 32px;
		height: 32px;
		border-radius: var(--r-sm);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 15px;
		flex-shrink: 0;
	}
	.fi-name {
		flex: 1;
		font-size: 13px;
		font-weight: 600;
	}
	.fi-size {
		font-size: 11px;
		color: var(--muted-fg);
	}
	.fi-remove {
		color: var(--muted-fg);
		cursor: pointer;
		font-size: 16px;
		transition: color .15s;
	}
	.fi-remove:hover {
		color: var(--red);
	}
	.subject-checkbox {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 8px 12px;
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		cursor: pointer;
		transition: all .15s;
		background: #fff;
	}
	.subject-checkbox:hover {
		border-color: var(--saffron);
	}
	.subject-checkbox input {
		accent-color: var(--saffron);
	}
	.subject-checkbox.checked {
		border-color: var(--saffron);
		background: var(--saffron-lt);
	}
	.submit-section {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		padding: 22px;
		margin-top: 20px;
	}
	.verif-hero {
		background: var(--primary);
		border-radius: var(--r-xl);
		padding: 28px;
		color: #fff;
		margin-bottom: 28px;
		display: flex;
		gap: 16px;
		align-items: flex-start;
	}
	.verif-hero-icon {
		width: 48px;
		height: 48px;
		background: rgba(255,255,255,.1);
		border-radius: var(--r);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 24px;
		color: var(--saffron);
		flex-shrink: 0;
	}
	.upload-box {
		border: 2px dashed var(--border-dk);
		border-radius: var(--r);
		padding: 24px;
		text-align: center;
		cursor: pointer;
		transition: all .2s;
		margin-bottom: 8px;
		background: #fff;
	}
	.upload-box:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
	}
	.upload-box.done {
		border-color: var(--green);
		border-style: solid;
		background: var(--green-lt);
	}
	.upload-box i {
		font-size: 32px;
		display: block;
		margin-bottom: 8px;
	}
	.upload-box-title {
		font-size: 13px;
		font-weight: 700;
		margin-bottom: 3px;
	}
	.upload-box-sub {
		font-size: 12px;
		color: var(--muted-fg);
	}
	.file-item {
		display: flex;
		align-items: center;
		gap: 10px;
		background: #fff;
		border: 1px solid var(--border-dk);
		border-radius: var(--r-sm);
		padding: 10px 14px;
		margin-bottom: 6px;
	}
	.fi-icon {
		width: 32px;
		height: 32px;
		border-radius: var(--r-sm);
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 15px;
		flex-shrink: 0;
	}
	.fi-name {
		flex: 1;
		font-size: 13px;
		font-weight: 600;
	}
	.fi-size {
		font-size: 11px;
		color: var(--muted-fg);
	}
	.fi-remove {
		color: var(--muted-fg);
		cursor: pointer;
		font-size: 16px;
		transition: color .15s;
	}
	.fi-remove:hover {
		color: var(--red);
	}
	.subject-checkbox {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 8px 12px;
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		cursor: pointer;
		transition: all .15s;
		background: #fff;
	}
	.subject-checkbox:hover {
		border-color: var(--saffron);
	}
	.subject-checkbox input {
		accent-color: var(--saffron);
	}
	.subject-checkbox.checked {
		border-color: var(--saffron);
		background: var(--saffron-lt);
	}
	.submit-section {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		padding: 22px;
		margin-top: 20px;
	}
</style>
