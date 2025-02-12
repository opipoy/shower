<script>
	import { CapacitorHttp } from '@capacitor/core';
	import { Preferences } from '@capacitor/preferences';
	import { scale } from 'svelte/transition';
	let moved = $state(false);
	let sec = $state(0);
	let time = $derived(Math.floor(sec / 3600) + ':' + Math.floor(sec / 60) + ':' + sec%60);
	let timer;

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

		if (moved) {
			setTimeout(() => {
				let video = document.getElementById('splash-animation');
				video.style.visibility = 'visible';
			}, 400);
			setTimeout(() => {
				let video = document.getElementById('splash-animation');
				video.style.visibility = 'hidden';
			}, 1650);
			sec = 0;
			timer = setInterval(() => (sec += 1), 1000);
		} else {
			clearInterval(timer);
			sec = 0;
		}
		let nav = document.getElementById('navbar');
		nav.style.visibility = moved ? 'hidden' : 'visible';
	};
</script>

<div id="button-div">
	{#if moved}
		<h1>{time}</h1>
	{/if}
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

<style>
	#splash-animation {
		position: absolute;
		z-index: 3;
		pointer-events: none;
		bottom: 0%;
		left: 50%;
		transform: translate(-55%, 25%);
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
	#button-div h1 {
		font-size: 30vw;
		font-weight: bold;
		margin: 0;
	}
	.moved {
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
