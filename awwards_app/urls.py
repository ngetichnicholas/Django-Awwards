from django.conf.urls import url
from django.urls import re_path,path
from django.contrib.auth import views as auth_views
from . import views as app_views

urlpatterns = [
  path('index/',app_views.index,name='home'),
  path('accounts/register/',app_views.register,name='register'),
  path('',auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('accounts/profile/',app_views.profile,name='profile'),
  path('update/',app_views.update_profile,name='update_profile'),
  path('post/',app_views.post,name='post'),
  path('project/<int:project_id>',app_views.detail,  name='project.detail'),
  re_path(r'^search/$',app_views.search,name='search'),
  re_path(r'^users/(?P<pk>\d+)$',app_views.users_profile,name='users_profile'),

]