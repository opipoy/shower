<script>
	import NavIcon from './NavIcon.svelte';
	import { goto } from '$app/navigation';
	let { navIcons } = $props();
	async function onNavClick(input) {
		// Navigate to the new page
		await goto(input);
	}

	let activeIcon = $state();
</script>

<div class="navbar" id="navbar">
	{#each navIcons as item}
		<NavIcon
			redirect={item.redirect}
			icon_path={item.icon}
			onclick={() => onNavClick(item.redirect)}
		/>
	{/each}
</div>

<style>
	.navbar {
		/*bg color*/
		background-color: rgba(var(--primary), 0.3);
		/*size*/
		width: 80%;
		height: 75px;
		/*padding*/
		padding: 0;
		padding-left: 10px;
		padding-right: 10px;
		/*behavior on screen*/
		display: flex;
		justify-content: space-around;
		align-items: center;
		/*position*/
		position: fixed;
		left: 50%;
		transform: translateX(-50%);
		bottom: 3%;
		/*borders*/
		border: 0px;
		border-radius: 10px;
	}
</style>
