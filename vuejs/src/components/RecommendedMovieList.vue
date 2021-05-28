<template>
  <div>
    <div>
      <h2 class="fw-bold text-light text-start text-bold content-font mt-5">이런 영화는 어떠신가요?</h2>
    </div>
    <div class="row row-cols-4">
      <RecommendedMovieListItem 
        v-for="movie in getRecommendedMovieList"
        :key="movie.pk"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import RecommendedMovieListItem from '@/components/RecommendedMovieListItem'

export default {
  name: 'RecommendedMovieList',
  components: {
    RecommendedMovieListItem,
  },
  computed: {
    getRecommendedMovieList() {
      return _.sampleSize(this.$store.getters.getRecommendedMovieList,8)
    }
  },
  created() {
    this.$store.dispatch('GET_RECOMMENDED_MOVIE_LIST')
  },
}
</script>

<style>

</style>