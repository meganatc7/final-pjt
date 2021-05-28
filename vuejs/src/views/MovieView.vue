<template>
  <div>

    <MovieCarousel />
   <div class="container">
    <RecentMovie />
    <RecommendedMovieList />
    <MovieList />
    <Movie />

  </div>

  
  </div>
</template>

<script>
import MovieCarousel from '@/components/MovieCarousel'
import MovieList from '@/components/MovieList'
import RecentMovie from '@/components/RecentMovie'
import Movie from '@/components/Movie'
import RecommendedMovieList from '@/components/RecommendedMovieList'

export default {
  name: 'MovieView',
  components: {
    MovieCarousel,
    MovieList,
    RecentMovie,
    Movie,
    RecommendedMovieList,
  },
  created() {
    this.$store.dispatch('GET_MOVIE_LIST')
    this.$store.dispatch('GET_LATEST_MOVIE_LIST')
    this.$store.dispatch('GET_BEST_MOVIE_LIST')
  },
}
</script>

<style>

</style>