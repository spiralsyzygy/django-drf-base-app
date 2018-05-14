<template>
<div class="container">
  <div class="row">
    <div class="panel panel-primary">
      <div class="panel-body Absolute-Center is-Responsive">
        <div class="panel-heading">Sign up</div>
        <form @submit.prevent="submitSignup()">
          <div class="form-group" v-bind:class="{ 'form-group--error': $v.signupForm.username.$error }">
            <input class="form__input" v-model.trim="signupForm.username"
            @input="$v.signupForm.username.$touch()"
            @click="clearError('username')"
            placeholder="Username"
            >
            <span class="form-group__message" v-if="!$v.signupForm.username.minLength">
              Name must have at least {{$v.signupForm.username.$params.minLength.min}} letters.
            </span>
            <span class="form-group__message" v-if="errors.username" v-for="msg in errors.username">
              {{ msg }}
            </span>
          </div>
          <div class="form-group" v-bind:class="{ 'form-group--error': $v.signupForm.email.$error }">
            <input class="form__input" v-model.trim="signupForm.email"
            @input="$v.signupForm.email.$touch()"
            @click="clearError('email')"
            placeholder="Email"
            >
            <span class="form-group__message" v-if="errors.email" v-for="msg in errors.email">
              {{ msg }}
            </span>
            <span class="form-group__message" v-if="!$v.signupForm.email.minLength">
              Email must have at least {{ $v.signupForm.email.$params.minLength.min }} letters.
            </span>
            <span class="form-group__message" v-if="!$v.signupForm.email.email">
              Invalid email!
            </span>
          </div>
          <div class="form-group" v-bind:class="{ 'form-group--error': $v.signupForm.password.$error }">
            <input class="form__input" v-model.trim="signupForm.password"
            @input="$v.signupForm.password.$touch()"
            v-on:click="clearError('password')"
            placeholder="Password"
            type="password"
            >
            <span class="form-group__message" v-if="errors.password" v-for="msg in errors.password">
              {{ msg }}
            </span>
            <span class="form-group__message" v-if="!$v.signupForm.password.minLength">
              Password must have at least {{ $v.signupForm.password.$params.minLength.min }} letters.
            </span>
          </div>
          <div class="form-group__message" v-bind:class="{ 'form-group--error': $v.signupForm.confirm_password.$error }">
            <input class="form__input" v-model.trim="signupForm.confirm_password"
            @input="$v.signupForm.confirm_password.$touch()"
            placeholder="Confirm Password"
            type="password"
            >
            <span class="form-group__message" v-if="!$v.signupForm.confirm_password.sameAsPassword">
              Passwords must be identical.
            </span>
            <span class="form-group__message" v-if="errors.non_field_errors" v-for="msg in errors.non_field_errors">
              {{ msg }}
            </span>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
</template>

<script>
/* eslint-disable */
import { required, minLength, sameAs, email as email_validator } from 'vuelidate/lib/validators'
// import { email as email_validator } from 'vuelidate/lib/validators'

const signup_url = 'signup/'
let page_errors = {}

export default {
  methods: {
    submitSignup () {
      console.log(this.signupForm)
      this.axios.post(
        signup_url,
        this.signupForm
      ).then(response => {
        // TODO: redirect on success
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
      signupForm: {
        username: '',
        email: '',
        password: '',
        confirm_password: ''
      },
      errors: {}
    }
  },

  validations: {
    signupForm: {
      username: {
        required,
        minLength: minLength(6)
      },
      email: {
        required,
        minLength: minLength(6),
        email: email_validator
      },
      password: {
        required,
        minLength: minLength(8)
      },
      confirm_password: {
        required,
        minLength: minLength(8),
        sameAsPassword: sameAs('password')
      }
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
