from django.shortcuts import render,redirect
from .models import Message
from user.models import Profile
# Create your views here.

def inbox(request,slug):
    if request.user.profile.slug != slug:
      profileuser=request.user.profile.slug
      return redirect(f'/inbox/{profileuser}')
    massegesinbox=Message.objects.filter(slug=slug)
    context={
        'title':'inbox',
        'massegesinbox':massegesinbox,
    }
    return render(request,'ask/inbox.html',context)
    pass

def deletem(request,slug):
    if request.method=='POST':
        x=Message.objects.get(slug=slug).delete()
        print(x)
    re=request.user.profile.slug
    return redirect(f'/inbox/{re}')
    pass