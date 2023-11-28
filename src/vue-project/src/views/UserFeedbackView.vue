<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1>User Feedback</h1>
        <hr>
        <table class="table table-hover">
          <thead>
            <tr>
              <th class="col-10">Feedback</th>
              <th class="col-2"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="feedback in user_feedbacks">
              <td>{{ feedback.feedback }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm" v-on:click="archiveUserFeedback(feedback.user_feedback_id)">Archive</button>
                </div>
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
  
  export default {
    data() {
      return {
        user_feedbacks: []
      }
    },
    methods: {
      getUserFeedbacks() {
        axios.get('http://localhost:5000/user-feedback')
          .then((res) => {
            this.user_feedbacks = res.data;
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
