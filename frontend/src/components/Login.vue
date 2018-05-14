<template>
<div class="container">
  <div class="row">
    <div class="panel panel-primary">
      <div class="panel-body Absolute-Center is-Responsive">
        <div class="panel-heading">Login</div>
        <form @submit.prevent="submitLogin()">
          <div class="form-group">
            <input class="form__input" v-model.trim="loginForm.username"
            @input="$v.loginForm.username.$touch()"
            @click="clearError('username')"
            placeholder="Username">
            <span class="form-group__message" v-if="errors.username" v-for="msg in errors.username">
              {{ msg }}
            </span>
          </div>
          <div class="form-group">
            <input class="form__input" v-model.trim="loginForm.password"
            @input="$v.loginForm.password.$touch()"
            v-on:click="clearError('password')"
            placeholder="Password"
            type="password">
            <span class="form-group__message" v-if="errors.password" v-for="msg in errors.password">
              {{ msg }}
            </span>
            <span class="form-group__message" v-if="errors.non_field_errors" v-for="msg in errors.non_field_errors">
              {{ msg }}
            </span>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-primary">Login</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
</template>

<script>
/* eslint-disable */
import { required, minLength } from 'vuelidate/lib/validators'

const login_url = 'token-auth/'
let page_errors = {}

export default {
  methods: {
    submitLogin () {
      console.log(this.loginForm)
      this.axios.post(
        login_url,
        this.loginForm,
      ).then(response => {
        // TODO: store token in vuex
        // TODO: redirect on success
        this.token = response.data['token']
        console.log("Recieved token:", this.token)
        console.log(response.data)
      }).catch(error => {
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          console.log("Response Error!")
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
          page_errors = error.response.data
          this.errors = page_errors
          console.log("this.errors", this.errors)
        } else if (error.request) {
          // The request was made but no response was received
          // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
          // http.ClientRequest in node.js
          console.log("Request Error!")
          console.log(error.request);
        } else {
          // Something happened in setting up the request that triggered an Error
          console.log('Error', error.message);
          }
          console.log('Error config', error.config);
      })
    },
    clearError (field) {
      delete this.errors[field]
      delete this.errors.non_field_errors
    }
  },

  data () {
    return {
      loginForm: {
        username: '',
        password: '',
      },
      errors: {},
      token: ''
    }
  },

  validations: {
    loginForm: {
      username: {
        required,
        minLength: minLength(6)
      },
      password: {
        required,
        minLength: minLength(8)
      }
    }
  }
}
</script>

<style>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
