/**
 * Date formatting utilities
 */

export function formatDate(date: string | Date): string {
	const d = typeof date === 'string' ? new Date(date) : date;
	return d.toLocaleDateString('en-GB', {
		day: '2-digit',
		month: 'short',
		year: 'numeric'
	});
}

export function formatDateTime(date: string | Date): string {
	const d = typeof date === 'string' ? new Date(date) : date;
	return d.toLocaleString('en-GB', {
		day: '2-digit',
		month: 'short',
		year: 'numeric',
		hour: '2-digit',
		minute: '2-digit'
	});
}

export function formatTime(date: string | Date): string {
	const d = typeof date === 'string' ? new Date(date) : date;
	return d.toLocaleTimeString('en-GB', {
		hour: '2-digit',
		minute: '2-digit'
	});
}

export function formatRelativeTime(date: string | Date): string {
	const d = typeof date === 'string' ? new Date(date) : date;
	const now = new Date();
	const diffMs = now.getTime() - d.getTime();
	const diffMins = Math.floor(diffMs / 60000);
	const diffHours = Math.floor(diffMs / 3600000);
	const diffDays = Math.floor(diffMs / 86400000);

	if (diffMins < 1) return 'Just now';
	if (diffMins < 60) return `${diffMins}m ago`;
	if (diffHours < 24) return `${diffHours}h ago`;
	if (diffDays < 7) return `${diffDays}d ago`;
	return formatDate(d);
}

export function isToday(date: string | Date): boolean {
	const d = typeof date === 'string' ? new Date(date) : date;
	const today = new Date();
	return d.toDateString() === today.toDateString();
}

export function isTomorrow(date: string | Date): boolean {
	const d = typeof date === 'string' ? new Date(date) : date;
	const tomorrow = new Date();
	tomorrow.setDate(tomorrow.getDate() + 1);
	return d.toDateString() === tomorrow.toDateString();
}

export function getDayOfWeek(date: string | Date): string {
	const d = typeof date === 'string' ? new Date(date) : date;
	return d.toLocaleDateString('en-GB', { weekday: 'long' });
}

export function addDays(date: string | Date, days: number): Date {
	const d = typeof date === 'string' ? new Date(date) : date;
	const result = new Date(d);
	result.setDate(result.getDate() + days);
	return result;
}

export function addHours(date: string | Date, hours: number): Date {
	const d = typeof date === 'string' ? new Date(date) : date;
	const result = new Date(d);
	result.setHours(result.getHours() + hours);
	return result;
}
