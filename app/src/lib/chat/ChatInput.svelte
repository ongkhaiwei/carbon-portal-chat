<script>
	import { createEventDispatcher } from "svelte";
	import {
		Button,
		TextInput,
		Grid,
		Row,
		Column,
	} from "carbon-components-svelte";
	import Send from "carbon-icons-svelte/lib/Send.svelte";

	const dispatch = createEventDispatcher();

	export let message = "";

	function focusInput() {
		const messageInput = document.getElementById("message-input");
		if (messageInput) {
			messageInput.focus();
		}
	}

	const onSubmit = (/** @type {{ preventDefault: () => void; }} */ e) => {
		e.preventDefault();
		dispatch("submit", {
			message: message,
		});
		message = "";
		focusInput();
	};
</script>

<form on:submit={onSubmit}>
	<Grid fullWidth>
		<Row>
			<Column sm={1} md={4} lg={8}>
				<TextInput
					id="message-input"
					bind:value={message}
					placeholder="Send a message"
				/>
			</Column>
			<Column sm={1} md={1} lg={1}>
				<Button
					type="submit"
					size="small"
					kind="primary"
					iconDescription="Send"
					icon={Send}
				/>
			</Column>
		</Row>
	</Grid>
</form>
