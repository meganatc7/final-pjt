<template>
  <div class="signup-form">
    <div class="area">
      <input v-model="userInfo.username" type="text" name="id" id="id" autocomplete="off" required autofocus>
      <label for="id" id="id-lb">USERNAME</label>
    </div>
    <div class="area mt-3">
      <input v-model="userInfo.email" type="email" name="eamil" id="eamil" autocomplete="off" required>
      <label for="email" id="email-lb">EMAIL</label>
    </div>
    <div class="area mt-3">
      <input v-model="userInfo.password" type="password" name="pw" id="pw" autocomplete="off" required>
      <label for="pw" id="pw-lb">PASSWORD</label>
    </div>
    <div class="area mt-3">
      <input v-model="userInfo.password_confirmation" type="password" name="pw-confirm" id="pw-confirm" autocomplete="off" required>
      <label for="pw-confirm" id="pw-lb">PASSWORD CONFIRM</label>
    </div>
    <p class="text-light" v-if="getUserCreateStatus === 200">회원가입 완료</p>
    <div class="d-grid gap-2 col-12 mx-auto">
      <button @click="onSubmit" class="btn btn-light mt-4">SignUp</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupForm',
  data() {
    return {
      userInfo: {
        username: '',
        email: '',
        password: '',
        password_confirmation: '',
      }
    }
  },
  computed: {
    getUserCreateStatus() {
      return this.$store.getters.getUserCreateStatus
    }
  },
  methods: {
    onSubmit() {
      this.$store.dispatch('CREATE_USER', this.userInfo)
    }
  }
}
</script>

<style>
  .signup-form {
     padding: 20px;
     transition: all 0.5s;
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
  }

  .area input:focus + label,
  .area input:valid + label {
    font-size: 13px;
    color: yellow;
  }
</style>