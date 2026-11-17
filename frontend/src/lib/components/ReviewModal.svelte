<script lang="ts">
	import { createReview } from '$lib/api/reviews';
	import type { ReviewInput } from '$lib/schemas';

	let { bookingId, teacherName, onClose, onSuccess } = $props<{
		bookingId: string;
		teacherName: string;
		onClose: () => void;
		onSuccess: () => void;
	}>();

	let rating = $state(0);
	let comment = $state('');
	let isSubmitting = $state(false);
	let error = $state('');

	function setRating(value: number) {
		rating = value;
	}

	async function submitReview() {
		if (rating === 0) {
			error = 'Please select a rating';
			return;
		}

		isSubmitting = true;
		error = '';

		try {
			await createReview({
				booking_id: bookingId,
				rating,
				comment: comment || undefined
			});
			onSuccess();
			onClose();
		} catch (e: any) {
			error = e.message || 'Failed to submit review';
		} finally {
			isSubmitting = false;
		}
	}
</script>

<div class="modal-overlay" onclick={onClose}>
	<div class="modal-content" onclick={(e) => e.stopPropagation()}>
		<div class="modal-header">
			<div style="font-size: 18px; font-weight: 700">Leave a Review</div>
			<button class="btn btn-ghost btn-sm" onclick={onClose}><i class="ti ti-x"></i></button>
		</div>

		<div class="modal-body">
			<div style="margin-bottom: 16px;">
				<div style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">
					How was your session with {teacherName}?
				</div>
				<div class="star-rating">
					{#each [1, 2, 3, 4, 5] as star}
						<button 
							class="star" 
							class:active={star <= rating}
							onclick={() => setRating(star)}
						>
							<i class="ti ti-star"></i>
						</button>
					{/each}
				</div>
			</div>

			<div style="margin-bottom: 16px;">
				<div style="font-size: 13px; font-weight: 600; margin-bottom: 8px;">
					Additional comments (optional)
				</div>
				<textarea 
					class="review-textarea" 
					placeholder="Share your experience..."
					bind:value={comment}
					rows="4"
				></textarea>
			</div>

			{#if error}
				<div class="alert alert-danger" style="margin-bottom: 16px;">
					<i class="ti ti-alert-circle"></i> {error}
				</div>
			{/if}
		</div>

		<div class="modal-footer">
			<button class="btn btn-ghost" onclick={onClose}>Cancel</button>
			<button 
				class="btn btn-primary" 
				onclick={submitReview}
				disabled={isSubmitting || rating === 0}
			>
				{isSubmitting ? 'Submitting...' : 'Submit Review'}
			</button>
		</div>
	</div>
</div>

<style>
	.modal-overlay {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: rgba(0, 0, 0, 0.5);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 1000;
		padding: 20px;
	}

	.modal-content {
		background: white;
		border-radius: var(--r);
		max-width: 500px;
		width: 100%;
		max-height: 90vh;
		overflow-y: auto;
		box-shadow: var(--sh-lg);
	}

	.modal-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 20px;
		border-bottom: 1px solid var(--border);
	}

	.modal-body {
		padding: 20px;
	}

	.modal-footer {
		display: flex;
		gap: 12px;
		justify-content: flex-end;
		padding: 20px;
		border-top: 1px solid var(--border);
	}

	.star-rating {
		display: flex;
		gap: 8px;
	}

	.star {
		font-size: 28px;
		color: var(--border);
		background: none;
		border: none;
		cursor: pointer;
		padding: 0;
		transition: color 0.15s;
	}

	.star:hover {
		color: var(--saffron);
	}

	.star.active {
		color: var(--saffron);
	}

	.review-textarea {
		width: 100%;
		padding: 12px;
		border: 1.5px solid var(--border-dk);
		border-radius: var(--r-sm);
		font-family: var(--ff);
		font-size: 13px;
		resize: vertical;
		transition: border-color 0.15s;
	}

	.review-textarea:focus {
		outline: none;
		border-color: var(--saffron);
	}
</style>
