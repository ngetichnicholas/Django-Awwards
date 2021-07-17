from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=144)
  description = models.TextField()
  published_at = models.DateTimeField(auto_now_add=True)
  project_image = CloudinaryField('image')
  repo_link = models.CharField(max_length=144)
  live_link = models.CharField(max_length=144)

class Profile(models.Model):
  profile_picture = CloudinaryField('image')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  email = models.EmailField()
  phone = models.CharField(max_length=10)
  address = models.CharField(max_length=30)
