<template>
  <div>
    <nav class="mt-5 align-items-center">
      <div class="me-5">
        <span class="fs-3 fw-bold">찜한 영화</span>
      </div>
    </nav>

    <WishListCarousel />
      
  </div>
</template>

<script>
import WishListCarousel from '@/components/WishListCarousel'

export default {
  name: 'WishList',
  components: {
    WishListCarousel,
  },
  created() {
    this.$store.dispatch('GET_WISH_LIST')
  },
}
</script>

