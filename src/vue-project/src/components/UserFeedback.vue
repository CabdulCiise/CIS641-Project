<template>
    <Dialog 
        modal 
        v-model:visible="visible"
        header="USER FEEDBACK"
        :closable="true"
        :draggable="true"
        :style="{ width: '600px'}">
        <DataTable
            :value="userFeedbacks"
            paginator
            :rows="5"
            :rowsPerPageOptions="[5, 10, 20, 50]"
            >
            <Column field="username" header="Username" style="width: 10%"></Column>
            <Column field="date" header="Date" style="width: 10%"></Column>
            <Column field="feedback" header="Feedback" style="width: 80%"></Column>
        </DataTable>
    </Dialog>
</template>

<script>
import axios from 'axios'
import Dialog from 'primevue/dialog';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'

export default {
    props: {},
    components: {
        Dialog,
        DataTable,
        Column
    },
    data() {
        return {
            userFeedbacks: [],
            visible: true
        }
    },
    methods: {
        getUserFeedbacks() {
            axios.get('http://localhost:5000/user-feedback')
                .then((res) => {
                    this.userFeedbacks = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        archiveUserFeedback(user_feedback_id) {
            axios.put(`http://localhost:5000/user-feedback/archive?user_feedback_id=${user_feedback_id}`)
                .then((res) => {
                    this.getUserFeedbacks()
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    },
    created() {
        this.getUserFeedbacks();
    },
}
</script>

<style scoped>
</style>
