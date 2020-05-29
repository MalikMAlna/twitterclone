from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notifications.models import Notification


@login_required
def index(request):
    # Referenced for correct use of order_by:
    # https://stackoverflow.com/
    # questions/9834038/
    # django-order-by-query-set-ascending-and-descending
    tweet_author = TwitterUser.objects.get(id=request.user.id)
    user_tweets = Tweet.objects.filter(user=request.user).order_by("-created")
    follower_tweets = Tweet.objects.filter(
        user__in=request.user.followers.all()).order_by("-created")
    # Referenced this with advice from Matt P.
    # https://stackoverflow.com/
    # questions/431628/
    # how-to-combine-two-or-more-querysets-in-a-django-view#434755
    my_tweets = user_tweets | follower_tweets
    # https://stackoverflow.com
    # /questions/431628
    # /how-to-combine-two-or-more-querysets-in-a-django-view#434755
    my_notifications_count = Notification.objects.filter(
        tweet_author=tweet_author, viewed=False).count()
    return render(request,
                  'authentication/index.html',
                  {"my_tweets": my_tweets,
                   "my_notifications_count": my_notifications_count}
                  )


def loginview(request):
    html = 'authentication/login.html'
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
        else:
            context['login_form'] = form
    else:
        form = LoginForm()
        context['login_form'] = form
    return render(request, html, context)


def logoutview(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse('homepage'))


def registration_view(request):
    html = 'authentication/register.html'
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(
                username=username,
                password=raw_password
            )
            login(request, account)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, html, context)
