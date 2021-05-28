import re
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Q

# from django.shortcuts import render

from django.shortcuts import get_object_or_404

from .serializers import (
    MovieSerializer,
    CommentSerializer,
    WishlistSerializer,

    CommentMovieSerializer,

    CommentSetSerializer,
)
from .models import Movie, Comment, Wishlist

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        # 1. 모든 movie list를 가져온다
        movies = Movie.objects.all()
        # 1-2. 20개씩 짤라서 페이지네이션
        paginator = Paginator(movies, 20)  

        page = request.GET.get('page')
        movies = paginator.get_page(page)

        # 2. serialize
        serializer = MovieSerializer(movies, many=True) 
        # 3. 응답
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data) # binding
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            # API 응답 구조
            # - 응답 데이터
            # - 상태 코드(201)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, todo_id):
    movies = get_object_or_404(Movie, pk=todo_id)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movies)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(
            data=request.data, instance=movies
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
    
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 댓글 전체 리스트 가져오기
@api_view(['GET'])
def comment_list(request, movie_id):
    comments = Comment.objects.filter(movie_id=movie_id).order_by('-pk')
    
    paginator = Paginator(comments, 4)

    page = request.GET.get('page')
    comments = paginator.get_page(page)

    serializer = CommentSerializer(comments, many=True)
    return Response(data=serializer.data)


# 댓글 만들기
@api_view(['POST'])
def create_comment(request):
    movie_id = request.data.get('movieId')
    username = request.data.get('userId')
    content = request.data.get('comment')
    rank = float(request.data.get('rank'))

    movie = get_object_or_404(Movie, id=movie_id)
    user = get_object_or_404(get_user_model(), username=username)
    data = {
        'content': content,
        'rank': rank,
        'username': username,
    }
    
    serializer = CommentSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        # 댓글 정보 영화에 저장
        comment = serializer.save(movie=movie, user=user)
        return Response(data=serializer.data)

# 댓글 수정 및 삭제
# http://localhost:8000/api/v1/movies/comments/<int:comment_id>/
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(data=serializer.data)

    elif request.method == 'DELETE':
        comment = comment.delete()
        data = {
            'message': '댓글 삭제가 완료되었습니다.'
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(data=serializer.data)


# 최신 영화 불러오기
@api_view(['GET'])
def latest(request):
    # 1. 모든 movie list를 가져온다
    movies = Movie.objects.all()
    # 2. serialize
    serializer = MovieSerializer(movies, many=True)
    # 3. 응답
    return Response(data=serializer.data)


@api_view(['GET'])
def best(request):
    movies = Movie.objects.order_by('vote_average')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def search_movie(request, keyword):
    reg = re.compile(r'[a-zA-Z]')

    if reg.match(keyword):
        movies = Movie.objects.filter(original_title__contains=keyword)
    else:
        movies = Movie.objects.filter(title__contains=keyword)
    
    serializer = MovieSerializer(movies, many=True)
    
    return Response(data=serializer.data)


@api_view(['GET'])
def filter_movie(request, category):
    if category == '전체':
        movies = Movie.objects.all()
    else:
        movies = Movie.objects.filter(genres__contains=category)
    

    serializer = MovieSerializer(movies, many=True)

    return Response(data=serializer.data)


@api_view(['POST'])
def check_movie(request):
    
    username = request.data.get('username')
    movie_id = request.data.get('movie')

    user = get_object_or_404(get_user_model(), username=username)
    movie = get_object_or_404(Movie, id=movie_id)


    data = {
        'user': user,
        'movie': movie,
    }
    serializer = WishlistSerializer(data=data)

    
    user_data = user.userlike_set.get(user=user.pk)
    
    genres = movie.genres.split(' ')


    if serializer.is_valid(raise_exception=True):
        if Wishlist.objects.filter(user=user.id, movie=movie.id).exists():
            movie = Wishlist.objects.filter(user=user.id, movie=movie.id)
            movie.delete()
            return Response({'message':'exsists'})
    
        for genre in genres:
            if genre == '액션':
                user_data.action = user_data.action + 1
                user_data.save()
            if genre == '모험':
                user_data.adventure = user_data.adventure + 1
                user_data.save()
            if genre == '애니메이션':
                user_data.animation = user_data.animation + 1
                user_data.save()
            if genre == '코미디':
                user_data.comedy = user_data.comedy + 1
                user_data.save()
            if genre == '범죄':
                user_data.crime = user_data.crime + 1
                user_data.save()
            if genre == '다큐멘터리':
                user_data.documentary = user_data.documentary + 1
                user_data.save()
            if genre == '드라마':
                user_data.drama = user_data.drama + 1
                user_data.save()
            if genre == '가족':
                user_data.family = user_data.family + 1
                user_data.save()
            if genre == '판타지':
                user_data.fantasy = user_data.fantasy + 1
                user_data.save()
            if genre == '역사':
                user_data.history = user_data.history + 1
                user_data.save()
            if genre == '공포':
                user_data.horror = user_data.horror + 1
                user_data.save()
            if genre == '음악':
                user_data.music = user_data.music + 1
                user_data.save()
            if genre == '미스터리':
                user_data.mystery = user_data.mystery + 1
                user_data.save()
            if genre == '로맨스':
                user_data.romance = user_data.romance + 1
                user_data.save()
            if genre == 'SF':
                user_data.sf = user_data.sf + 1
                user_data.save()
            if genre == '티비':
                user_data.tvmovie = user_data.tvmovie + 1
                user_data.save()
            if genre == '스릴러':
                user_data.thriller = user_data.thriller + 1
                user_data.save()
            if genre == '전쟁':
                user_data.war = user_data.war + 1
                user_data.save()
            if genre == '서부':
                user_data.western = user_data.western + 1
                user_data.save()
        serializer.save(user=user, movie=movie)
        return Response(data=serializer.data)
    return Response({'message':'wait'})


@api_view(['POST'])
def get_user_comment_list(request):
    username = request.data.get('username')

    comment_list = Comment.objects.filter(username=username).select_related('movie')
    serializer = CommentSetSerializer(comment_list, many=True)

    return Response(data=serializer.data)


@api_view(['GET'])
def get_like_movie_list(request, username):
    
    user = get_object_or_404(get_user_model(), username=username)
    my_movie_list = Wishlist.objects.filter(user=user.id)
    
    serializer = WishlistSerializer(my_movie_list, many=True)
    
    return Response(data=serializer.data)


@api_view(['GET'])
def recommend_movie(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_data = user.userlike_set.get(user=user.id)
    score = [
        (user_data.action,'액션'),
        (user_data.adventure,'모험'),
        (user_data.animation,'애니메이션'),
        (user_data.comedy,'코미디'),
        (user_data.crime,'범죄'),
        (user_data.documentary,'다큐멘터리'),
        (user_data.drama,'드라마'),
        (user_data.family,'가족'),
        (user_data.fantasy,'판타지'),
        (user_data.history,'역사'),
        (user_data.horror,'공포'),
        (user_data.music,'음악'),
        (user_data.mystery,'미스터리'),
        (user_data.romance,'로맨스'),
        (user_data.sf,'SF'),
        (user_data.tvmovie,'티비'),
        (user_data.thriller,'스릴러'),
        (user_data.war,'전쟁'),
        (user_data.western,'서부')
    ]
    score.sort(reverse=True)
    top_one = score[0][1]
    top_two = score[1][1]
    top_three = score[2][1]

    movie1 = Movie.objects.filter(genres__contains=top_one)
    movie2 = Movie.objects.filter(genres__contains=top_two)
    movie3 = Movie.objects.filter(genres__contains=top_three)

    recommended_movie = movie1.union(movie2,movie3)

    serializer = MovieSerializer(recommended_movie, many=True)
        
    
    return Response(data=serializer.data)

