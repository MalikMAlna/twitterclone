from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import AddTweetForm
from .models import Tweet
from twitteruser.models import TwitterUser
from notifications.models import Notification
import re


class TweetDetailView(DetailView):
    model = Tweet
    context_object_name = 'tweet'


@login_required
def tweetadd(request):
    html = 'tweet/tweetform.html'
    form = AddTweetForm()
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                text=data['text'],
                user=request.user
            )
# Modified this for current regex
# https://stackoverflow.com/questions/2304632/regex-for-twitter-username
# Also referenced this for regex:
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html
        text_list = re.findall(r'@([A-Za-z]+[A-Za-z0-9-_]+)', data['text'])
        if "@" in data['text']:
            for t_user in text_list:
                Notification.objects.create(
                    tweet=new_tweet,
                    tweet_author=TwitterUser.objects.get(username=t_user)
                )
        messages.info(request, "Tweet created successfully!")
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {"form": form})
