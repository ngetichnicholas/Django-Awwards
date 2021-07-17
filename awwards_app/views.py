from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



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