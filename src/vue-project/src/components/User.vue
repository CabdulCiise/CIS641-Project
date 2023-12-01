<template>
    <div class="container" v-if="users && roles">
      <div class="row">
        <div class="col-12">
          <h1>User</h1>
          <hr>
          <Dropdown 
                    v-model="test"
                    :options="roles"
                    optionLabel="name"
                    optionValue="role_id"
                    placeholder="Select User Role"
                    class="w-full" />    
          <table class="table table-hover">
            <thead>
              <tr>
                <th class="col-3">Username</th>
                <th class="col-3">Role</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users">
                <td>{{ user.username }}</td>
                <td>
                  <Dropdown 
                    v-model="user.user_id"
                    :options="roles"
                    optionLabel="name"
                    optionValue="role_id"
                    placeholder="Select User Role"
                    class="w-full" />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
    import axios from 'axios'
    import Dropdown from 'primevue/dropdown';
  
    export default {
      components: {
        Dropdown
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
        updateUser(userId, newRole) {
          axios.put('http://localhost:5000/user', {
              user_id: userId,
              role: newRole
            })
            .then((res) => {
              this.getUsers()
            })
            .catch((error) => {
              console.error(error);
            });
        }
      },
      created() {
        this.getUsers();
        this.getRoles();
      },
    }
  </script>
  
  <style scoped>
  </style>
  