<template>
  <div>
    <div class="col my-4" id="">
      <div class="movie" @click="isModalViewed=true">
        <img class="w-75 border" :src="movie.poster">
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
  name: 'MovieListItem',
  components: {
    ModalView
  },
  props: {
    movie: {
      type: Object,
    },
    comment: {
      type: Object,
    }
  },
  data () {
    return {
      isModalViewed: false,
    }
  },
}
</script>

<style>
  .movie {
    transition: all 0.3s;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: rgb(165, 165, 165);
  }
  .movie:hover {
    box-shadow: 0 0 5px white;
    transform: scale(1.1);
  }
  .modal-dialog {
    top: 30%;
  }

</style>