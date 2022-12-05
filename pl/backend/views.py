from django.shortcuts import render, redirect
from .models import Tweets
from django.http import Http404
from .forms import TweetForm
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

def CreateTweets(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweetList')
    context ={'form':form}
    return render(request,'backend/tweet_form.html',context)