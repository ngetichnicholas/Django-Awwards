from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=144)
  description = models.TextField()
  published_at = models.DateTimeField(auto_now_add=True)
  project_image = CloudinaryField('image')
  repo_link = models.CharField(max_length=144)
  live_link = models.CharField(max_length=144)
