from django.conf.urls import url
from django.urls import re_path,path,include
from django.contrib.auth import views as auth_views
from . import views as app_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  path('',app_views.index,name='home'),
  path('accounts/register/',app_views.register,name='register'),
  path('accounts/login/',app_views.login,name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('accounts/profile/',app_views.profile,name='profile'),
  path('update/',app_views.update_profile,name='update_profile'),
  path('post/',app_views.post_project,name='post'),
  path('project/<int:project_id>',app_views.detail,  name='project.detail'),
  path('api/projects/',app_views.ProjectList.as_view()),
  path('api/profiles/',app_views.ProfileList.as_view()),
  path('api_token/', obtain_auth_token),
  re_path(r'^search/$',app_views.search,name='search'),
  re_path(r'^users/(?P<pk>\d+)$',app_views.users_profile,name='users_profile'),
  re_path(r'^delete/(?P<project_id>\d+)$',app_views.delete,name='delete'),


]