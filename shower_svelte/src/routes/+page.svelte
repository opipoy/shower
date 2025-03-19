<script>
	import { CapacitorHttp } from '@capacitor/core';
	import { Preferences } from '@capacitor/preferences';
	import { scale } from 'svelte/transition';
    import MovingWaves from "$lib/waves/MovingWaves.svelte"
	let moved = $state(false);
	let timeC = $state();
	let sec = $state(0);
	let timer;
	let move = $props();

	function start_counting() {
		sec = 0;
		timer = setInterval(() => (sec += 1), 1000);
	}
	function stop_counting() {
		sec = 0;
		timer = clearInterval(timer);
	}

	let move_button = async () => {
		try {
			const url = await Preferences.get({ key: 'base_url' });
			const username = await Preferences.get({ key: 'username' });

			const options = { url: url.value + '/add_time_usr/' + username.value };
			const response = await CapacitorHttp.post(options);

			// let i =await fetch("http://google.com");
			// alert(JSON.stringify(i))
		} catch (error) {
			alert(error);
		}
		moved = !moved;
		let nav = document.getElementById('navbar');
		nav.style.visibility = moved ? 'hidden' : 'visible';

		if (moved) {
			setTimeout(() => {
				let video = document.getElementById('splash-animation');
				video.style.visibility = 'visible';
			}, 400);
			setTimeout(() => {
				let video = document.getElementById('splash-animation');
				video.style.visibility = 'hidden';
				start_counting();
			}, 1650);
		} else {
			stop_counting();
		}
	};
</script>

<div id="button-div">
	<div id="time" class={moved ? 'moved' : ''}>
		<h1 id="hours">{((sec / 3600) % 60 < 10 ? '0' : '') + (Math.floor(sec / 3600) % 60)}</h1>
		<h1>:</h1>
		<h1 id="mins">{((sec / 60) % 60 < 10 ? '0' : '') + (Math.floor(sec / 60) % 60)}</h1>
		<h1>:</h1>
		<h1 id="seconds">{(sec % 60 < 10 ? '0' : '') + (Math.floor(sec) % 60)}</h1>
	</div>

	<style>
		@font-face {
			font-family: 'Wendy One';
			src: url(/WendyOne-Regular.ttf);
		}
		#time h1 {
			text-transform: none;
			line-break: auto;
			overflow-wrap: initial;
			white-space: pre;
			font-size: 80px;
			text-rendering: geometricPrecision;
			text-decoration: none;
			letter-spacing: 0px;
			font-family: 'Wendy One';
			font-style: normal;
			font-weight: 20vw;
			position: relative;
			transition: transform 2s cubic-bezier(0.65, 0.27, 0, 1.03);
			padding: 0px;
			margin: 0px;
		}
		#time {
			display: flex;
			overflow: visible;
			align-items: start;
		}
	</style>

	<button class={moved ? 'moved' : ''} onclick={move_button}>
		{#if moved}
			<img src="./stop.svg" alt="stop img" />
		{:else}
			<img src="./bathtub.svg" alt="shower img" />
		{/if}
	</button>
</div>

{#if moved}
	<div id="play-div" in:scale={{ delay: 300, duration: 200 }}>
		<div>
			<img src="./list.svg" alt="list img" />
		</div>
		<div>
			<img src="./pause.svg" alt="pause img" />
		</div>
	</div>
	<video width="320" height="240" autoplay muted id="splash-animation">
		<source src="/splash-updated.webm" type="video/webm" />
	</video>
{/if}
<div id="water-holder" class={moved ? 'moved' : ''}>
    <MovingWaves/>
	<div id="water"></div>
</div>

<style>
	#splash-animation {
		position: absolute;
		z-index: 3;
		pointer-events: none;
		bottom: 0%;
		left: 50%;
		transform: translate(-55%, 30%);
		width: 200px;
		height: 200px;
		margin: 0;
		visibility: hidden;
	}
	#button-div {
		display: grid;
		justify-content: space-around;
		place-items: center;
		height: 100vh;
	}
	#time {
		z-index: -1;
		visibility: hidden;
		overflow: visible;
	}
	#time.moved {
		z-index: 0;
		visibility: visible;
	}
	#time.moved #hours {
		transform: translateY(15vh) rotateZ(30deg);
	}
	#time.moved #mins {
		transition-delay: 1s;
		transform: translateY(-5vh) scale(110%);
	}
	#time.moved #seconds {
		transition-delay: 1.5s;
		transform: translateY(-20vh) rotateZ(-30deg) scale(120%);
	}
	#water-holder {
        position: absolute;
        visibility: hidden;
        overflow: visible;
        width: 100%;
        height: 0px;
		bottom: 0px;
        left: 50%;
        transform: translateX(-50%);
        transition: height 3s ease-out;
        z-index: -4;
	}
	#water-holder.moved {
		visibility: visible;
        height: 100vh;
	}
    #water {
        position: absolute;
        width: 100%;
        height: 90%;
        bottom: 0;
        background-color: #0178C9;
    }

	button.moved {
		transform: translateY(40vh) scale(30%);
	}
	#button-div button {
		position: absolute;
		transition: transform 600ms cubic-bezier(1, -0.3, 0.265, 2);
		border: 0px;
		border-radius: 50%;
		background-color: rgb(var(--second));
		height: 40%;
		aspect-ratio: 1;
	}
	#play-div {
		z-index: -1;
		/*bg color*/
		background-color: rgba(var(--primary), 0.5);
		/*size*/
		width: 80%;
		height: 50px;
		/*padding*/
		padding: 0;
		padding-left: 20px;
		padding-right: 20px;
		/*behavior on screen*/
		display: flex;
		align-items: stretch;
		justify-content: space-between;
		/*position*/
		position: fixed;
		left: 50%;
		transform: translateX(-50%);
		bottom: 6.5%;
		/*borders*/
		border: 0px;
		border-radius: 25px;
	}
	#play-div div {
		display: flex;
		align-items: stretch;
	}
	#play-div div img {
		width: 45px;
		height: 45px;
	}
	img {
		width: 60%;
		aspect-ratio: 1;
	}
</style>
