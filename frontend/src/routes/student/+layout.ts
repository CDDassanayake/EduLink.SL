import { redirect } from '@sveltejs/kit';

export async function load() {
	// TODO: Implement proper auth check
	// For now, just allow access for demo purposes
	// In production, check auth store and redirect if not student
	
	// const auth = getAuthStore();
	// if (!auth.user || auth.user.role !== 'STUDENT') {
	//   throw redirect(302, '/auth/login');
	// }
	
	return {};
}
