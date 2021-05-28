<template>
  <div>
    <transition name="modal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-container comment-container">
            <h1 class="text-light mt-4">후기 작성</h1>
            <fieldset class="rating">
              <input type="radio" id="star5" name="rating" value='5' v-model="comments.rank"/><label class = "full" for="star5" title="Awesome - 5 stars"></label>
              <input type="radio" id="star4half" name="rating" value='4.5' v-model="comments.rank"/><label class="half" for="star4half" title="Pretty good - 4.5 stars"></label>
              <input type="radio" id="star4" name="rating" value='4' v-model="comments.rank"/><label class = "full" for="star4" title="Pretty good - 4 stars"></label>
              <input type="radio" id="star3half" name="rating" value='3.5' v-model="comments.rank"/><label class="half" for="star3half" title="Meh - 3.5 stars"></label>
              <input type="radio" id="star3" name="rating" value='3' v-model="comments.rank"/><label class = "full" for="star3" title="Meh - 3 stars"></label>
              <input type="radio" id="star2half" name="rating" value='2.5' v-model="comments.rank"/><label class="half" for="star2half" title="Kinda bad - 2.5 stars"></label>
              <input type="radio" id="star2" name="rating" value='2' v-model="comments.rank"/><label class = "full" for="star2" title="Kinda bad - 2 stars"></label>
              <input type="radio" id="star1half" name="rating" value='1.5' v-model="comments.rank"/><label class="half" for="star1half" title="Meh - 1.5 stars"></label>
              <input type="radio" id="star1" name="rating" value="1" v-model="comments.rank"/><label class = "full" for="star1" title="Sucks big time - 1 star"></label>
              <input type="radio" id="starhalf" name="rating" value="0.5" v-model="comments.rank"/><label class="half" for="starhalf" title="Sucks big time - 0.5 stars"></label>
            </fieldset>
            <input v-model="comments.comment" type="text" class="mt-3 w-50 h-25 bg-light" @keyup.enter="onSubmit" ref="commentInput">
            <div class="d-flex mt-4">
              <button class="btn btn-light me-4" @click="onSubmit" >작성 완료</button>
              <button class="btn btn-light ms-4" @click="$emit('close')">닫기</button>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'CommentModal',
  data() {
    return {
      comments: {
        comment: '',
        rank: 0,
        userId: '',
        movieId: '',
      },
    }
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  methods: {
    onSubmit() {
      if (!this.comments.comment.length) return 
      this.comments.movieId = this.movie.id
      this.comments.userId = localStorage.getItem('username')

      this.$store.dispatch('CREATE_COMMENT', this.comments)
      this.$emit('close')
      this.$store.dispatch('GET_MOVIE_COMMENT', {page: 1, movie_id: this.movie.id})
      this.comments.comment = '' // input 태그 초기화
      this.$refs.commentInput.value
    },
  },
  // computed() {
  //   userId  ,
  //   movieId = ,
  // }
}
</script>

<style scoped>
  @import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);
  .comment-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .rating { 
    border: none;

  }

  .rating > input { display: none; } 
  .rating > label:before { 
    margin: 5px;
    font-size: 3.5rem;
    font-family: FontAwesome;
    display: inline-block;
    content: "\f005";
  }

  .rating > .half:before { 
    content: "\f089";
    position: absolute;
  }

  .rating > label { 
    color: #ddd; 
  float: right; 
  }

  .rating > input:checked ~ label,
  .rating:not(:checked) > label:hover,
  .rating:not(:checked) > label:hover ~ label { color: #FFD700;  }

  .rating > input:checked + label:hover,
  .rating > input:checked ~ label:hover,
  .rating > label:hover ~ input:checked ~ label,
  .rating > input:checked ~ label:hover ~ label { color: #FFED85;  } 
</style>