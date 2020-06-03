"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
# For page structuring:
# https://github.com/itsthejoker/
# templatedemo-sharedfolder/blob/master/template_test/urls.py

from authentication import views as auth_views
from notifications import views as notif_views
from tweet import views as tweet_views
from twitteruser import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.index, name="homepage"),
    path('login/', auth_views.loginview, name='login-page'),
    path('logout/', auth_views.logoutview, name='logout'),
    path('register/', auth_views.RegistrationFormView.as_view(), name='register'),
    path('tweet-add/', tweet_views.tweetadd, name='tweet-add'),
    path('show-notifications/',
         login_required(notif_views.ShowNotificationsView.as_view()),
         name="show-notifications"),
    path('twitter-user/<int:pk>',
         user_views.TwitterUserDetailView.as_view(),
         name='user-detail'
         ),
    path('tweet/<int:pk>',
         tweet_views.TweetDetailView.as_view(),
         name='tweet-detail'
         ),
    path('follow-user/<int:user_pk>',
         user_views.follow_user,
         name='follow-user'
         ),
    path('unfollow-user/<int:user_pk>',
         user_views.unfollow_user,
         name='unfollow-user'
         ),
]
