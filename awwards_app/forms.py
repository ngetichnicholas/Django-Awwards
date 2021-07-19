from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile,Rate
    
class Registration(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username','email','password1','password2']

class PostProjectForm(forms.ModelForm):

  class Meta:
    model = Project
    fields = ('title','description','project_image','repo_link','live_link', 'technologies_used')

class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_picture','bio','phone','address']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design_wise', 'usability_wise', 'content_wise']







