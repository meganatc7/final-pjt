<template>
  <div class="login-form">
    <div class="area">
      <input v-model="userInfo.username" type="text" name="id" id="id" autocomplete="off" required autofocus>
      <label for="id" id="id-lb">USERNAME</label>
    </div>
    <div class="area mt-3">
      <input v-model="userInfo.password" @keyup.enter="onSubmit" type="password" name="pw" id="pw" autocomplete="off" required>
      <label for="id" id="pw-lb">PASSWORD</label>
    </div>
    <div class="d-grid gap-2 col-12 mx-auto">
      <button @click="onSubmit" class="btn btn-light mt-4">Login</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      userInfo: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    onSubmit() {
      this.$store.dispatch('AUTH_USER', this.userInfo)
      this.$router.push('/')
    }
  }
}
</script>

<style>
  .login-form {
     padding: 20px;
   }

  .area > input {
    width: 100%;
    padding: 20px 10px 0px;
    background-color: transparent;
    border: none;
    border-bottom: 1px solid #999;
    font-size: 18px;
    color: white;
  }

  .area label {
    position: absolute;
    left: 30px;
    transition: all .5s ease;
    color: rgb(143, 143, 143);
  }

  .area input:focus + label,
  .area input:valid + label {
    font-size: 13px;
    color: yellow;
  }

</style>