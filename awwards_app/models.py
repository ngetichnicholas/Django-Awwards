from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=144)
  description = models.TextField()
  posted_on = models.DateTimeField(auto_now_add=True)
  project_image = CloudinaryField('image')
  repo_link = models.URLField(max_length=300)
  live_link = models.URLField(max_length=300)
  user = models.ForeignKey(User,on_delete = models.CASCADE)


class Profile(models.Model):
  profile_picture = CloudinaryField('image')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  email = models.EmailField()
  phone = models.CharField(max_length=10)
  address = models.CharField(max_length=30)

class Rate(models.Model):
  content_wise = models.IntegerField(blank=True,default=0)
  usability_wise = models.IntegerField(blank=True,default=0)
  design_wise = models.IntegerField(blank=True,default=0)
  average_rate = models.FloatField(default=0.0,blank=True)
  project = models.ForeignKey(Project,on_delete=CASCADE)
  user = models.ForeignKey(User,on_delete=CASCADE)
