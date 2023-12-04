<template>
	<div class="document-editor">
		<h3 class="document-editor__heading">Upload New Documents</h3>
		<FileUpload name="document[]" url="http://localhost:5000/document" @upload="onAdvancedUpload($event)" :multiple="true" accept=".pdf" :maxFileSize="1000000">
			<template #empty>
				<p>Drag and drop files to here to upload.</p>
			</template>
		</FileUpload>
		<h3 class="document-editor__heading">Delete Documents</h3>
		<DataTable
			:value="documents"
			paginator
			:rows="5"
			:rowsPerPageOptions="[5, 10, 20, 50]"
		>
            <Column field="created_date" sortable  header="Date" style="width: 20%">
                <template #body="{ data }">{{ dateFormat(data.created_date) }}</template>
            </Column>
            <Column field="name" sortable header="File Name" style="width: 30%"></Column>
            <Column field="" header="Delete" style="width: 20%">
                <template #body="{ data }">
                    <Button type="submit" @click="onDeleteDocument(data.uploaded_doc_id)" severity="danger" label="Delete"/>
                </template>
            </Column>
		</DataTable>
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

export default {
    props: {},
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
        uploadDocument() {
            axios.put(`http://localhost:5000/user-feedback/archive?user_feedback_id=${user_feedback_id}`)
                .then((res) => {
                    this.getUserFeedbacks()
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        dateFormat(date) {
            return moment(date).format('MM-DD-YYYY HH:mm');
        },
        onDeleteDocument(uploaded_doc_id) {
            console.log(uploaded_doc_id);
        }
    },
    created() {
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
	&__heading {
		margin: 0;
	}
}
</style>
