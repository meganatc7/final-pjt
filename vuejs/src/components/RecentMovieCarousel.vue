<template>
  <swiper class="swiper example-3d" :options="swiperOption">
    <swiper-slide v-for="movie in GetLatestMovieList" :key="movie.pk">
      <img class="border w-100" :src="movie.poster" alt="">
    </swiper-slide>
  <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'

  export default {
    name: 'swiper-example-3d-coverflow',
    title: '3D Coverflow effect',
    components: {
      Swiper,
      SwiperSlide
    },
    props: {
      GetLatestMovieList: {
        type: Array,
        required: true,
      }
    },
    data() {
      return {
        swiperOption: {
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 'auto',
          coverflowEffect: {
            rotate: 50,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows : true
          },
          pagination: {
            el: '.swiper-pagination'
          }
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .example-3d {
    width: 100%;
    height: 400px;
    padding-top: 50px;
    padding-bottom: 50px;
  }
  .border {
    border-radius: 40% 10% / 10% 10%;
  }
  .swiper {
    height: 100%;
    width: 100%;

    .swiper-slide {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 250px;
      height: 300px;
      text-align: center;
      background-color: #0000;
      background-position: center;
      background-size: cover;
      
    }
    .swiper-pagination {
      ::v-deep .swiper-pagination-bullet.swiper-pagination-bullet-active {
        
      }
    }
  }

</style>