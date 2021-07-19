from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator




# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=144)
  description = models.TextField()
  posted_on = models.DateTimeField(auto_now_add=True)
  project_image = CloudinaryField('image')
  repo_link = models.URLField(max_length=300)
  live_link = models.URLField(max_length=300)
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  technologies_used =models.TextField()

  @classmethod
  def display_projects(cls):
    projects = cls.objects.all().order_by('-posted_on')
    return projects

  def save_project(self):
    self.save()

  def delete_project(self):
    self.delete()

  @classmethod
  def search_projects(cls, title):
    return cls.objects.filter(title__icontains=title).all()

  @classmethod
  def get_projects(cls):
    return cls.objects.all()

  def __str__(self):
    return f'{self.title}'

class Profile(models.Model):
  profile_picture = CloudinaryField('image')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  phone = models.CharField(max_length=10)
  address = models.CharField(max_length=30)

  @receiver(post_save , sender = User)
  def create_profile(instance,sender,created,**kwargs):
    if created:
      Profile.objects.create(user = instance)

  @receiver(post_save,sender = User)
  def save_profile(sender,instance,**kwargs):
    instance.profile.save()

  def __str__(self):
    return "%s profile" % self.user

class Rate(models.Model):
  content_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
  content_wise_average = models.FloatField(default=0.0,blank=True)
  usability_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
  usability_wise_average = models.FloatField(default=0.0,blank=True)
  design_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
  design_wise_average = models.FloatField(default=0.0,blank=True)
  aggregate_average_rate = models.FloatField(default=0.0,blank=True)
  project = models.ForeignKey(Project,on_delete=CASCADE)
  user = models.ForeignKey(User,on_delete=CASCADE)


  def save_rating(self):
      self.save()

  @classmethod
  def get_ratings(cls, id):
      ratings = Rate.objects.filter(project_id=id).all()
      return ratings

  def __str__(self):
      return f'{self.project} Rating'

