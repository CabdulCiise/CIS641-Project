<template>
  <Login @logged-in="onLoggedIn" v-if="!loggedInUser"/>

	<div v-else class="home">
		<div class="home__sidebar">
            <Button icon="pi pi-comments"
			        v-tooltip="'Chat'"
			        @click="showChat = true"/>
			<Button icon="pi pi-thumbs-up"
			        v-tooltip="'User Feedback'"
			        @click="showUserFeedback = true"/>
			<Button icon="pi pi-file-edit"
			        v-tooltip="'Document Editor'"
			        @click="showDocumentEditor = true"/>
			<Button icon="pi pi-user"
			        v-tooltip="'Profile Editor'"
			        @click="showProfileEditor = true"/>
            <Button icon="pi pi-sign-out"
			        v-tooltip="'Logout'"
			        @click="onLoggedOut"/>
		</div>
		<div class="home__content">
			<div class="home__header">
				<label class="home__user">Hi there, {{ loggedInUser.username }}</label>
			</div>
			<div class="home__body">
				<UserFeedback v-if="showUserFeedback"/>
				<DocumentEditor v-if="showDocumentEditor"/>
				<ProfileEditor v-if="showProfileEditor" :logged-in-user="loggedInUser" />
				<Chat v-if="showChat" :logged-in-user="loggedInUser"/>
			</div>
		</div>
	</div>
</template>

<script>
import Login from '../components/Login.vue'
import Chat from '../components/Chat.vue'
import ProfileEditor from '../components/ProfileEditor.vue'
import UserFeedback from '../components/UserFeedback.vue'
import User from '../components/User.vue'
import DocumentEditor from '../components/DocumentEditor.vue'

import Button from 'primevue/button'

export default {
    props: {},
    components: {
        Login,
        Chat,
        ProfileEditor,
        UserFeedback,
        User,
        Button,
        DocumentEditor
    },
    data() {
        return {
            loggedInUser: null,
            showUserFeedback: false,
            showDocumentEditor: false,
            showProfileEditor: false,
            showChat: false,
            items: [
                {
                    separator: true
                },
                {
                    label: 'Documents',
                    items: [
                        {
                            label: 'New',
                            icon: 'pi pi-plus',
                            shortcut: '⌘+N'
                        },
                        {
                            label: 'Search',
                            icon: 'pi pi-search',
                            shortcut: '⌘+S'
                        }
                    ]
                },
                {
                    label: 'Profile',
                    items: [
                        {
                            label: 'Settings',
                            icon: 'pi pi-cog',
                            shortcut: '⌘+O'
                        },
                        {
                            label: 'Messages',
                            icon: 'pi pi-inbox',
                            badge: 2
                        },
                        {
                            label: 'Logout',
                            icon: 'pi pi-sign-out',
                            shortcut: '⌘+Q'
                        }
                    ]
                },
                {
                    separator: true
                }
            ]
        }
    },
    methods: {
        onLoggedIn(loggedInUser) {
            this.loggedInUser = loggedInUser;
            this.showChat = true;
        },
        onLoggedOut() {
            this.loggedInUser = null;
            this.hideAll();
        },
        hideAll() {
            this.showChat = false;
            this.showDocumentEditor = false;
            this.showProfileEditor = false;
            this.showUserFeedback = false;
        }
    },
    watch: {
        showProfileEditor() {
            if (this.showProfileEditor) {
                this.showDocumentEditor = false;
                this.showUserFeedback = false;
                this.showChat = false;
            }
        },
        showDocumentEditor() {
            if (this.showDocumentEditor) {
                this.showProfileEditor = false;
                this.showUserFeedback = false;
                this.showChat = false;
            }
        },
        showChat() {
            if (this.showChat) {
                this.showProfileEditor = false;
                this.showUserFeedback = false;
                this.showDocumentEditor = false;
            }
        },
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
		justify-content: end;
	}
	&__body {
		flex: 1;
		overflow: hidden;

	}
}
</style>
