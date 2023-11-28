<template>
    <div class="row h-100 d-flex justify-content-center align-items-center">
        <form @submit.prevent="register" class="col-5">
            <h1 class="mb-3">CREATE AN ACCOUNT</h1>
            <input type="input" class="form-control mb-3" placeholder="Enter Username" required autofocus v-model="username">
            <input type="password" class="form-control mb-3" placeholder="Password" required v-model="password">
            <input type="password" class="form-control" placeholder="Repeat your password" required v-model="passwordRepeat">
            <button type="submit" class="btn btn-lg btn-primary col-12 mt-3">Register</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            password: '',
            passwordRepeat: ''
        }
    },
    methods: {
        register() {
            axios.post('http://localhost:5000/register', {
                'username': this.username,
                'password': this.password
            })
            .then((res) => {
                console.log(res.data)
                this.$emit('user-registered', res.data)
            })
            .catch((error) => {
                console.error(error);
            });
        }
    }
}
</script>

<style scoped>
</style>