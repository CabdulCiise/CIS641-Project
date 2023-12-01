<template>
    <Dialog 
        modal 
        v-model:visible="loginModalVisible"
        header="LOG IN"
        :closable="false"
        :draggable="true"
        >
        <div class="card flex justify-content-center">
            <form @submit.prevent="submitLogin" class="">
                <InputText type="input" class="" placeholder="Enter Username" autofocus v-model="username"></InputText>
                <InputText type="password" class="" placeholder="Password" v-model="password"></InputText>
                <Button type="submit" raised class="" label="Sign In"></Button>
                <div class="">Don't have an account? <a href="#" @click.prevent="onRegistering">Register</a></div>
            </form>
        </div>
    </Dialog>
    <Dialog 
        modal 
        v-model:visible="registerModalVisible"
        header="CREATE AN ACCOUNT"
        :closable="false"
        :draggable="true">
        <div class="row justify-content-center">
            <form @submit.prevent="register" class="col-7 mt-3">
                <InputText type="input" class="form-control mb-3 col-8" placeholder="Enter Username" required autofocus v-model="username"></InputText>
                <InputText type="password" class="form-control mb-3" placeholder="Password" required v-model="password"></InputText>
                <InputText type="password" class="form-control mb-3" placeholder="Repeat your password" required v-model="passwordRepeat"></InputText>
                <Button type="submit" class="btn btn-lg btn-primary col-12 mb-3">Register</Button>
            </form>
        </div>
    </Dialog>
</template>

<script>
import axios from 'axios'
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'

export default {
    props: {},
    components: {
        Dialog,
        InputText,
        Button
    },
    data() {
        return {
            loginModalVisible: true,
            registerModalVisible: false,
            username: '',
            password: '',
            passwordRepeat: '',
            loggedInUser: null,
            isRegistering: false
        }
    },
    methods: {
        submitLogin() {
            axios.post('http://localhost:5000/login', {
                'username': this.username,
                'password': this.password
            })
            .then((res) => {
                this.loggedInUser = res.data;
                this.$emit('logged-in', this.loggedInUser);
            })
            .catch((error) => {
                console.error(error);
            });
        },
        register() {
            if (this.password === this.passwordRepeat && this.password.length > 0) {
                axios.post('http://localhost:5000/register', {
                    'username': this.username,
                    'password': this.password
                })
                .then((res) => {
                    this.loggedInUser = res.data;
                    this.$emit('logged-in', this.loggedInUser);
                })
                .catch((error) => {
                    console.error(error);
                });
            }
        },
        onRegistering() {
            this.registerModalVisible = true;
            this.loginModalVisible = false;
        }
    }
}
</script>

<style scoped>
.p-dialog-content {
    width: 100%;
    height: 100%;
}
</style>