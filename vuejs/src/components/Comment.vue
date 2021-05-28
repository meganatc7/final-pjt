<template>
<div>
  <div class="modal-body comment-page d-flex justify-content-between align-items-center">
    <div class="w-25 text-left">
      <p>평점: {{ movie.vote_average }}</p>
      <p>개봉일: {{ movie.release_date }}</p>
      <p>런타임: {{ movie.runtime }}</p>
      <!-- <p>댓글 수: {{ getCommentList.length }}</p> -->
    </div>
    <div class="row row-cols-2 w-75" v-if="getCommentList.length">
      <div
        class="col mt-4" 
        v-for="comment in getCommentList"
        :key="comment.id"
        
      >
      <div class="d-flex align-items-center justify-content-between">
        <div>
          <h1>{{ comment.username }}</h1> 
          <p>{{ comment.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</p>
        </div>
        <div>
          <span>{{ comment.rank }} / 5</span>
        </div>
      </div>
        <p>{{ comment.content }}</p>
      </div>
    </div>
    <div v-else class="w-75">
      <h1 class="text-start">아직 등록된 댓글이 없습니다.</h1>
    </div>
  </div>
  <div @click="getNextPage" class="pb-5" v-if="getCommentList.length">
    <v-pagination
      v-model="page"
      :length="5"
      :total-visible="7"
      class="mt-5"
      @click="getNextPage"
    ></v-pagination>
  </div>
</div>

</template>

<script>

export default {
  name: 'Comment',
  data() {
    return {
      page: 1,
    }
  },
  computed: {
    getCommentList() {
      return this.$store.getters.getMovieCommentList
    },
  },
  props: {
    movie: {
      type:Object,
    }
  },
  methods: {
    getNextPage() {
      this.$store.dispatch('GET_MOVIE_COMMENT', {page: this.page, movie_id: this.movie.id})
    }
  }
}
</script>

<style>

</style>