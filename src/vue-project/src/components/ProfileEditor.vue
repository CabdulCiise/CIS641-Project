<template>
    <Dialog
        modal
        v-model:visible="visible"
        header="USER PROFILE"
        :closable="true"
        :draggable="true"
        :style="{ width: '600px'}">
	    <div class="profile-editor">
            <label>These instructions are fed into AI model</label>
            <span class="profile-editor__content">
                <TextArea v-model="customInstructions" autoResize rows="10" cols="60"></TextArea>
            </span>
            <Button label="Save Changes" @click="updateCustomInstructions"/>
	    </div>
    </Dialog>
</template>

<script>
import axios from 'axios';
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Dialog from 'primevue/dialog'
import TextArea from 'primevue/textarea'

export default {
    props: {
        loggedInUser: { name: 'logged-in-user', required: true }
    },
    components: {
        Button,
        InputText,
        TextArea,
        Dialog
    },
    data() {
        return {
            customInstructions: "",
            visible: true
        }
    },
    methods: {
        updateCustomInstructions() {
            axios.put(`http://localhost:5000/user/custom-instructions`, {
                'user_id': this.loggedInUser.user_id,
                'custom_instruction': this.customInstructions
            })
                .then((res) => {
                    this.customInstruction = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    },
    created() {
        this.customInstructions = this.loggedInUser.custom_instruction;
    }
}

</script>

<style lang="scss">
	.profile-editor {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		&__header {

		}
		&__content {
			textarea {
				width: 100%;
			}
		}
	}
</style>
