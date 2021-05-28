<template>
  <div class="thumb-example">

    <swiper class="swiper gallery-top" id="bg" :options="swiperOptionTop" ref="swiperTop">
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Ella/Ella_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Line/0525/Line_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Conjuring/0518/Conjuring_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/InTheHeights/InTheHeights_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Truck/0520/Truck_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Voyagers/0524/Voyagers_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Place/Place_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Spiral/0520/Spiral_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/TheFast/0525/TheFast_1920774.jpg">
      </swiper-slide>
      <swiper-slide>
        <img class="bd main-header-style" src="https://caching2.lottecinema.co.kr/lotte_image/2021/Killer/0520/Killer_1920774.jpg">
      </swiper-slide>
      <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
      <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>
    </swiper>
  </div>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'

  export default {
    name: 'swiper-example-thumbs-gallery',
    title: 'Thumbs gallery with Two-way control',
    components: {
      Swiper,
      SwiperSlide
    },
    computed: {
      GetBestMovieList(){
        return this.$store.getters.getBestMovieList
      }
    },
    data() {
      return {
        swiperOptionTop: {
          loop: true,
          loopedSlides: 5, // looped slides should be the same
          spaceBetween: 10,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        swiperOptionThumbs: {
          loop: true,
          loopedSlides: 5, // looped slides should be the same
          spaceBetween: 10,
          centeredSlides: true,
          slidesPerView: 'auto',
          touchRatio: 0.2,
          slideToClickedSlide: true
        }
      }
    },
  }
</script>

<style lang="scss" scoped>
  .bd {
    border-radius: 30px;
  }
  .swiper {
    .swiper-slide {
      background-size: cover;
      background-position: center;

      &.slide-1 {
        background-image:url('/images/example/1.jpg');
      }
      &.slide-2 {
        background-image:url('/images/example/2.jpg');
      }
      &.slide-3 {
        background-image:url('/images/example/4.jpg');
      }
      &.slide-4 {
        background-image:url('/images/example/5.jpg');
      }
      &.slide-5 {
        background-image:url('/images/example/6.jpg');
      }
    }

    &.gallery-top {
      height: 100%;
      width: 100%;
    }
    &.gallery-thumbs {
      height: 250px;
      box-sizing: border-box;
    }
    &.gallery-thumbs .swiper-slide {
      width: 25%;
      height: 100%;
      opacity: 0.4;
    }
    &.gallery-thumbs .swiper-slide-active {
      opacity: 1;
    }
  }

  img.gallery-top-image {
    width: 100%;
    height: 70%;
    object-fit: contain;
  }

  img.gallery-thumbs-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .main-header-style{
    width: 100%;
    object-fit: contain;
  }

  .angled-gradient { 
    background: linear-gradient(70deg, blue, pink); 
    }

  #bg { 
  top: 0; 
  left: 0; 
    
  /* Preserve aspet ratio */
  min-width: 100%;
  min-height: 100%;
}
</style>