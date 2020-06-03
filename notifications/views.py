from django.shortcuts import render
from notifications.models import Notification
from django.views import View


class ShowNotificationsView(View):
    html = 'notifications/notifications.html'

    def get(self, request):
        notifications = Notification.objects.filter(tweet_author=request.user)

        rendered = render(request, self.html, {"notifications": notifications})

        for notification in notifications:
            notification.viewed = True
            notification.save()
        return rendered
