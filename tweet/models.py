from django.db import models
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
