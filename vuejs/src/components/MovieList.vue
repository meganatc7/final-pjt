<template>
  <div>
    <nav class="d-flex mt-5 align-items-center justify-content-between movie-list-nav">
      <div class="me-5 d-flex align-items-center">
        <span class="fs-3 fw-bold content-font">모든 영화</span>
        <div class="filter ms-5">
          <span class="content-font" :class="{ pick: state == 1 }" @click=all>전체</span>
          <span class="content-font" :class="{ pick: state == 2 }" @click=action>액션</span>
          <span class="content-font" :class="{ pick: state == 3 }" @click=comedy>코미디</span>
          <span class="content-font" :class="{ pick: state == 4 }" @click=horror>공포</span>
          <span class="content-font" :class="{ pick: state == 5 }" @click=animation>애니메이션</span>
          <span class="content-font" :class="{ pick: state == 6 }" @click=sf>SF</span>
        </div>
      </div>
      <div class="" style="right:0;">
        <input 
          type="text" 
          class="me-3 search-box" 
          :class="{ searching: searching }"
          @input=onSearchInput
          v-model.trim=keyword
          placeholder="검색"
        >
        <i class="fas fa-search fa-lg search" style="color:white;" @click=onSearch></i>
      </div>
    </nav>
    <div class="row row-cols-4" v-if="keyword.length === 0">
      <MovieListItem
        v-for="movie in movieList"
        :key="movie.pk"
        :movie="movie"
      />
    </div>
    <div class="row row-cols-4" v-else>
      <MovieListItem
        v-for="movie in searchMovieList"
        :key="movie.pk"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
import _ from 'lodash'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data() {
    return {
      state: 1,
      searching: false,
      keyword: '',
    }
  },
  computed: {
    movieList() {
      return this.$store.getters.getMovieList
    },
    searchMovieList() {
      return this.$store.getters.getSearchMovieList
    }
  },
  methods: {
    all() {
      this.state = 1
      this.$store.dispatch('FILTER_MOVIE','전체')
      // document.addEventListener('scroll', _.throttle(this.checkBottomFilter('전체'),500))
    },
    action() {
      this.state = 2
      this.$store.dispatch('FILTER_MOVIE','액션')
      // document.addEventListener('scroll', _.throttle(this.checkBottomFilter('액션'),500))
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
      const {scrollTop, clientHeight, scrollHeight} = document.documentElement
      if (scrollHeight - scrollTop <= clientHeight + 400) {
        this.$store.dispatch('GET_MOVIE_LIST')
      }
    },
    checkBottomFilter(category) {
      console.log(category)
      // const {scrollTop, clientHeight, scrollHeight} = document.documentElement
      // if (scrollHeight - scrollTop <= clientHeight + 400) {
      //   this.$store.dispatch('GET_MOVIE_LIST')
      // }
    },
    onSearch() {
      this.searching = !this.searching
    },
    onSearchInput() {
      _.throttle(this.$store.dispatch('SEARCH_MOVIE', this.keyword),150)
    }
  },
  created() {
    this.$store.dispatch('GET_MOVIE_LIST')
    document.addEventListener('scroll', _.throttle(this.checkBottom,500))
  },
}
</script>

<style>
  nav.movie-list-nav span {
    color: white;
  }
  .filter span {
    margin-right: 15px;
    cursor: pointer;
  }

  .filter span:hover {
    text-shadow: 0 0 5px yellow;
    font-size: 17px;
  }

  .pick {
    color: yellow;
    font-size: 17px;
  }

  .search-box {
    width: 0;
    padding: 0;
    background-color: white;
    border: none;
    border-radius: 10px;
    transition: all .5s;
  }

  .searching {
    width: 250px;
    padding: 5px;
  }

  .search {
    cursor: pointer;
  }
</style>