from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required , permission_required
from home.forms import PasswordChangeForm
from django.contrib.auth.models import User


# Create your views here.

def home_logout(request):
    logout(request)
    return redirect('/')

def home_login(request):
    if request.method == "POST":

      user = authenticate(username=request.POST.get('username'),password = request.POST.get('password'))
      
      if(user is not None ):
        if(user.last_login == None):
          login(request , user)
          messages.add_message(request, messages.INFO, "Change your password!!")
          return redirect('/home/profile')
        else:
          login(request , user)
          return redirect('/dashboard/create')

      else:
    #    print(request.POST.get('password'))
         messages.add_message(request, messages.ERROR, 'invalid email or password')

    return render(request , "home/login.html" , {}) 

def home_profile(request):
    if request.method == "POST":
      form = PasswordChangeForm(request.POST)
      user = authenticate(username=request.POST.get('username'),password = request.POST.get('password'))
      
      if(form.is_valid()):
        data = form.cleaned_data
        
        user = authenticate(username=request.user.username,password = data['oldpass'])

        if(user is None ):
          messages.add_message(request, messages.ERROR, ' Old password is not correct')
          return redirect('/home/profile')
        elif(data['newpass'] != data['confirmpass']):
          messages.add_message(request, messages.ERROR, ' Passwords did not match')
          return redirect('/home/profile')
        else:
          u = User.objects.get(username=request.user.username)
          u.set_password(data['newpass'])
          u.save()
        messages.add_message(request, messages.INFO, ' Password changed successfully')
        return redirect('/home/profile')
     
    #   if(user is not None ):
    #      login(request , user)
    #      return redirect('/patient/list')
    #   else:
    # #    print(request.POST.get('password'))
    #      messages.add_message(request, messages.ERROR, 'invalid email or password')
    else:
      form = PasswordChangeForm()

    context = {
      'form' : form,
      'title' : 'Profile Information'
    }


    return render(request , "home/profile.html" , context) 

