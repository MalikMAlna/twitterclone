from django.shortcuts import render
from notifications.models import Notification
from django.contrib.auth.decorators import login_required


@login_required
def show_notifications(request):
    html = 'notifications/notifications.html'
    notifications = Notification.objects.filter(tweet_author=request.user)

    rendered = render(request, html, {"notifications": notifications})

    for notification in notifications:
        notification.viewed = True
        notification.save()
    return rendered
