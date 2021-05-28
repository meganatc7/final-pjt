<template>
  <div>
    <div>
      <h4 class="text-light mt-5">감명 깊게 본 영화를 골라주세요</h4>
      <p class="text-light">(당신의 영화 추천에 도움이 됩니다)</p>
      <EvalMovieList />
    </div>
  </div>
</template>

<script>
import EvalMovieList from '@/components/EvalMovieList'

export default {
  name: 'MovieEvaluation',
  components: {
    EvalMovieList,
  },
}
</script>

<style>

</style>