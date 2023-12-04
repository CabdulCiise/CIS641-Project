<template>
	<div class="document-editor">
		<div class="document-editor__panel">
			<h3 class="document-editor__heading">Upload New Documents</h3>
			<div class="document-editor__content">
				<div class="document-editor__wrapper">
					<FileUpload
						@select="onFilesUpload"
						:auto="true"
						accept=".pdf"
						:showCancelButton="false"
						:showUploadButton="false"
						:maxFileSize="1000000"
					>
					</FileUpload>
				</div>
			</div>
		</div>
		<div class="document-editor__panel">
			<h3 class="document-editor__heading">Delete Documents</h3>
			<div class="document-editor__content">
				<DataTable
					:value="documents"
					paginator
					scrollable
					scroll-height="flex"
					:rows="5"
					:rowsPerPageOptions="[5, 10, 20, 50]"
				>
					<Column field="created_date" sortable  header="Date" style="width: 20%">
						<template #body="{ data }">{{ dateFormat(data.created_date) }}</template>
					</Column>
					<Column field="name" sortable header="File Name" style="width: 30%"></Column>
					<Column field="" header="Delete" style="width: 20%">
						<template #body="{ data }">
							<Button type="submit" @click="deleteDocument(data.uploaded_doc_id, data.name)" severity="danger" label="Delete"/>
						</template>
					</Column>
				</DataTable>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

import FileUpload from 'primevue/fileupload';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import Badge from 'primevue/badge';
import ProgressBar from 'primevue/progressbar';

import { showNotification } from '../services/notification'

export default {
    props: {
		loggedInUser: { name: 'logged-in-user', required: true}
    },
    components: {
        FileUpload,
        DataTable,
        Column,
        Button,
        Badge,
        ProgressBar
    },
    data() {
        return {
            documents: []
        }
    },
    methods: {
        getUploadedDocuments() {
            axios.get('http://localhost:5000/document')
            .then((res) => {
                this.documents = res.data;
            })
            .catch((error) => {
                console.error(error);
            });
        },
        uploadDocument(document) {
            console.log(document);

            let formData = new FormData();
            formData.append('file', document);
            formData.append('user_id', this.loggedInUser.user_id);

            console.log(formData);

            axios.post('http://localhost:5000/document', formData, {
                    headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then((res) => {
                this.getUploadedDocuments()
				showNotification("Success", "File added successfully.", "success", 2000);
            })
            .catch((error) => {
				console.log(error)
				showNotification("Error", error.response.data, "error", 2000);
            });
        },
        deleteDocument(uploaded_doc_id, filename) {
            axios.delete('http://localhost:5000/document', { params: {
                    'uploaded_doc_id': uploaded_doc_id,
                    'file_name': filename
                }
            })
            .then((res) => {
				showNotification("Success", "File deleted successfully.", "success", 2000);
                this.getUploadedDocuments()
            })
            .catch((error) => {
                console.error(error);
            });
        },
        dateFormat(date) {
            return moment(date).format('MM-DD-YYYY HH:mm');
        },
        onFilesUpload(event) {
            event.files.forEach(file => {
				console.log(file);
                this.uploadDocument(file);
            });
        },
        onError(event) {
            console.log('Upload Error:', event);
        }
    },
    mounted() {
        this.getUploadedDocuments();
    }
}

</script>
<style lang="scss">
.document-editor {
	padding: 1rem;
	display: flex;
	flex-direction: column;
	gap: 1rem;
	height: 100%;
	&__heading {
		margin: 0;
	}
	&__panel {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		flex: 1;
	}
	&__content {
		flex: 1;
		position: relative;
	}
	&__wrapper {
		position: absolute;
		left: 0;
		top: 0;
		right: 0;
		bottom: 0;
		overflow-y: auto;
	}
	.p-file-upload {
		height: 100%;
		display: flex;
		flex-direction: column;
	}
	.p-fileupload-file {
		margin: 0;
		padding: .5rem;
		height: 5rem;
	}
	.p-fileupload-file-thumbnail {
		// TODO Remove to display icon (broken atm)
		display: none;
	}
	.p-fileupload-buttonbar {
		padding: .5rem;
	}
	.p-fileupload-content {
		flex: 1;
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		grid-template-rows: 5rem;
		gap: .5rem;
		padding: 1rem .5rem;
	}
	.p-fileupload-file-details {
		flex: 1;
	}
	.p-fileupload-file-remove {
		color: red;
	}
}
</style>
