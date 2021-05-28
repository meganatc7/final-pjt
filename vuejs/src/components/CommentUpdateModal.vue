<template>
  <div>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container comment-container">
          <fieldset class="rating">
            <input type="radio" id="star5" name="rating" value="5" v-model="rank" /><label class = "full" for="star5" title="Awesome - 5 stars"></label>
            <input type="radio" id="star4half" name="rating" value="4.5" v-model="rank" /><label class="half" for="star4half" title="Pretty good - 4.5 stars"></label>
            <input type="radio" id="star4" name="rating" value="4" v-model="rank"/><label class = "full" for="star4" title="Pretty good - 4 stars"></label>
            <input type="radio" id="star3half" name="rating" value="3.5" v-model="rank"/><label class="half" for="star3half" title="Meh - 3.5 stars"></label>
            <input type="radio" id="star3" name="rating" value="3" v-model="rank" /><label class = "full" for="star3" title="Meh - 3 stars"></label>
            <input type="radio" id="star2half" name="rating" value="2.5" v-model="rank"/><label class="half" for="star2half" title="Kinda bad - 2.5 stars"></label>
            <input type="radio" id="star2" name="rating" value="2" v-model="rank"/><label class = "full" for="star2" title="Kinda bad - 2 stars"></label>
            <input type="radio" id="star1half" name="rating" value="1.5" v-model="rank"/><label class="half" for="star1half" title="Meh - 1.5 stars"></label>
            <input type="radio" id="star1" name="rating" value="1" v-model="rank"/><label class = "full" for="star1" title="Sucks big time - 1 star"></label>
            <input type="radio" id="starhalf" name="rating" value="0.5" v-model="rank"/><label class="half" for="starhalf" title="Sucks big time - 0.5 stars"></label>
          </fieldset>
          <input type="text" v-model="content" class="border w-100 h-50 mt-4">
          <div class="d-grid gap-2 col-12 mx-auto mt-5">
            <button class="btn btn-warning" type="button" @click="onSubmit">수정 완료</button>
            <button class="btn btn-danger" type="button" @click="$emit('close')">닫기</button>
          </div>
        </div>
      </div>
    </div>
  </transition>
  </div>
</template>

<script>

export default {
  name: 'CommentUpdateModal',
  data() {
    return {
      content: this.comment.content,
      rank: 0,
    }
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
  methods: {
    onSubmit() {
      this.comment.content = this.content
      if (this.rank !== 0) {
        this.comment.rank = this.rank
      }
      console.log(this.comment)
      this.$store.dispatch("UPDATE_COMMENT", this.comment)
    }
  }
}
</script>

<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

  .comment-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    display: table;
    transition: opacity .3s ease;
  }

  .modal-wrapper {
    display: table-cell;
    vertical-align: middle;
  }

  .modal-container {
    width: 500px;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
    transition: all .3s ease;
    font-family: Helvetica, Arial, sans-serif;
  }

  .modal-header h3 {
    margin-top: 0;
    color: #42b983;
  }

  .modal-body {
    margin: 20px 0;
  }

  .modal-default-button {
    float: right;
  }

  .modal-enter .modal-container,
  .modal-leave-active .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
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