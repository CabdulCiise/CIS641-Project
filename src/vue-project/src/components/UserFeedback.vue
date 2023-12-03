<template>
	<div class="user-feedback">
		<TabView>
			<TabPanel header="New">
				<div class="user-feedback__panel">
					<div class="user-feedback__content">
						<div class="user-feedback__wrapper">
							<DataTable
								scrollable
								scroll-height="flex"
								:value="userFeedbacks"
								paginator
								:rows="20"
								:rowsPerPageOptions="[5, 10, 20, 50]"
								paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
								currentPageReportTemplate="{first} to {last} of {totalRecords}"
							>
								<Column field="created_date" sortable header="Date" style="width: 15%">
									<template #body="{ data }">{{ dateFormat(data.created_date) }}</template>
								</Column>
								<Column field="feedback" sortable header="Feedback" style="width: 75%"></Column>
								<Column field="" header="" style="width: 10%">
									<template #body="slotProps">
										<Button label="Archive" @click="archiveUserFeedback(slotProps.data.user_feedback_id)"/>
									</template>
								</Column>
							</DataTable>
						</div>
					</div>
				</div>
			</TabPanel>
			<TabPanel header="Archived">
				<div class="user-feedback__panel">
					<div class="user-feedback__content">
						<div class="user-feedback__wrapper">
							<DataTable
								scrollable
								scroll-height="flex"
								:value="archivedUserFeedbacks"
								paginator
								:rows="20"
								:rowsPerPageOptions="[5, 10, 20, 50]"
								paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
								currentPageReportTemplate="{first} to {last} of {totalRecords}"
							>
								<Column field="created_date" sortable header="Date" style="width: 15%">
									<template #body="{ data }">{{ dateFormat(data.created_date) }}</template>
								</Column>
								<Column field="feedback" sortable header="Feedback" style="width: 85%"></Column>
							</DataTable>
						</div>
					</div>
				</div>
			</TabPanel>
		</TabView>
	</div>
</template>

<script>
import axios from 'axios';
import moment from 'moment'

import Dialog from 'primevue/dialog';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button'
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';

import { showNotification } from '../services/notification'

export default {
	props: {},
	components: {
		Dialog,
		DataTable,
		Column,
		Button,
		TabView,
		TabPanel
	},
	data() {
		return {
			userFeedbacks: [],
			archivedUserFeedbacks: [],
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
		getArchivedUserFeedbacks() {
			axios.get('http://localhost:5000/user-feedback/archive')
				.then((res) => {
					this.archivedUserFeedbacks = res.data;
				})
				.catch((error) => {
					console.error(error);
				});
		},
		archiveUserFeedback(user_feedback_id) {
			axios.put(`http://localhost:5000/user-feedback/archive?user_feedback_id=${user_feedback_id}`)
				.then((res) => {
					this.getUserFeedbacks()
					this.getArchivedUserFeedbacks();
                    showNotification("Success", "User feedback archived.", "success", 2000);
				})
				.catch((error) => {
					console.error(error);
				});
		},
		dateFormat(date) {
			console.log(date)
			return moment(date).format('MM-DD-YYYY HH:mm');
		},
	},
	created() {
		this.getUserFeedbacks();
		this.getArchivedUserFeedbacks();
	},
}
</script>

<style lang="scss">
.user-feedback {
	padding: 1rem;
	height: 100%;

	.p-tabview {

		height: 100%;
		display: flex;
		flex-direction: column;

		.p-tabview-panels {
			flex: 1;
		}

		.p-tabview-panel {
			height: 100%;
		}
	}

	&__panel {
		height: 100%;
	}

	&__content {
		position: relative;
		height: 100%;
	}

	&__wrapper {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
	}
}
</style>
