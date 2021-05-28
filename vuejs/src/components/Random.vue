<template>
  <div class="d-flex justify-content-center align-content-center m-3" style="color:white">
    <div class="font-extrabold text-lg text-light">
    <b-button 
      type="button"  
      v-on:click="pickOne"
      pill variant="outline-danger"
    >Random
    </b-button>
    <br/>
    <img class="pick m-2 border" v-bind:src="pickMoviePoster">
  </div>
  </div>
</template>

<script>
import movieArrData from "../../../final_pjt_back/movies/fixtures/movies/movie.json"

export default {
  name: 'Random',
  data: function () {
    return {
      movieArr : movieArrData,
      pickMovieName : "NULL",
      pickMoviePoster :''
    }
  },
  methods : {
    pickOne : function () {
      console.log(this)
      console.log("hi");
      var randomIndex = parseInt(Math.random() * this.movieArr.length)
      this.pickMovieName = this.movieArr[randomIndex].fields.title
      this.pickMoviePoster = this.movieArr[randomIndex].fields.poster
      console.log(this.movieArr[randomIndex].title);
    }
  },
}
</script>
<style scoped>
.pick {
  width: 300px;
  height: 400px;
}
.jbGrad05 {
        background: linear-gradient( 45deg, yellow, red );
      }
.border {
  border-radius: 30px;
}
</style>