<script lang="ts">
	import { getAuthStore } from '$lib/stores/auth.svelte';
	import { createOrUpdateTeacherProfile, getMyTeacherProfile, uploadDocument, type TeacherProfileDetail } from '$lib/api/tutors';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	let authStore = getAuthStore();
	let showSuccess = false;
	let isLoading = $state(false);
	let isUploading = $state(false);
	let error = $state('');
	let profile = $state<TeacherProfileDetail | null>(null);

	let yearsOfExperience = $state('');
	let bio = $state('');
	let uploadedFiles = $state<Array<{name: string, url: string}>>([]);

	onMount(async () => {
		// Allow access without authentication for registration flow
		// If authenticated, check role
		if (authStore.user && authStore.user.role !== 'TEACHER') {
			window.location.href = '/';
			return;
		}
		await loadProfile();
	});

	async function loadProfile() {
		// Only try to load profile if user is authenticated
		if (!authStore.user) {
			return;
		}

		try {
			profile = await getMyTeacherProfile();
			bio = profile.bio || '';
			yearsOfExperience = profile.years_experience ? profile.years_experience.toString() : '';
			if (profile.document_urls) {
				try {
					const docs = JSON.parse(profile.document_urls);
					uploadedFiles = docs;
				} catch {
					uploadedFiles = [];
				}
			}
		} catch (e: any) {
			// Profile doesn't exist yet, that's okay
			console.log('No existing profile');
		}
	}

	async function submitVerif() {
		if (!bio || !yearsOfExperience) {
			error = 'Please fill in all required fields';
			return;
		}

		isLoading = true;
		error = '';

		try {
			const documentUrls = JSON.stringify(uploadedFiles);
			// Get user_id from auth store or URL params
			const userId = authStore.user?.id || $page.url.searchParams.get('user_id');

			if (!userId) {
				error = 'User ID not found. Please log in or register again.';
				return;
			}

			await createOrUpdateTeacherProfile({
				bio,
				years_experience: parseInt(yearsOfExperience),
				document_urls: uploadedFiles.length > 0 ? documentUrls : undefined
			}, userId);
			showSuccess = true;
		} catch (e: any) {
			error = e.message || 'Failed to submit verification';
			console.error('Error submitting verification:', e);
		} finally {
			isLoading = false;
		}
	}

	async function handleFileUpload(event: Event) {
		const input = event.target as HTMLInputElement;
		if (input.files && input.files.length > 0) {
			isUploading = true;
			error = '';

			try {
				const file = input.files[0];
				const result = await uploadDocument(file);
				console.log('Upload result:', result); // Debug logging
				uploadedFiles = [...uploadedFiles, {
					name: result.filename,
					url: result.url
				}];
				console.log('Uploaded files:', uploadedFiles); // Debug logging
			} catch (e: any) {
				error = e.message || 'Failed to upload document';
				console.error('Error uploading file:', e);
			} finally {
				isUploading = false;
				// Reset input
				input.value = '';
			}
		}
	}

	function removeFile(index: number) {
		uploadedFiles = uploadedFiles.filter((_, i) => i !== index);
	}
</script>

<svelte:head>
	<title>Account Verification — EduLink SL</title>
</svelte:head>

