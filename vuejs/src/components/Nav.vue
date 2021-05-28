<template>
  <div>
    <nav class="navbar navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
        <div>

          <router-link to="/">
            <img @click="homePage" src="../assets/logo.png" alt="" class="logo">
          </router-link>
          <router-link 
            class="ms-5 link" 
            to="/movie-evaluation"
          >
            <span @click="changePage">영화 고르기</span>
          </router-link>
        </div>
        <div class="user-info dropdown">
          <div class="" id="drop" data-bs-toggle="dropdown">
            <img src="../assets/man.jpg" alt="" class="me-3">
            <p class="text-light">{{ getUser }}</p>
          </div>
          <ul class="dropdown-menu" aria-labelledby="drop">
            <li><a href="" class="dropdown-item" @click.prevent="logout">Logout</a></li>
            <li>
              <router-link to="/profile" class="dropdown-item"><span @click="profilePage">Profile</span></router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Nav',

  data() {
    return {
    }
  },
  computed: {
    getUser() {
      return localStorage.getItem('username')
    }
  },
  methods: {
    logout() {
      this.$store.commit('LOGOUT')
    },
    changePage() {
      this.$emit('change-page')
    },
    homePage() {
      this.$emit('home-page')
    },
    profilePage() {
      this.$emit('profile-page')
    }
  }
}
</script>

<style>
.user-info {
  margin-right: 200px;
  cursor: pointer;
}

.user-info img {
  width: 30px;
  height: 30px;
  border-radius: 15px;
  border: 1px solid orange;
}

.user-info p{
  display: inline;
  color: white;
  margin-right: 20px;
}

.link {
  text-decoration: none;
}

.link > span {
  color: white; 
}

.link > span:hover {
  color: gold;
}
</style>