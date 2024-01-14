import { env } from '$env/dynamic/public';

const url = env.PUBLIC_URL.slice(-1) !== "/" ? env.PUBLIC_URL + "/" : env.PUBLIC_URL
console.log("PUBLIC_URL = " + url)

const headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
	'Access-Control-Allow-Origin': 'http://localhost:3000',
	'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
	'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token'
};

const sendMessage = async (message: string) => {
	console.log(message);
	const response = await fetch(url + "chat", {
		method: 'POST',
		headers: headers,
        body: JSON.stringify({
            message: message
        })
	});
	let result = "";
	// @ts-ignore
	const reader = response.body.pipeThrough(new TextDecoderStream()).getReader();
	return reader
    
};	

export {
    sendMessage,
};
