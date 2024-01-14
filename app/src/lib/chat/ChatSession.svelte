<script lang="ts">
	import ChatBox from "./ChatBox.svelte";
	import ChatInput from "./ChatInput.svelte";
	import { sendMessage } from "$lib/services/watsonx";

	export let disabled = false;
	let current: any[] = [];
	let generatedOutput: string = "";

	const onSubmit = async (event: { detail: { message: any } }) => {
		const message = event.detail.message;

		const _data = {
			text: message,
			who: "you",
		};
		current.push(_data);

		const _watsonx_data = {
			text: "Sending to watsonx ...",
			who: "watsonx",
		};
		current.push(_watsonx_data);
		current = current;

		const response = await sendMessage(message);
		let result = "";
		while (true) {
			const { value, done } = await response.read();
			//console.log("resp", done, value);
			if (done) {
				let d = current[current.length - 1];
				d.text = d.text.slice(0, -1);
				current[current.length - 1] = d;
				current = current;
				break;
			}
			result += `${value}`;
			//console.log(result)
			generatedOutput = result + "_";
			let d = current[current.length - 1];
			d.text = generatedOutput;
			current[current.length - 1] = d;
			current = current;
		}
	};

	$: {
	}

	let message = "";
</script>

{#each current as { text, who }}
	<ChatBox {who} {text} />
{/each}
{#if !disabled}
	<ChatInput on:submit={onSubmit} bind:message />
{/if}
