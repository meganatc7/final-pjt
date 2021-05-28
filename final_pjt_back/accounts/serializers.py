from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Userlike, User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email',)

class UserlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlike 
        exclude = ('user',)

