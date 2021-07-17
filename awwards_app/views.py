from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
  all_users = User.objects.all()
  
  return render (request,'index.html',{"all_users":all_users})