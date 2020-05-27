from django import forms


class AddTweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=140)
