from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.TextField()
    email = models.EmailField(unique=True)
    pass

class Userlike(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    crime = models.IntegerField(default=0)
    documentary = models.IntegerField(default=0)
    drama = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    mystery = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    sf = models.IntegerField(default=0)
    tvmovie = models.IntegerField(default=0)
    thriller = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    western = models.IntegerField(default=0)