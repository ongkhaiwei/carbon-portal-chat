
   
import { browser } from '$app/environment';
import { writable } from 'svelte/store';

const defaultTheme = 'white';
const initialThemeValue = browser
	? window.localStorage.getItem('theme') ?? defaultTheme
	: defaultTheme;
export const theme = writable(initialThemeValue);
theme.subscribe((value) => {
	if (browser) {
		window.localStorage.setItem('theme', value);
	}
});