<div class="verif-page-wrapper">
<div class="verif-wrap">
	{#if profile && profile.verification_status === 'APPROVED'}
		<div class="section-card" style="text-align:center;padding:40px">
			<div style="width:64px;height:64px;background:var(--green-lt);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:28px;color:var(--green)"><i class="ti ti-check"></i></div>
			<h2 style="font-size:20px;font-weight:800;margin-bottom:6px">Already Verified!</h2>
			<p style="font-size:14px;color:var(--muted-fg);margin-bottom:20px">Your account has been verified. You can now post classes.</p>
			<a href="/teacher/dashboard" class="btn btn-primary btn-full">Go to teacher dashboard &rarr;</a>
		</div>
	{:else if profile && profile.verification_status === 'REJECTED'}
		<div class="section-card" style="text-align:center;padding:40px;margin-bottom:16px">
			<div style="width:64px;height:64px;background:var(--red-lt);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:28px;color:var(--red)"><i class="ti ti-x"></i></div>
			<h2 style="font-size:20px;font-weight:800;margin-bottom:6px">Verification Rejected</h2>
			<p style="font-size:14px;color:var(--muted-fg);margin-bottom:20px">
				{#if profile.verification_note}
					Reason: {profile.verification_note}
				{:else}
					Your verification was rejected. Please update your documents and resubmit.
				{/if}
			</p>
		</div>
	{/if}

	{#if error}
		<div class="alert alert-error" style="margin-bottom:16px">
			<i class="ti ti-alert-circle"></i>
			{error}
		</div>
	{/if}

	<div class="verif-hero">
		<div class="verif-hero-icon"><i class="ti ti-shield-check"></i></div>
		<div>
			<div style="font-size:20px;font-weight:800;margin-bottom:4px">Verify your tutor account</div>
			<div style="font-size:14px;opacity:.8;line-height:1.6">Upload your identification and qualifications so our team can verify your account. This usually takes 1–2 business days. You cannot list classes until verification is approved.</div>
		</div>
	</div>

	<!-- Documents -->
	<div class="section-card" style="margin-bottom:16px">
		<div style="font-size:15px;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px">
			<span style="width:24px;height:24px;background:var(--saffron);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#fff">1</span>
			Documents
		</div>
		<div style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Upload your NIC, degree certificate, and other qualifications. PNG, JPG, or PDF, max 10MB each.</div>
		<div class="dropzone" style="margin-bottom:14px">
			<input type="file" multiple accept=".pdf,.jpg,.jpeg,.png" onchange={handleFileUpload} disabled={isUploading} style="display:none" id="fileInput">
			<label for="fileInput" class="dropzone-label" style={isUploading ? 'opacity:0.5;cursor:not-allowed' : ''}>
				{#if isUploading}
					<i class="ti ti-loader" style="font-size:36px;color:var(--saffron);display:block;margin-bottom:8px;animation:spin 1s linear infinite"></i>
					<div class="dropzone-txt"><strong>Uploading...</strong></div>
				{:else}
					<i class="ti ti-file-certificate" style="font-size:36px;color:var(--muted-fg);display:block;margin-bottom:8px"></i>
					<div class="dropzone-txt"><strong style="color:var(--saffron)">Click to upload</strong> or drag & drop files here</div>
					<div style="font-size:11px;color:var(--muted-fg);margin-top:4px">PDF, JPG, PNG — Max 10MB each</div>
				{/if}
			</label>
		</div>
		{#each uploadedFiles as file, index}
			<div class="file-item">
				<div class="fi-icon" style="background:#EFF6FF;color:#2563EB"><i class="ti ti-file"></i></div>
				<div class="fi-name">{file.name}</div>
				<i class="fi-remove ti ti-x" onclick={() => removeFile(index)}></i>
			</div>
		{/each}
	</div>

	<!-- Teaching info -->
	<div class="section-card" style="margin-bottom:16px">
		<div style="font-size:15px;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px">
			<span style="width:24px;height:24px;background:var(--saffron);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#fff">2</span>
			Teaching experience
		</div>
		<div style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Tell us about your experience. This will appear on your public profile.</div>
		<div class="form-group" style="margin-bottom:14px">
			<label class="form-label">Years of teaching experience</label>
			<input type="number" class="form-input" value={yearsOfExperience} oninput={(e) => yearsOfExperience = e.target.value} placeholder="e.g., 5" min="0" />
		</div>
		<div class="form-group">
			<label class="form-label">Short bio (shown on your profile)</label>
			<textarea class="form-input" rows="4" value={bio} oninput={(e) => bio = e.target.value} placeholder="Describe your teaching approach, specialisations, and what makes you a great tutor..."></textarea>
		</div>
	</div>

	<!-- Submit -->
	<div class="submit-section">
		<div class="alert alert-warning" style="margin-bottom:16px"><i class="ti ti-info-circle"></i> By submitting, you confirm all uploaded documents are genuine. Fraudulent submissions result in permanent account ban.</div>
		<div style="display:flex;gap:12px;align-items:center">
			<button class="btn btn-primary btn-lg" onclick={submitVerif} disabled={isLoading}>
				{#if isLoading}
					Processing...
				{:else}
					<i class="ti ti-send"></i> Submit for verification
				{/if}
			</button>
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
	.dropzone {
		border: 2px dashed var(--border-dk);
		border-radius: var(--r);
		padding: 24px;
		text-align: center;
		cursor: pointer;
		transition: all .2s;
		margin-bottom: 8px;
		background: #fff;
	}
	.dropzone-label {
		display: block;
		cursor: pointer;
	}
	.dropzone:hover {
		border-color: var(--saffron);
		background: var(--saffron-lt);
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
	.fi-remove {
		color: var(--muted-fg);
		cursor: pointer;
		font-size: 16px;
		transition: color .15s;
	}
	.fi-remove:hover {
		color: var(--red);
	}
	.submit-section {
		background: #fff;
		border-radius: var(--r-lg);
		border: 1px solid var(--border-dk);
		padding: 22px;
		margin-top: 20px;
	}
	@keyframes spin {
		from { transform: rotate(0deg); }
		to { transform: rotate(360deg); }
	}
</style>
