<template>
  <div>
    <div class="col my-4">
      <div class="movie" @click="isModalViewed=true">
        <img class="w-75 border" :src="movie.poster" alt="">
        <span class="mt-3 title-font">{{ movie.title }}</span>
      </div>
    </div>
    <ModalView 
      v-if="isModalViewed"
      :movie="movie"
      @close="isModalViewed=false"
    />
  </div>
</template>

<script>
import ModalView from "@/components/ModalView"

export default {
  name: 'RecommendedMovieListItem',
  components: {
      ModalView,
  },
  data () {
    return {
      isModalViewed: false,
    }
  },
  props: {
    movie: {
      type: Object,
    }
  },
}
</script>

<style>

</style>