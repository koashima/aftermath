from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)