<script>
	import { onMount } from 'svelte';
	let wave_number = 3;

	onMount(() => {
		let waves_wrapper = document.getElementById('waves-wrapper');
		const interval = setInterval(() => {
			let wave = document.createElement('img');
			wave.src = '/wave.svg';
			wave.alt = 'wave';
			wave.className = 'wave';
			waves_wrapper.appendChild(wave);
            wave.style.position = 'absolute';
				wave.style.transform = 'translateX(100vw)';
			setTimeout(() => {
				wave.style.transform = 'translateX(-100vw)';
			}, 10);
			setTimeout(() => waves_wrapper.removeChild(wave), 4000);
		}, 700);
		let waves = document.querySelectorAll('.wave');
	});
</script>

<div id="waves-wrapper"></div>

<style>
	:global(.wave) {
        position: absolute;
		transition: linear transform 4s;
	}
	#waves-wrapper {
        display: flex;
		overflow: visible;
	}
</style>
