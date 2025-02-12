<script>
	import { scale } from 'svelte/transition';
	import { afterNavigate } from '$app/navigation';
	import { page } from '$app/stores';
	let { redirect, icon_path, onclick } = $props();
</script>

<button {onclick}>
	<img src={icon_path} alt="Navbar icon: {icon_path}" />
	{#if $page.url.pathname == redirect}
		<div transition:scale={{ duration: 100 }} class="navbarActive"></div>
	{/if}
</button>

<style>
	* {
		padding: 0;
		margin: 0;
	}
	.navbarActive {
		width: 100%;
		height: 10px;
		background-color: rgba(var(--second), 0.3);
		opacity: 40%;
		border: 0px;
		border-radius: 1em;
	}
	button {
		background: transparent;
		border: none !important;
	}
	img {
		width: 40px;
		height: 40px;
	}
</style>
