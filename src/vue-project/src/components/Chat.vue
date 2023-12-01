<template>
	<div class="chat">
		<div class="chat__content">
			<div class="chat__inner">
				<div class="chat__messages">
					<template v-for="message in messages">
						<div class="chat__bubble">
							<label class="chat__query">{{ message.query }}</label>
						</div>
						<div v-if="message.response" class="chat__bubble">
							<label class="chat__response">{{ message.response }}</label>
						</div>
					</template>
				</div>
			</div>
			<div class="chat__bar">
				<span class="chat__input p-input-icon-right">
					<InputText v-model="query"
							placeholder="What do you want to ask?"
							type="input"
							@keydown.enter="onNewQuery"/>
					<i class="pi pi-arrow-circle-up"></i>
				</span>
				<Button icon="pi pi-refresh"
						text
						v-tooltip.top="'Reset'"
						@click=""/>

			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'

export default {
	props: {
		loggedInUser: { name: 'logged-in-user', required: true}
	},
	components: {
		Button,
		InputText
	},
	data() {
		return {
			isHandlingAQuery: false,
			query: "",
			messages: []
		}
	},
	methods: {
		onNewQuery() {
			if (!this.isHandlingAQuery) {
				this.isHandlingAQuery = true;

				let currentQuery = this.query;
				this.query = null;

				this.messages.push({
					query: currentQuery,
					response: null
				});

				this.getResponse(currentQuery);
			}
		},
		getResponse(currentQuery) {
			axios.post(`http://localhost:5000/chat?user_id=${this.loggedInUser.user_id}`, {
				'query': currentQuery
			})
				.then((res) => {
					this.messages[this.messages.length - 1].response = res.data;
					this.isHandlingAQuery = false;
				})
				.catch((error) => {
					console.error(error);
					this.isHandlingAQuery = false;
				});
		}
	}
}
</script>

<style lang="scss">
.chat {
	display: flex;
	flex-direction: column;
	height: 100%;
	&__content {
		padding: 1rem;
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}
	&__inner {
		height: 100%;
		position: relative;
	}
	&__bar {
		padding-top: 1rem;
		border-top: 1px solid $border;
		display: flex;
		gap: 1rem;
	}
	&__input {
		flex: 1;
		width: 100%;
		input {
			width: 100%;
		}
	}
	&__messages {
		position: absolute;
		left: 0;
		top: 0;
		right: 0;
		bottom: 0;
		display: flex;
		flex-direction: column;
		flex: 1;
		gap: 1rem;
		overflow-x: hidden;
		overflow-y: auto;
	}
	&__bubble {
		padding: 0 1rem;
	}
	&__query,
	&__response {
		max-width: 75%;
		position: relative;
		padding: .625rem .875rem;
		border-radius: 1.5rem;
		&:before,
		&:after {
			content: "";
			position: absolute;
			height: 1.25rem;
		}
		&:before {
			bottom: -.125rem;
			transform: translate(0, -.125rem);

		}
		&:after {
			bottom: -.125rem;
			transform: translate(-1.875rem, -.125rem);
			background: $background;
		}
	}
	&__response {
		color: $queryBubbleText;
		background: $queryBubbleBg;
		float: right;
		&:before {
			right: -.5rem;
			border-right: 1.25rem solid $queryBubbleBg;
			border-bottom-left-radius: .625rem;
		}
		&:after {
			right: -3.5rem;
			width: 1.625rem;
			border-bottom-left-radius: .625rem;
		}
	}

	&__query {
		color: $responseBubbleText;
		background: $responseBubbleBg;
		float: left;
		&:before {
			left: -.5rem;
			border-left: 20px solid $responseBubbleBg;
			border-bottom-right-radius: .625rem;
		}
		&:after {
			left: 4px;
			width: 26px;
			border-bottom-right-radius: .625rem;
		}
	}
}
</style>
