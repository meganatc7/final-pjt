<template>
<div>
  <p class="text-light">{{ myMovieList }}</p>
  <div class="row row-cols-4">
    <EvalMovieListItem
      v-for="movie in movieList"
      :key="movie.pk"
      :movie=movie
      :myMovieList="myMovieList"
      :class="{ checked: movie.id in myMovieList }"
    />
  </div>
</div>
</template>

<script>
import _ from 'lodash'
import EvalMovieListItem from '@/components/EvalMovieListItem'

export default {
  name: 'EvalMovieList',
  components: {
    EvalMovieListItem
  },
  computed: {
    movieList() {
      return this.$store.getters.getMovieList
    },
    myMovieList() {
      return this.$store.getters.getMyMovieList
    }
  },
  methods: {
    checkBottom() {
        const {scrollTop, clientHeight, scrollHeight} = document.documentElement
        if (scrollHeight - scrollTop === clientHeight) {
          this.$store.dispatch('GET_MOVIE_LIST')
        }
    },
  },
  async created() {
    document.addEventListener('scroll', _.throttle(this.checkBottom,500))
    await this.$store.dispatch('GET_MOVIE_LIST')
    await this.$store.dispatch('GET_MY_MOVIE_LIST')
  },
}
</script>

<style>

</style>