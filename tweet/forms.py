from django import forms


class AddTweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=140,
                           help_text="Limit: 140 characters max")
