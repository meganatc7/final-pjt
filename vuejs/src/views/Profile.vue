<template>
  <div class="profile-area">
    <div class="profile-header">
      <div class="profile-header-left">
        <img class="profile-img" src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairDreads&accessoriesType=Blank&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=Heather&eyeType=Side&eyebrowType=UpDownNatural&mouthType=Disbelief&skinColor=Brown" />
        <h3 class="fs-3 fw-bold content-font">  {{ getUser }}  님, 안녕하세요</h3>
      </div>
      <div class="profile-header-right">
      
        <div class="data-area">
          <span>댓글 쓴 영화<br>
          <br><span>{{ userCommentList.length }}</span>
          </span>
        </div>
      </div>
    </div>
    <div class="profile-body">
      <p class="profile-sub-title"></p>
      <div>
        <Random />
      </div>
      <p class="profile-sub-title">댓글 쓴 영화</p>
      <div class="row row-cols-4">
        <ProfileMovieListItem
          v-for="item in userCommentList"
          :key="item.movie.pk"
          :movie="item.movie"
          :comment="item"
          :genre="item.movie.genres"
        />
      </div>
    </div>
  </div>

</template>

<style scoped>
.profile-header {
    background: rgb(85,69,69);
    padding: 40px 50px;
    color: white;
}

img.profile-img {
    border-radius: 100%;
    border: 1px solid #333;
    object-fit: cover;
    width: 150px;
    height: 150px;
}

.profile-header-left, .profile-header-right {
    display: inline-block;
    width: 50%;
}

.profile-header-left > h3 {
    font-size: 38px;
    font-weight: 700;
    display: inline-block;
    vertical-align: middle;
    margin: 0 10px;
}

.data-area:first-child {
    border-right: 2px solid white;
}

.data-area {
    display: inline-block;
    padding: 0 15px;
    text-align: center;
}

.profile-header-right {
    text-align: center;
    vertical-align: middle;
}

p.profile-sub-title {
    text-align: left;
    color: white;
    padding: 0 20px;
    margin: 10px 0;
}

.pick {
  width: 300px;
  height: 400px;
}
</style>

<script>
// const SERVER_URL = 'http://localhost:8000'
import Random from '@/components/Random'
import ProfileMovieListItem from '@/components/ProfileMovieListItem'
import _ from 'lodash'
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name: 'Profile',
  components: {
    Random,
    ProfileMovieListItem,
  },
  data() {
    return {
      profileUser: {},
      state: 1,
      searching: false,
      keyword: '',
      userName : '',
    }
  },
  props: {
    currentUser: Object,
    id: [Number, String],
  },
  computed: {
    movieList() {
      return this.$store.getters.getMovieList
    },
    searchMovieList() {
      return this.$store.getters.getSearchMovieList
    },
    getUser() {
      return localStorage.getItem("username")
    },
    userCommentList() {
      return this.$store.getters.getUserCommentList
    },
  },
  methods: {
    all() {
      this.state = 1
      this.$store.dispatch('GET_MOVIE_LIST')
      document.addEventListener('scroll', _.throttle(this.checkBottom,500))
    },
    action() {
      this.state = 2
      this.$store.dispatch('FILTER_MOVIE','액션')
    },
    comedy() {
      this.state = 3
      this.$store.dispatch('FILTER_MOVIE','코미디')
    },
    horror() {
      this.state = 4
      this.$store.dispatch('FILTER_MOVIE','공포')
    },
    animation() {
      this.state = 5
      this.$store.dispatch('FILTER_MOVIE','애니메이션')
    },
    sf() {
      this.state = 6
      this.$store.dispatch('FILTER_MOVIE','SF')
    },
    checkBottom() {
      console.log('scroll!!!')
      const {scrollTop, clientHeight, scrollHeight} = document.documentElement
      if (scrollHeight - scrollTop === clientHeight) {
        this.$store.dispatch('GET_MOVIE_LIST')
      }
    },
    onSearch() {
      this.searching = !this.searching
    },
    onSearchInput() {
      _.throttle(this.$store.dispatch('SEARCH_MOVIE', this.keyword),150)
      console.log(this.searchMovieList)
    },
    deleted() {
      this.userName = localStorage.getItem('username')
      const params = {
      username: this.userName
      }
      this.$store.dispatch('GET_USER_COMMENT', params)  
    }
  },
  created() {
    this.userName = localStorage.getItem('username')
    const params = {
      username: this.userName
    }
    this.$store.dispatch('GET_USER_COMMENT', params)
    this.$store.dispatch('GET_MOVIE_LIST')
    document.addEventListener('scroll', _.throttle(this.checkBottom,500))
  },
}
</script>