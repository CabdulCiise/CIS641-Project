<template>
    <p>Hi there, {{ loggedInUser.username }}</p>
    <div v-for="message in messages">
            <p>{{ message.query }}</p>
            <p v-if="message.response">{{ message.response }}</p>
    </div>
    <span class="p-input-icon-right">
        <i class="pi pi-arrow-circle-up"></i>
        <InputText v-model="query" placeholder="What do you want to ask?" type="input" @keydown.enter="onNewQuery" :disabled="isDisabled" />
    </span>
</template>

<script>
import axios from 'axios'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'

export default {
    props: {
        loggedInUser: { name: 'logged-in-user', required: true }
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

<style scoped>
</style>