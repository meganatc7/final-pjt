<template>
  <div>
    <nav class="d-flex mt-5 align-items-center">
      <div class="me-5">
        <span class="fs-3 fw-bold content-font">최신 영화</span>
      </div>
    </nav>

    <RecentMovieCarousel 
      :GetLatestMovieList="GetLatestMovieList"
    />
      
  </div>
</template>

<style scoped>
.content-font {
  font-family: 'Nanum Myeongjo', serif;
  color: white;
}
</style>

<script>
import RecentMovieCarousel from '@/components/RecentMovieCarousel'

export default {
  name: 'RecentMovie',
  components: {
    RecentMovieCarousel,
  },
  computed: {
    GetLatestMovieList(){
      return this.$store.getters.getLatestMovieList
    }
  },
  created() {
    this.$store.dispatch('GET_LATEST_MOVIE_LIST')
  },
}
</script>

