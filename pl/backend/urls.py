from django.urls import path
from . import views

urlpatterns = [
    path('tweetsList', views.list,name="tweetList"),
    path('tweetDetail/<int:pk>', views.details),
    path('createTweet/',views.CreateTweets,name="CreateTweet"),
]