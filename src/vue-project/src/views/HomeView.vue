<template>
	<Login @logged-in="onLoggedIn" v-if="!loggedInUser"/>

	<div v-else class="home">
		<div class="home__sidebar">
			<Button icon="pi pi-comments"
					v-if="isAdmin"
			        v-tooltip="'Chat'"
			        @click="showChat = true"/>
			<Button icon="pi pi-file-edit"
					v-if="isAdmin"
			        v-tooltip="'Document Editor'"
			        @click="showDocumentEditor = true"/>
			<Button icon="pi pi-users"
					v-if="isAdmin"
			        v-tooltip="'Users'"
			        @click="showUsers = true"/>
			<Button icon="pi pi-check"
					v-if="isAdmin"
			        v-tooltip="'Review Feedback'"
			        @click="showUserFeedback = true"/>
		</div>
		<div class="home__content">
			<div class="home__header">
				<label class="home__welcome">PDF Query Tool</label>
				<div class="home__profile">
					<label class="home__user">Hi there, {{ loggedInUser.username }}</label>
					<Button icon="pi pi-user" text type="button" @click="toggleMenu"
					        aria-haspopup="true" aria-controls="overlay_menu"/>
					<Menu ref="menu" id="overlay_menu" :model="items" :popup="true"/>
				</div>
			</div>
			<div class="home__body">
				<ProfileEditor v-if="showProfileEditor" :logged-in-user="loggedInUser"/>
				<User v-if="showUsers"/>
				<UserFeedback v-if="showUserFeedback"/>
				<DocumentEditor v-if="showDocumentEditor"/>
				<Chat v-if="showChat" :logged-in-user="loggedInUser"/>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'

import Login from '../components/Login.vue'
import Chat from '../components/Chat.vue'
import ProfileEditor from '../components/ProfileEditor.vue'
import UserFeedback from '../components/UserFeedback.vue'
import User from '../components/User.vue'
import DocumentEditor from '../components/DocumentEditor.vue'
import Button from 'primevue/button'
import Menu from 'primevue/menu'
import {PrimeIcons} from 'primevue/api';
import { nextTick } from 'vue'

export default {
	props: {},
	components: {
		Login,
		Chat,
		ProfileEditor,
		UserFeedback,
		User,
		DocumentEditor,
		Button,
		Menu
	},
	data() {
		return {
			loggedInUser: null,
			showProfileEditor: false,
			showUserFeedback: false,
			showDocumentEditor: false,
			showChat: false,
			showUsers: false,
			adminRoleId: null,
			items: [
				{
					label: 'Options',
					items: [
						{
							label: 'Profile',
							icon: PrimeIcons.USER_EDIT,
                            command: () => this.onShowProfileEditor()

						},
						{
							label: 'Logout',
							icon: PrimeIcons.SIGN_OUT,
                            command: () => this.onLoggedOut()
						}
					]
				}
			]
		}
	},
	methods: {
		onLoggedIn(loggedInUser) {
			this.loggedInUser = loggedInUser;
            this.hideAll();
			this.showChat = true;
		},
		onLoggedOut() {
			this.loggedInUser = null;
			this.hideAll();
		},
        async onShowProfileEditor() {
            this.showProfileEditor = false;
            await nextTick();
            this.showProfileEditor = true;
        },
		hideAll() {
			this.showChat = false;
			this.showDocumentEditor = false;
			this.showUserFeedback = false;
		},
		toggleMenu(event) {
			this.$refs.menu.toggle(event);
		},
		getRoles() {
			axios.get('http://localhost:5000/role')
			.then((res) => {
				const adminRoles = res.data.filter(role => role.name === "admin");
				this.adminRoleId = adminRoles.length > 0 ? adminRoles[0].role_id : null;
			})
			.catch((error) => {
				console.error(error);
			});
		},
	},
	watch: {
		showDocumentEditor() {
			if (this.showDocumentEditor) {
				this.showUserFeedback = false;
				this.showChat = false;
				this.showUsers = false;
			}
		},
		showChat() {
			if (this.showChat) {
				this.showUserFeedback = false;
				this.showDocumentEditor = false;
				this.showUsers = false;
			}
		},
		showUsers() {
			if (this.showUsers) {
				this.showUserFeedback = false;
				this.showDocumentEditor = false;
				this.showChat = false;
			}
		},
		showUserFeedback() {
			if (this.showUserFeedback) {
				this.showUsers = false;
				this.showDocumentEditor = false;
				this.showChat = false;
			}
		}
	},
	computed: {
		isAdmin() {
			if (this.loggedInUser != null && this.adminRoleId === this.loggedInUser.user_role_id) {
				return true;
			}
			else {
				return false;
			}
		}
	},
	created() {
		this.getRoles();
	}
}
</script>

<style lang="scss">
.home {
	display: flex;
	height: 100vh;

	&__sidebar {
		background: $sidebar;
		border-right: 1px solid $border;
		display: flex;
		justify-content: end;
		flex-direction: column;
		gap: 1rem;
		padding: 1rem;
	}

	&__content {
		flex: 1;
		display: flex;
		flex-direction: column;
	}

	&__header {
		padding: 1rem;
		border-bottom: 1px solid $border;
		display: flex;
		width: 100%;
		justify-content: space-between;
	}
	&__welcome {
		flex: 1;
		line-height: 0;
		margin: auto 0;
	}
	&__profile {
		display: flex;
		gap: 1rem;

	}
	&__user {
		line-height: 0;
		margin: auto 0;
	}

	&__body {
		flex: 1;
		overflow: hidden;
	}
}
</style>
