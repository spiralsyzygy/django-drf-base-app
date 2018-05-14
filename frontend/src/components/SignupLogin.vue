<template>
  <div class="signuplogin">
    <h1>{{ msg }}</h1>
      <a href='/signup'>Sign up</a>
      <a href='/login'>Login</a>
  </div>
</template>

<script>
export default {
  name: 'SignupLogin',
  data () {
    return {
      msg: 'Sign up or Login'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
