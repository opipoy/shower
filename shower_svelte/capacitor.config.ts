import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
	appId: 'com.shower.odh.app',
	appName: 'shower app',
	webDir: 'build',
	server: {
		allowNavigation: ['*'], // Allow all routes
		cleartext: true // For Android HTTP access
	},
    plugins: {
        CapacitorHttp: {
            enabled: true
        }
    }
};
export default config;
