<script>
	import { Label, Input, GradientButton } from 'flowbite-svelte';
	import axios from 'axios';

	let reviewText = '';
	let evaluation = '';

	const api = axios.create({
		baseURL: 'http://127.0.0.1:8000',
		headers: {
			'Content-Type': 'application/json'
		},
		timeout: 5000
	});

	async function handleSubmit() {
		console.log('Review:', reviewText);
		try {
			const response = await api.post('/api/review', {
				text: reviewText
			});
			evaluation = response.data.evaluation;
			console.log('Server replied:', response.data);
		} catch (err) {
			console.error('Error while sending review:', err);
		}
	}
</script>

<div class="h-screen bg-gray-800 p-8">
	<h1 class="text-3xl font-bold text-white">⭐ The Review Reviewer App</h1>
	<div class="flex h-6/12 items-center justify-center">
		<div class="w-6/12 space-y-4">
			<Label for="large-input" class="mb-2 block text-xl text-white">Paste review here</Label>
            <div class="flex gap-2">
                <Input id="large-input" size="lg" placeholder="Review" bind:value={reviewText} />
                <GradientButton color="pinkToOrange" onclick={handleSubmit} pill={false}>Submit</GradientButton>
            </div>
			<p class="mt-4 text-2xl text-white">
				Sentiment: <strong>{evaluation}</strong>
                {#if evaluation === "POSITIVE"}
                    👍
                {/if}
                {#if evaluation === "NEGATIVE"}
                    👎
                {/if}
			</p>
		</div>
	</div>
</div>
