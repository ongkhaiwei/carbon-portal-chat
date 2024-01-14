import { ADMIN_LOGIN } from '$env/static/private';

// @ts-ignore
export const handle = async ({ event, resolve }) => {
	// @ts-ignore
	const url = new URL(event.request.url);

	const auth = event.request.headers.get('Authorization');

	// @ts-ignore
	if (auth !== `Basic ${btoa(ADMIN_LOGIN)}`) {
		return new Response('Not authorized', {
			status: 401,
			headers: {
				'WWW-Authenticate': 'Basic realm="User Visible Realm", charset="UTF-8"'
			}
		});
	}

	return resolve(event);
};
