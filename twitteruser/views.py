from .models import TwitterUser
from tweet.models import Tweet
from django.views import View
from django.shortcuts import render


class TwitterUserDetailView(View):
    html = "twitteruser/twitteruser_detail.html"

    def get(self, request, pk):
        author = TwitterUser.objects.get(pk=pk)

        personal_tweet_count = Tweet.objects.filter(
            user=author).count()
        return render(request,
                      self.html,
                      {"author": author,
                       "personal_tweet_count": personal_tweet_count})
