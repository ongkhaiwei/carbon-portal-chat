<script>
	import { onMount } from "svelte";
	import { User, Watson } from "carbon-icons-svelte";

	import { Grid, Row, Column } from "carbon-components-svelte";

	export let who = "you";
	export let text = "";

	onMount(() => {
		setTimeout(() => {
			window.scrollTo({
				top: document.documentElement.scrollHeight,
				behavior: "smooth",
			});
		}, 0);
	});
</script>

<Grid fullWidth padding>
	<Row>
		<Column sm={1} md={1} lg={1}>
			{#if who === "watsonx"}
				<Watson size={32} />
			{/if}
			{#if who === "you"}
				<User size={32} />
			{/if}
		</Column>

		<Column sm={1} md={4} lg={8}>
			<h4>{text}</h4>
		</Column>
	</Row>
</Grid>
