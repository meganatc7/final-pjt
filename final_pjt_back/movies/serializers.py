from rest_framework import serializers
from .models import Movie, Comment, Wishlist


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ('user','movie', 'rank', 'content', 'username', 'id', 'created_at')
        # 댓글을 작성할 때, movie는 입력하지 않을 것이므로, movie필드는 읽기 전용.
        read_only_fields = ['user', 'movie', 'id', 'created_at']

class CommentMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Comment 
        fields = ('user','movie', 'rank', 'content', 'username', 'id')
        # 댓글을 작성할 때, movie는 입력하지 않을 것이므로, movie필드는 읽기 전용.
        read_only_fields = ['user', 'movie', 'id', '']


class MovieItemSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 
        'overview', 'language', 'poster', 'genres', 
        'runtime', 'release_date', 'vote_average', 'vote_count', 
        'comment_set')


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('movie', 'user')
        read_only_fields = ['movie', 'user']


# 프로필 페이지의 댓글 쓴 영화 불러오기
class CommentSetSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Comment 
        fields = ('user','movie', 'rank', 'content', 'username', 'id')
        # 댓글을 작성할 때, movie는 입력하지 않을 것이므로, movie필드는 읽기 전용.
        read_only_fields = ['user', 'movie', 'id']