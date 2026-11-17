/**
 * Currency formatting utilities for Sri Lankan Rupee (LKR)
 */

export function formatLKR(amount: number): string {
	return new Intl.NumberFormat('en-LK', {
		style: 'currency',
		currency: 'LKR',
		minimumFractionDigits: 0,
		maximumFractionDigits: 0
	}).format(amount);
}

export function formatLKRWithDecimals(amount: number, decimals: number = 2): string {
	return new Intl.NumberFormat('en-LK', {
		style: 'currency',
		currency: 'LKR',
		minimumFractionDigits: decimals,
		maximumFractionDigits: decimals
	}).format(amount);
}

export function formatLKRCompact(amount: number): string {
	if (amount >= 1000000) {
		return `LKR ${(amount / 1000000).toFixed(1)}M`;
	}
	if (amount >= 1000) {
		return `LKR ${(amount / 1000).toFixed(1)}K`;
	}
	return formatLKR(amount);
}

export function parseLKR(formatted: string): number {
	// Remove currency symbol and commas, then parse
	const cleaned = formatted.replace(/[^\d.-]/g, '');
	return parseFloat(cleaned);
}

export function calculateDiscount(originalPrice: number, discountPercent: number): number {
	return originalPrice * (1 - discountPercent / 100);
}

export function calculatePlatformFee(amount: number, feePercent: number = 10): number {
	return amount * (feePercent / 100);
}

export function calculateTeacherPayout(amount: number, platformFeePercent: number = 10): number {
	return amount * (1 - platformFeePercent / 100);
}
