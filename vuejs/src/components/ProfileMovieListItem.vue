<template>
  <div>
    <div class="col my-4" id="">
      <div class="profile-movie">
        <img class="w-75 border" :src="movie.poster" @click="isModalViewed=true">
        <span class="mt-3 title-font">{{ comment.content }}</span>
        <div class="d-flex">
          <button class="btn btn-sm text-danger" @click="deleteComment">댓글 삭제</button>
          <button class="btn btn-sm text-warning" @click="showModal = true">댓글 수정</button>
        </div>
      </div>
    </div>
    <CommentUpdateModal 
      v-if="showModal" 
      @close="showModal=false"
      :movie="movie"
      :comment="comment"
    />
    <ModalView 
      v-if="isModalViewed"
      :movie="movie"
      @close="isModalViewed=false"
    />
  </div>
</template>

<script>
import ModalView from "@/components/ModalView"
import CommentUpdateModal from '@/components/CommentUpdateModal' 

export default {
  name: 'ProfileMovieListItem',
  components: {
    ModalView,
    CommentUpdateModal,
  },
  props: {
    movie: {
      type: Object,
      required: true,
    },
    comment: {
      type: Object,
      required: true,
    }
  },
  data () {
    return {
      isModalViewed: false,
      showModal: false,
    }
  },
  methods: {
    deleteComment() {
      this.$store.dispatch('DELETE_COMMENT', this.comment)
      this.$emit('deleted')
    }
  }
}
</script>

<style>
  .profile-movie {
    transition: all 0.3s;
    /* cursor: pointer; */
    display: flex;
    flex-direction: column;
    align-items: center;
    color: rgb(165, 165, 165);
  }
  .profile-movie:hover {
    box-shadow: 0 0 5px white;
    transform: scale(1.1);
  }
  .modal-dialog {
    top: 30%;
  }

</style>