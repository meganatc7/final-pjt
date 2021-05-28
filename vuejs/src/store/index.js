import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


axios.defaults.baseURL = 'http://localhost:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    userInfo: {},
    userCreateStatus: '',
    username: '',
    token: localStorage.getItem('token') || '',
    movieList: [],
    page: 1,
    latestMovieList: [],
    latestMovieItem: [],
    movieItem: [],
    searchedMovieList: [],
    bestMovieList: [],
    bestMovieItem: [],
    comments: {},
    commentList: [],
    nowPage: 'home',
    userCommentList: [],
    myMovieList: [],
    recommendedMovieList: [],
    userWishList: [],

  },
  getters: {
    getPage(state) {
      return state.nowPage
    },
    isAuthenticated(state) {
      return state.token ? true : false
    },
    getUserInfo(state) {
      return state.username
    },
    getMovieList(state) {
      return state.movieList
    },
    getLatestMovieList(state) {
      return state.latestMovieList
    },
    getBestMovieList(state) {
      return state.bestMovieList
    },
    getUserCreateStatus(state) {
      return state.userCreateStatus
    },
    getSearchMovieList(state) {
      return state.searchedMovieList
    },
    get(state) {
      return state.comments
    },
    getMovieCommentList(state) {
      return state.commentList
    },
    getUserCommentList(state) {
      return state.userCommentList
    },
    getMyMovieList(state) {
      const myList = []
      for (let i = 0; i < state.myMovieList.length; i++ ) {
        myList.push(state.myMovieList[i].movie)
      }
      return myList
    },
    getRecommendedMovieList(state) {
      return state.recommendedMovieList
    },
    getUserWishList(state) {
      return state.userWishList
    },
  },
  mutations: {
    HOME(state) {
      state.nowPage = 'home'
    },
    EVAL(state) {
      state.nowPage = 'eval'
    },
    PROFILE(state) {
      state.nowPage = 'profile'
    },
    CREATE_USER(state, userCreateData) {
      state.userInfo = userCreateData.userInfo
      state.userCreateStatus = userCreateData.status
    },
    AUTH_USER(state, payload) {
      state.token = payload.token
      state.username = payload.username
      state.nowPage = 'home'
      localStorage.setItem('username', state.username)
    },
    GET_MOVIE_LIST(state, movieList) {
      state.movieList.push(...movieList)
      state.page += 1
    },
    GET_LATEST_MOVIE_LIST(state, movieList) {
      state.latestMovieList = movieList
    },
    GET_BEST_MOVIE_LIST(state, movieList) {
      state.bestMovieList = movieList
    },
    LOGOUT(state) {
      state.token = ''
      localStorage.removeItem('token')
      localStorage.removeItem('username')
    },
    SET_LATEST_LAYER(state, movie) {
      state.latestMovieItem = movie
    },
    SET_BEST_LAYER(state, movie) {
      state.bestMovieItem = movie
    },
    SEARCH_MOVIE(state, searchedMovieList) {
      state.searchedMovieList = searchedMovieList
    },
    FILTER_MOVIE(state, filterMovieList) {
      state.movieList = filterMovieList
    },
    CREATE_COMMENT(state, comments) {
      
      state.comments = comments
      state.commentList.push(comments)
    },
    DELETE_COMMENT(state, comment) {
      const idx = state.userCommentList.indexOf(comment)
      state.userCommentList.splice(idx,1)
    },
    GET_MOVIE_COMMENT(state, commentList) {
      state.commentList = commentList
    },
    GET_USER_COMMENT(state, commentList) {
      state.userCommentList = commentList
    },
    GET_MY_MOVIE_LIST(state, myMovieList) {
      state.myMovieList = myMovieList
    },
    GET_RECOMMENDED_MOVIE_LIST(state, recommendedMovieList) {
      state.recommendedMovieList = recommendedMovieList 
    },
    GET_USER_WISH(state, wishList) {
      state.userWishList = wishList
      
    },
    CHECK_MOVIE(state, payload) {
      state.myMovieList.push(payload)
    }
  },
  actions: {
    async CREATE_USER({ commit }, userInfo) {
      const USER_CREATE_URL = '/api/v1/accounts/signup/'
      const data = userInfo
      const response = await axios.post(USER_CREATE_URL, data)
      const userCreateData = {
        'userInfo': response.data,
        'status': response.status
      }
      commit('CREATE_USER', userCreateData)
    },
    async AUTH_USER({ commit }, userInfo) {
      const AUTH_USER_URL = '/api/token/'
      const data = userInfo
      const response = await axios.post(AUTH_USER_URL, data)
      
      const token = response.data.access
      const payload = {'username': userInfo.username, 'token': token}
      localStorage.setItem('token', token)
      commit('AUTH_USER', payload)
    },
    async GET_MOVIE_LIST({ state, commit }) {
      const MOVIE_LIST_URL = '/api/v1/movies/'
      const response = await axios.get(`${MOVIE_LIST_URL}?page=${state.page}`)
      commit('GET_MOVIE_LIST', response.data)
    },
    async GET_LATEST_MOVIE_LIST({ commit }) {
      const LATEST_MOVIE_LIST_URL = '/api/v1/movies/latest'
      const response = await axios.get(LATEST_MOVIE_LIST_URL)
      let latestMovieList = response.data
      latestMovieList = latestMovieList.filter(function (a) {
        return a.release_date.replace(/-/g, '') <= 20210525
      })
      // yyyyMMdd 20210101 -> 20210201(현재) - 20210301 => 마이너스 나오니까 필터 제외
      let newlatestMovieList = []
      latestMovieList.forEach((element) => {
        if (!newlatestMovieList.includes(element)) {
          newlatestMovieList.push(element);
        }
      })
      newlatestMovieList = newlatestMovieList.sort(function (a, b) {
        return b.release_date.replace(/-/g, '') - a.release_date.replace(/-/g, '');
      }).slice(0, 15)
      
      commit('GET_LATEST_MOVIE_LIST', newlatestMovieList)
    },
    async GET_BEST_MOVIE_LIST({ commit }) {
      const BEST_MOVIE_LIST_URL = '/api/v1/movies/best'
      const response = await axios.get(BEST_MOVIE_LIST_URL)
      let bestMovieList = response.data
      bestMovieList = bestMovieList.sort().slice(0, 5)
      
      commit('GET_BEST_MOVIE_LIST', bestMovieList)
    },
    async SEARCH_MOVIE({ commit }, keyword) {
      const SEARCH_MOVIE_URL = `/api/v1/movies/search/${keyword}`
      const response = await axios.get(SEARCH_MOVIE_URL)
      commit('SEARCH_MOVIE', response.data)
    },
    async FILTER_MOVIE({ commit }, category) {
      const FILTER_MOVIE_URL = `/api/v1/movies/${category}`
      const response = await axios.get(FILTER_MOVIE_URL)
      
      commit('FILTER_MOVIE', response.data)
    },
    async CHECK_MOVIE({commit}, movie_id) {
      const CHECK_MOVIE_URL = '/api/v1/movies/checklist/'
      
      const data = {
        'username': localStorage.getItem('username'),
        'movie': movie_id
      }
      const response = await axios.post(CHECK_MOVIE_URL, data)
      
      commit('CHECK_MOVIE', response.data)
    },
    async CREATE_COMMENT({ commit }, comments){
      const COMMENT_CREATE_URL = '/api/v1/movies/createcomments/'
      const data = comments
      const response = await axios.post(COMMENT_CREATE_URL, data)
      const commentCreateData = {
        'comments': response.data,
      }
      commit('CREATE_COMMENT', commentCreateData)
    },
    async DELETE_COMMENT({ commit }, comment) {
      const COMMENT_DELETE_URL = `/api/v1/movies/comments/${comment.id}/`
      let response = await axios.delete(COMMENT_DELETE_URL)
      response = comment
      commit('DELETE_COMMENT', response)
    },
    async UPDATE_COMMENT({ commit }, comments) {
      const COMMENT_UPDATE_URL = `/api/v1/movies/comments/${comments.id}/`
      await axios.put(COMMENT_UPDATE_URL,comments)
      
      commit('UPDATE_COMMENT')
    },
    async GET_MOVIE_COMMENT({ commit }, payload) {
      const movie_id = payload.movie_id
      const page = payload.page
      const GET_COMMENT_URL = `/api/v1/movies/${movie_id}/comments/?page=${page}`
      const response = await axios.get(GET_COMMENT_URL)
      commit('GET_MOVIE_COMMENT', response.data)
    },
    async GET_USER_COMMENT({ commit }, params) {
      const GET_COMMENT_URL = `/api/v1/movies/user/comment/`
      const data = params
      const response = await axios.post(GET_COMMENT_URL, data)
      let userCommentList = [];
      for (let i=0; i<response.data.length; i++) {

        let isSkiped = false
        for (let j=0; j<userCommentList.length; j++) {
          if (userCommentList[j].movie.id == response.data[i].movie.id) {
            isSkiped = true
            break
          }
        }
        if (response.data[i].username != localStorage.getItem("username")) {
          isSkiped = true
        }
        if (isSkiped) continue
        else userCommentList.push(response.data[i])
      }
      commit('GET_USER_COMMENT', userCommentList)
    },
    async GET_WISH_LIST({ commit }, params) {
      const LIKE_MOVIE_LIST_URL = '/api/v1/movies/like'
      const data = params
      const response = await axios.post(LIKE_MOVIE_LIST_URL, data)
      commit('GET_LIKE_MOVIE_LIST', response.data)
    },
    async GET_MY_MOVIE_LIST({ commit }) {
      const username = localStorage.getItem('username')
      const GET_MY_MOVIE_URL = `/api/v1/movies/like/${username}`

      const response = await axios.get(GET_MY_MOVIE_URL)
      
      commit('GET_MY_MOVIE_LIST', response.data)
    },
    async GET_RECOMMENDED_MOVIE_LIST({ commit }) {
      const username = localStorage.getItem('username')
      const GET_RECOMMENDED_MOVIE_LIST_URL = `/api/v1/movies/recommend/${username}`
      const response = await axios.get(GET_RECOMMENDED_MOVIE_LIST_URL)
      
      commit('GET_RECOMMENDED_MOVIE_LIST', response.data)
    }
  },
  modules: {
  }
})
