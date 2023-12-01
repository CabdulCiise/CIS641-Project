<template>
    <Login @logged-in="onLoggedIn" v-if="!loggedInUser"/>
    <div v-else>
        <div>
            <Button @click="showUserFeedback = true">User Feedback</Button>
            <Button @click="showDocumentEditor = true">Document Editor</Button>
        </div>
        <!-- <UserFeedback v-if="showUserFeedback"/> -->
        <!-- <DocumentEditor v-if="showDocumentEditor"/> -->
        <Chat :logged-in-user="loggedInUser"/>
    </div>
</template>

<script>
import Login from '../components/Login.vue'
import Chat from '../components/Chat.vue'
import UserFeedback from '../components/UserFeedback.vue'
import User from '../components/User.vue'
import DocumentEditor from '../components/DocumentEditor.vue'

import Button from 'primevue/button'
import Menu from 'primevue/menu'
import Toolbar from 'primevue/toolbar'
import Avatar from 'primevue/toolbar'

export default {
    props: {},
    components: {
    Login,
    Chat,
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
            this.loggedInUser = loggedInUser
        },
        onLoggedOut() {
            user = null
        }
    }
}
</script>

<style scoped>
</style>