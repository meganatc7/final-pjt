<template>
  <div class="background">
    <div class="right-side">
      <div class="form mt-5">
        <div class="choice pe-4">
          <span @click="loginClick" :class="{ activate: state == 'login' }">Login</span> / 
          <span @click="signUpClick" :class="{ activate: state == 'signup' }">Signup</span>
        </div>
        <div v-if="state === 'login'">
          <LoginForm />
        </div>
        <div v-else>
          <SignupForm />
        </div>
      </div>
    </div>
    <div class="sentence">
      <h1>Welcome to SGMovies</h1>
      <h2>Play your movie right Now!<br>
      Enjoy millions of the latest movies & 
      Conversation with us more. 
      Anytime, anywhere, across your devices.<br></h2>
      <h3>Copyright © 2021 |   hyojin,  changyoung,  sunyoung</h3>
      
      <br>
    </div>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'
import SignupForm from '@/components/SignupForm'

export default {
  name: 'LoginSignupView',
  data() {
    return{
      state: 'login',
    }
  },
  components: {
    LoginForm,
    SignupForm,
  },
  methods: {
    loginClick() {
      this.state = 'login'
    },
    signUpClick() {
      this.state = 'signup'
    }
  }
}
</script>

<style>
  .background {
    background: url(../assets/man.jpg);
    background-size: cover;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: row-reverse;
    justify-content: space-between
  }

  .background::before {
    content: '';
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    background-color: rgba(0,0,0,0.2);
  }

  .right-side {
    background-color: black;
    position: relative;
    box-shadow: -5px 5px 10px rgb(12, 12, 12);
    width: 25%;
    height: 100vh;
    text-align: right;
  }

  .right-side > div {
    margin-right: 15px;
    top: 20px;
  }

  .form {
    top: 100px;
  }

  .choice {
    color: white;
  }

  .choice > span {
    cursor: pointer;
  }

  .sentence {
    color: white;
    position: absolute;
    text-align: left;
    bottom: 100px;
    left: 30px;
    text-shadow: 2px 4px 1px rgba(0,0,0,1);
  }

  .activate {
    color: yellow;
    font-size: 20px;
    text-shadow: 0 0 20px yellow;
  }
</style>