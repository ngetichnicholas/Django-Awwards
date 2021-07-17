from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import Registration
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
@login_required
def index(request):
  all_users = User.objects.all()
  
  return render (request,'index.html',{"all_users":all_users})

def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login')
  else:
    form = Registration()
  return render(request,'registration/registration_form.html',{"form":form})