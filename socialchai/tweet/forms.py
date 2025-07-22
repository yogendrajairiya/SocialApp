from django import forms
from .models import Tweet, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        
class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
  
  def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio', 'location', 'birthdate', 'phone', 'address']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        } 