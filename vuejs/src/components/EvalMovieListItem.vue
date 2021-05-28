<template>
  <div>
    <div class="col my-4" id="">
      <div class="movie" @click="chkMovie">
        <img 
          :class="{ userlike: myMovie.includes(movie.id) }" 
          class="w-75 border" 
          :src="movie.poster" 
          alt=""
        >
        <span class="mt-3">{{ movie.title }}<i class="bi bi-bookmark-plus"></i></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EvalMovieListItem',
  props: {
    movie: {
      type: Object,
    },
    myMovieList: {
      type: Array,
    }
  },
  computed: {
    myMovie() {
      return this.$store.getters.getMyMovieList
    }
  },
  methods: {
    chkMovie() {
      const movie_id = this.movie.id
      this.$store.dispatch('CHECK_MOVIE', movie_id)
      this.$store.dispatch('GET_MY_MOVIE_LIST')
    },
  }
}
</script>

<style>
  .userlike {
    box-shadow: 0 0 15px orange;
    animation: wiggle 2s ease;
    animation-iteration-count: infinite;
  }

  @keyframes wiggle {
    0% {transform: translateY(0px)}
    50% {transform: translateY(-15px)}
    100% {transform: translateY(0px)}
  }
</style>