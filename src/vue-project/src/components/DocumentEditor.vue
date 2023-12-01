<template>
    <h2>Upload New Documents</h2>
    <FileUpload name="demo[]" url="/api/upload" @upload="onTemplatedUpload($event)" :multiple="true" accept="image/*" :maxFileSize="1000000" @select="onSelectedFiles">
    <template #header="{ chooseCallback, uploadCallback, clearCallback, files }">
        <div class="flex flex-wrap justify-content-between align-items-center flex-1 gap-2">
            <div class="flex gap-2">
                <Button @click="chooseCallback()" icon="pi pi-images" rounded outlined></Button>
                <Button @click="uploadEvent(uploadCallback)" icon="pi pi-cloud-upload" rounded outlined severity="success" :disabled="!files || files.length === 0"></Button>
                <Button @click="clearCallback()" icon="pi pi-times" rounded outlined severity="danger" :disabled="!files || files.length === 0"></Button>
            </div>
            <ProgressBar :value="totalSizePercent" :showValue="false" :class="['md:w-20rem h-1rem w-full md:ml-auto', { 'exceeded-progress-bar': totalSizePercent > 100 }]"
                ><span class="white-space-nowrap">{{ totalSize }}B / 1Mb</span></ProgressBar
            >
        </div>
    </template>
    <template #content="{ files, uploadedFiles, removeUploadedFileCallback, removeFileCallback }">
        <div v-if="files.length > 0">
            <h5>Pending</h5>
            <div class="flex flex-wrap p-0 sm:p-5 gap-5">
                <div v-for="(file, index) of files" :key="file.name + file.type + file.size" class="card m-0 px-6 flex flex-column border-1 surface-border align-items-center gap-3">
                    <div>
                        <img role="presentation" :alt="file.name" :src="file.objectURL" width="100" height="50" class="shadow-2" />
                    </div>
                    <span class="font-semibold">{{ file.name }}</span>
                    <div>{{ formatSize(file.size) }}</div>
                    <Badge value="Pending" severity="warning" />
                    <Button icon="pi pi-times" @click="onRemoveTemplatingFile(file, removeFileCallback, index)" outlined rounded  severity="danger" />
                </div>
            </div>
        </div>

        <div v-if="uploadedFiles.length > 0">
            <h5>Completed</h5>
            <div class="flex flex-wrap p-0 sm:p-5 gap-5">
                <div v-for="(file, index) of uploadedFiles" :key="file.name + file.type + file.size" class="card m-0 px-6 flex flex-column border-1 surface-border align-items-center gap-3">
                    <div>
                        <img role="presentation" :alt="file.name" :src="file.objectURL" width="100" height="50" class="shadow-2" />
                    </div>
                    <span class="font-semibold">{{ file.name }}</span>
                    <div>{{ formatSize(file.size) }}</div>
                    <Badge value="Completed" class="mt-3" severity="success" />
                    <Button icon="pi pi-times" @click="removeUploadedFileCallback(index)" outlined rounded  severity="danger" />
                </div>
            </div>
        </div>
    </template>
    <template #empty>
        <div class="flex align-items-center justify-content-center flex-column">
            <i class="pi pi-cloud-upload border-2 border-circle p-5 text-8xl text-400 border-400" />
            <p class="mt-4 mb-0">Drag and drop files to here to upload.</p>
        </div>
    </template>
</FileUpload>
    <h2>Delete Documents</h2>
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