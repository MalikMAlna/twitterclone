from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import TwitterUser
from tweet.models import Tweet
from django.views import View
from django.contrib.auth.decorators import login_required


# Referenced this from Matt P.'s advice for views:
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/
class TwitterUserDetailView(View):
    html = "twitteruser/twitteruser_detail.html"

    def get(self, request, pk):
        author = TwitterUser.objects.get(pk=pk)
        self_user = TwitterUser.objects.get(username=request.user)
        personal_tweet_count = Tweet.objects.filter(
            user=author).count()
        users_followed_count = self_user.followers.all().count()
        return render(request,
                      self.html,
                      {"author": author,
                       "personal_tweet_count": personal_tweet_count,
                       "users_followed_count": users_followed_count})

# Referenced this from Matt P.'s advice
# for following functionality:
# https://docs.djangoproject.com/en/3.0/ref/models/relations/


@login_required
def follow_user(request, user_pk):
    user_to_follow = TwitterUser.objects.get(pk=user_pk)
    self_user = TwitterUser.objects.get(username=request.user)

    self_user.followers.add(user_to_follow)

    return HttpResponseRedirect(
        reverse('user-detail', args=(user_pk,))
    )


@login_required
def unfollow_user(request, user_pk):
    user_to_follow = TwitterUser.objects.get(pk=user_pk)
    self_user = TwitterUser.objects.get(username=request.user)

    self_user.followers.remove(user_to_follow)

    return HttpResponseRedirect(
        reverse('user-detail', args=(user_pk,))
    )
