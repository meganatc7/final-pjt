from django.urls import path
from . import views


urlpatterns = [

    # GET, POST http://localhost:8000/api/v1/
    path('', views.index),
    # GET, PIT, DELETE  http://localhost:8000/api/v1/todos/:id
    path('<int:todo_id>/', views.movie_detail),

    # 전체 댓글 목록 가져오기
    # GET http://localhost:8000/api/v1/movies/comments/
    path('<int:movie_id>/comments/', views.comment_list),

    # 댓글 생성하기
    # POST http://localhost:8000/api/v1/movies/createcomments/
    path('createcomments/', views.create_comment),

    # 댓글 수정하기
    # GET, POST http://localhost:8000/api/v1/movies/comments/<int:comment_id>/
    path('comments/<int:comment_id>/', views.comment_detail),

    # GET, POST http://localhost:8000/api/v1/latest/
    path('latest/', views.latest),

    # MovieCrousel에 들어갈 부분
    path('best/', views.best),
    # 영화 검색
    path('search/<str:keyword>/', views.search_movie),

    # 영화 체크리스트 (평가기능에서 체크한 영화들)
    path('checklist/', views.check_movie),
    
    # 영화 필터링
    path('<str:category>/', views.filter_movie),

    # 사용자 댓글 리스트
    # POST http://localhost:8000/api/v1/movies/user/comment
    path('user/comment/', views.get_user_comment_list),

    # 좋아한 영화 리스트
    path('like/<str:username>/', views.get_like_movie_list),

    # 추천 영화 리스트
    path('recommend/<str:username>/', views.recommend_movie),
]