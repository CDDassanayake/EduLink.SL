<script lang="ts">
	import './layout.css';
	import { getAuthStore } from '$lib/stores/auth.svelte';

	let { children } = $props();

	const auth = getAuthStore();
</script>

<svelte:head>
	<link rel="icon" href="/favicon.svg" />
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css" />
</svelte:head>

{@render children()}
