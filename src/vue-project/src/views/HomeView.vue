<template>
    <Document />
    <!-- <Login @logged-in="onLoggedIn" v-if="!user"/> -->
    <!-- <Register @user-registered="onRegistered" v-else="true" /> -->
</template>

<script setup>
import { ref } from 'vue'

import Document from '../components/Document.vue'
// import Login from '../components/Login.vue'
// import Register from '../components/Register.vue';

const user = ref(null)

function onLoggedIn(newUser) {
    user = newUser
}

function onLoggedOut() {
    user = null
}

</script>

<style scoped>
</style>