from awwards_app.models import Project,Profile,Rate
from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import Registration,UpdateUser,UpdateProfile,PostProjectForm,RatingsForm
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

  return render (request,'index.html',{"projects":projects,"post_project":post_form,"all_users":all_users})

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

def detail(request,project_id):
  all_ratings = Rate.objects.filter(project_id=project_id).all()
  project = Project.objects.get(pk = project_id)
  ratings = Rate.objects.filter(user=request.user,project=project_id).first()
  rating_status = None
  if ratings is None:
    rating_status = False
  else:
    rating_status = True
  if request.method == 'POST':
    form = RatingsForm(request.POST)
    if form.is_valid():
      rate = form.save(commit=False)
      rate.user = request.user
      rate.project = project
      rate.save()
      post_ratings = Rate.objects.filter(project=project_id)

      design_ratings = [design.design_wise for design in post_ratings]
      design_wise_average = sum(design_ratings) / len(design_ratings)

      usability_ratings = [usability.usability_wise for usability in post_ratings]
      usability_wise_average = sum(usability_ratings) / len(usability_ratings)

      content_ratings = [content.content_wise for content in post_ratings]
      content_wise_average = sum(content_ratings) / len(content_ratings)

      aggregate_average_rate = (design_wise_average + usability_wise_average + content_wise_average) / 3
      print(aggregate_average_rate)
      rate.design_wise_average = round(design_wise_average, 2)
      rate.usability_wise_average = round(usability_wise_average, 2)
      rate.content_wise_average = round(content_wise_average, 2)
      rate.aggregate_average_rate = round(aggregate_average_rate, 2)
      rate.save()
      return HttpResponseRedirect(request.path_info)
  else:
      form = RatingsForm()
  return render(request, 'project_details.html', {'all_ratings':all_ratings,'project':project,'rating_form': form,'rating_status': rating_status})

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
def post_project(request):
  if request.method == 'POST':
    post_form = PostProjectForm(request.POST,request.FILES) 
    if post_form.is_valid():
      new_post = post_form.save(commit = False)
      new_post.user = request.user
      new_post.save()
      return redirect('home')

  else:
    post_form = PostProjectForm()
  return render(request,'post_project.html',{"post_form":post_form})

@login_required
def users_profile(request,pk):
  user = User.objects.get(pk = pk)
  projects = Project.objects.filter(user = user)
  current_user = request.user
  
  return render(request,'profile/users_profile.html',{"user":user,"projects":projects,"current_user":current_user})

@login_required
def delete(request,project_id):
  current_user = request.user
  project = Project.objects.get(pk=project_id)
  if project:
    project.delete_project()
  return redirect('home')