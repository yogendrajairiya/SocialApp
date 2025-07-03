from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
  class Meta:
    model = Tweet
    fields = ['text', 'image']  # fields to be displayed in the form
    