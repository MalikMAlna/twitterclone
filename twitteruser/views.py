from django.views.generic.detail import DetailView
from .models import TwitterUser
from tweet.models import Tweet


class TwitterUserDetailView(DetailView):
    model = TwitterUser
    context_object_name = 'twitter_user'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['personal_tweets_count'] = Tweet.objects.all().count()
        return context
