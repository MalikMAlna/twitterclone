from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddTweetForm
from .models import Tweet


@login_required
def tweetadd(request):
    html = 'tweet/tweetform.html'
    form = AddTweetForm()
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                text=data['text'],
                user=request.user
            )
            messages.info(request, "Tweet created successfully!")
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {"form": form})
