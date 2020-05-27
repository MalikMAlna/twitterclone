from django.db import models
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
