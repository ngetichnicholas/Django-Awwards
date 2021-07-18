from awwards_app.models import Project
from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import Registration,UpdateUser,UpdateProfile,PostProjectForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
@login_required
def index(request):
  post_form = PostProjectForm()
  all_users = User.objects.all()
  projects = Project.display_projects()


  
  return render (request,'index.html',{"projects":projects,"post":post_form,"all_users":all_users})

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

@login_required
def profile(request):
  current_user = request.user
  all_users = User.objects.all()
  
  return render(request,'profile/profile.html',{'all_users':all_users,"current_user":current_user})

@login_required
def update_profile(request):
  if request.method == 'POST':
    user_form = UpdateUser(request.POST,instance=request.user)
    profile_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    user_form = UpdateUser(instance=request.user)
    profile_form = UpdateProfile(instance=request.user.profile) 
  params = {
    'user_form':user_form,
    'profile_form':profile_form
  }
  return render(request,'profile/update.html',params)

@login_required
def search(request):
  if 'search_user' in request.GET and request.GET["search_user"]:
    search_term = request.GET.get('search_user')
  return render(request,'search.html')

@login_required
def post(request):
  if request.method == 'POST':
    post_form = PostProjectForm(request.POST,request.FILES) 
    if post_form.is_valid():
      the_post = post_form.save(commit = False)
      the_post.user = request.user
      the_post.save()
      return redirect('home')

  else:
    post_form = PostProjectForm()
  return render(request,'post.html',{"post_form":post_form})