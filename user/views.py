from django.shortcuts import render,redirect,get_object_or_404
from .forms import Register,NewLogin,NewMessage,ProfileUpdate
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.
def register(request):
   if request.user.is_authenticated == True:
      profileuser=request.user.profile.slug
      return redirect(f'profile/{profileuser}')
   form=Register()
   if request.method=='POST':
      form=Register(request.POST)
      if form.is_valid():
         newuser=form.save(commit=False)
         newuser.set_password(form.cleaned_data['password'])
         newuser.save()
         username=form.cleaned_data['username']
         password=form.cleaned_data['password']
         loginv(request,username,password)
         profileuser=request.user.profile.slug
         return redirect(f'profile/{profileuser}')
   
   context={
      'title':'register',
      'form':form,
   }
   return render(request,'user/register.html',context)
   pass 


def loginv(request,username=None,password=None):
   if request.user.is_authenticated == True:
      profileuser=request.user.profile.slug
      return redirect(f'/profile/{profileuser}')
   form=NewLogin()
   if request.method =='POST':
      username=request.POST['username']
      password=request.POST['password']
      user=authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         profileuser=request.user.profile.slug
         return redirect(f'/profile/{profileuser}')
         
   context={
      'title':'login',
      'form':form,
   }
   
   return render(request,'user/login.html',context)
   pass 


def profile(request,slug):
   getprofile=get_object_or_404(Profile,slug=slug)
   form=NewMessage()
   formupdate=ProfileUpdate()
   if request.method=='POST':
      form=NewMessage(request.POST)
      if form.is_valid():
         newmassage=form.save(commit=False)
         newmassage.userProfile=getprofile
         newmassage.save()
         messages.success(request,'done ✌')
         form = NewMessage()
         return redirect(f'/profile/{getprofile}')

   if request.method=='POST':
      formupdate=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
      if formupdate.is_valid():
         formupdate.save()
   
   context={
      'title':'profile',
      'getprofile':getprofile,
      'form':form,
      'formupdate':formupdate,
   }
   return render(request,'user/profile.html',context)
   pass 


def logoutv(request):
   logout(request)
   return redirect('login')