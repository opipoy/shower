<script>
	import { Preferences } from '@capacitor/preferences';

	async function set_base_url(url) {
		let the_url = url.target.value;
		await Preferences.set({ key: 'base_url', value: the_url });
	}
	async function set_username(username) {
		let the_username = username.target.value;
		await Preferences.set({ key: 'username', value: the_username });
        console.warn(await Preferences.get({key:"username"}))
	}
</script>

<div>
	<h3>Base Url</h3>
	<input type="text" placeholder="eg. 127.0.0.1:5000" on:change={set_base_url} />
	<h3>username</h3>
	<input type="text" placeholder="eg. Opipoy" on:change={set_username} defaultvalue="" />
</div>
