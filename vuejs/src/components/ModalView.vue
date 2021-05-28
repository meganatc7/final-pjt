<template>
  <div class="">
    <transition name="modal">
        <div class="modal-mask"> <!-- @click="$emit('close')" -->
          <div class="modal-wrapper">
            <div class="modal-container">
              <!-- header -->
              <div class="d-flex justify-content-between">
                <div class="icons ms-5">
                  <i class="fas fa-info-circle fa-2x me-4" @click="movieInfo" :class="{ picked: category === 'info' }"></i>
                  <i class="fas fa-comment-dots fa-2x me-4" @click="movieComment" :class="{ picked: category === 'comment' }"></i>
                  <i class="fas fa-video fa-2x" @click="movieTrail" :class="{ picked: category === 'trail' }"></i>
                </div>
                <div class="me-5">
                  <i v-if="category === 'comment'" class="fas fa-edit fa-2x write-button" @click="showModal = true"></i>
                  <CommentModal v-if="showModal" @close="closeEvent" :movie="movie"/>
                  <i class="fas fa-times fa-2x cancel-button" @click="$emit('close')" style="color:white;"></i>
                </div>
              </div>
              <!-- body -->
              <div v-if="category === 'info' " class="modal-body d-flex justify-content-between">
                <div class="mt-5 px-3">
                  <h1 class="title-font pb-2">{{ movie.title }}</h1>
                  <p class="content-font">{{ movie.vote_average }}/10</p>
                  <p class="content-font">{{ movie.overview }}</p>
                </div>
                <div>
                  <img :src="movie.poster" alt="" class="poster p-3">
                </div>
              </div>
              <div v-if="category === 'comment' " class="modal-body comment-page">
                <Comment :movie="movie"/>
              </div>

              <div v-if="category === 'trail' " class="modal-body d-flex justify-content-between h-100">
                <ModalTrail :movie="movie"/>
              </div>
            </div>
          </div>
        </div>
    </transition>
  </div>
</template>

<script>
import CommentModal from '@/components/CommentModal'
import ModalTrail from '@/components/ModalTrail'
import Comment from '@/components/Comment'

export default {
  name: 'ModalView',
  components: {
    CommentModal,
    ModalTrail,
    Comment,
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      category: 'info',
      showModal: false,
      
      videoList: [],
      video: null,
    }
  },
  computed: {
    getCommentList() {
      return this.$store.getters.getMovieCommentList
    },
  },
  methods: {
    movieInfo() {
      this.category = 'info'
    },
    movieComment() {
      this.category = 'comment'
      this.$store.dispatch('GET_MOVIE_COMMENT', {page: 1, movie_id: this.movie.id})
    },
    movieTrail() {
      this.category = 'trail'
      // this.video = video
    },
    closeEvent() {
      this.showModal = false
      this.movieComment()
    }
  },
  created() {
  },
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity .3s ease;
}

.modal-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}

.modal-container {
  width: 70%;
  height: 81%;
  
  margin: 0px auto;
  padding: 20px 0 0 0;
  background-color: black;
  border-radius: 2px;
  box-shadow: 0 0 15px rgba(255, 254, 254);
  transition: all .3s ease;
  position: relative;
}

.modal-body {
  padding: 0;
  text-align: left;
  color: white;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.icons > i {
  color: grey;
  cursor: pointer;
}

.icons .picked {
  color: yellow;
}

.poster {
  float: right;
  top: 0;
  width: 300px;
  height: 65vh;
}

.cancel-button {
  cursor: pointer;
}

.write-button {
  color: white;
  margin-right: 20px;
  cursor: pointer;
}

.write-button:hover {
  color: yellow;
}

.comment-page {
  top: 15%;
}

.content-font {
  font-family: 'Nanum Myeongjo', serif;
}

.title-font{
  font-family: 'Nanum Myeongjo', serif;
  font-family: 'Poor Story', cursive; 
}

</style>