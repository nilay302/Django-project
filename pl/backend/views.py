from django.shortcuts import render, redirect
from .models import Tweets
from django.http import Http404
from .forms import TweetForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def list(request):
    all_tweets = Tweets.objects.all()
    return render(request, 'backend/tweet_list.html',{'tweets':all_tweets})

def details(request,pk):
    try:
        tweet = Tweets.objects.get(pk=pk)
    except Tweets.DoesNotExist:
        raise Http404('Tweet Does not exist')
    return render(request,'backend/tweet_detail.html',{'tweet':tweet})

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('tweetList')
    
    return render(request,'backend/login.html',{})

def LogoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def CreateTweets(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweetList')
    context ={'form':form}
    return render(request,'backend/tweet_form.html',context)

def UserRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created')
            return redirect('tweetList')
    context = {'form':form}
    return render(request,'backend/register.html',context)
   