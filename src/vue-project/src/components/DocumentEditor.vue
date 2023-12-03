<template>
	<div class="document-editor">
		<h2 class="document-editor__heading">Upload New Documents</h2>
		<FileUpload name="document[]" url="http://localhost:5000/document" @upload="onAdvancedUpload($event)" :multiple="true" accept=".pdf" :maxFileSize="1000000">
			<template #empty>
				<p>Drag and drop files to here to upload.</p>
			</template>
		</FileUpload>
		<h2 class="document-editor__heading">Delete Documents</h2>
		<DataTable
			:value="uploadedDocs"
			paginator
			:rows="5"
			:rowsPerPageOptions="[5, 10, 20, 50]"
		>
			<Column field="username" header="Username" style="width: 10%"></Column>
			<Column field="date" header="Date" style="width: 10%"></Column>
			<Column field="feedback" header="Feedback" style="width: 80%"></Column>
		</DataTable>
	</div>
</template>

<script>
import axios from 'axios'
import FileUpload from 'primevue/fileupload'
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

        }
    },
    methods: {
        getUploadedDocuments() {
            axios.get('http://localhost:5000/document')
                .then((res) => {
                    this.userFeedbacks = res.data;
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
