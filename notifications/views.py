from django.shortcuts import render
from django.http import HttpResponseRedirect
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notifications.models import Notification


def show_notifications(request, id):
    html = 'notifications/notifications.html'
    tweet_author = TwitterUser.objects.get(id=id)
    notifications = Notification.objects.filter(tweet_author=tweet_author)

    for notification in notifications:
        notification.viewed = True
        notification.save()

    return render(request, html, {"notifications": notifications})
