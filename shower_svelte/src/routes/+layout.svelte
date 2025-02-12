<script>
	import Navbar from '$lib/Navbar/Navbar.svelte'; //import the navbar
	let navIcons = [
		// WARNING: there should not be 2 of the same redirects
		{ redirect: '/', icon: '/timer.svg' },
		{ redirect: '/history', icon: '/history.svg' },
		{ redirect: '/settings', icon: '/settings.svg' }
	];
</script>

<slot />

<Navbar {navIcons} />

<style>
    :global(*) {
        overflow: hidden;
    }
	:global(:root) {
		--primary: 3, 52, 110;
		--second: 110, 172, 218;
		--bg: 2, 21, 38;
		--text: #e2e2b6;
	}
	:global(body) {
		background-color: rgb(var(--bg));
	}
	:global(h1) {
		color: var(--text);
	}
</style>
