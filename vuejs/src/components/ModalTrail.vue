<template>

  <div class="container mb-4">
    <div class="container h-100 pb-4">
      <div class="h-100 video-container embed-responsive embed-responsive-16by9" v-if="videoList.length">
        <iframe width="100%" height="100%" class="embed-responsive-item" :src="videoUrl" allowfullscreen frameborder="0"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


const YOUTUBE_API_KEY = 'AIzaSyBCNyVF3W6jLT2rmdc5du7hHM-dXJWAoPg'
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'ModalTrail',
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  data(){
    return {
      videoList: ''
    }
  },

  methods: {
    async searchVideo() {
      const keyword = '공식 예고편 ' + this.movie.title
      const config = {
        params: {
          part: 'snippet',
          type: 'video',
          q: keyword,
          key: YOUTUBE_API_KEY
        }
      }
      const response = await axios.get(YOUTUBE_API_URL, config)
      this.videoList = response.data.items
    },
  },
  created() {
    this.searchVideo()
  },
  computed: {

    videoUrl() {
      const videoId = this.videoList[0].id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
}
</script>

<style>

</style>