from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet)
    tweet_author = models.ForeignKey(TwitterUser)
