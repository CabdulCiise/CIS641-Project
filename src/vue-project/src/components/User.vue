<template>
	<div class="user-page">
		<h3 class="user-page__heading">System Users</h3>
		<div class="user-page__content">
			<div class="user-page__wrapper">
				<DataTable
					scrollable
					scroll-height="flex"
					:value="users"
					paginator
					:rows="5"
					:rowsPerPageOptions="[5, 10, 20, 50]"
					paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
					currentPageReportTemplate="{first} to {last} of {totalRecords}"
				>
					<Column field="created_date" sortable  header="Date" style="width: 30%">
            <template #body="{ data }">{{ dateFormat(data.created_date) }}</template>
          </Column>
					<Column field="username" sortable header="Username" style="width: 40%"></Column>
					<Column field="role_id" header="Role" style="width: 30%">
						<template #body="slotProps">
							<Dropdown
								v-model="slotProps.data.user_role_id"
								:options="roles"
								optionLabel="name"
								optionValue="role_id"
								placeholder="Select User Role"
								@change="onRoleUpdated(slotProps.data.user_id, slotProps.data.user_role_id)" />
						</template>
					</Column>
				</DataTable>
			</div>
		</div>
	</div>
</template>

<script>
  import axios from 'axios'
  import moment from 'moment'

  import Dropdown from 'primevue/dropdown';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';

  export default {
    components: {
      Dropdown,
      DataTable,
      Column
    },
    data() {
      return {
        users: [],
        roles: [],
        test: 1
      }
    },
    methods: {
      getUsers() {
        axios.get('http://localhost:5000/user')
          .then((res) => {
            this.users = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      getRoles() {
        axios.get('http://localhost:5000/role')
          .then((res) => {
            this.roles = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      updateUser(userId, newRoleId) {
        axios.put('http://localhost:5000/user', {
            user_id: userId,
            role_id: newRoleId
          })
          .then((res) => {
            this.getUsers()
          })
          .catch((error) => {
            console.error(error);
          });
      },
      dateFormat(date) {
        return moment(date).format('MM-DD-YYYY HH:mm');
      },
      onRoleUpdated(userId, newRoleId) {
        this.updateUser(userId, newRoleId);
      }
    },
    created() {
      this.getUsers();
      this.getRoles();
    },
  }
</script>

<style lang="scss">
.user-page {
	padding: 1rem;
	height: 100%;
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
  &__heading {
		margin-top: 0;
	}
}
</style>
