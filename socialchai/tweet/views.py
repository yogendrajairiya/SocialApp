from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tweet, Comment, Profile, Like
from .forms import TweetForm, UserRegistrationForm, UserForm,  ProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType

# Create your views here.
def index(request):
    return render(request, 'index.html')  # Ensure you have a template at 'tweet/index.html'

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')

    liked_tweet_ids = []
    if request.user.is_authenticated:
        tweet_type = ContentType.objects.get_for_model(Tweet)
        liked_tweet_ids = Like.objects.filter(
            user=request.user,
            content_type=tweet_type
        ).values_list('object_id', flat=True)

    return render(request, 'tweets/tweet_list.html', {
        'tweets': tweets,
        'liked_tweet_ids': liked_tweet_ids
    })

@login_required  # Ensure that only logged-in users can create tweets
def tweet_create(request):
  if request.method == 'POST':
      form = TweetForm(request.POST, request.FILES)  # Handle file uploads
      if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user  # Associate the tweet with the logged-in user
          tweet.save()
          return redirect('tweet_list')  
  else:
      form = TweetForm()
  
  return render(request, 'tweet_form.html', {'form': form})  # Render the form for creating a new tweet

@login_required  
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if tweet.user != request.user:
        return HttpResponse("You are not allowed to edit this tweet.", status=403)  # Check if the user is the owner of the tweet
    if request.method == 'POST':
      form = TweetForm(request.POST, request.FILES, instance=tweet)  # Handle file uploads
      if form.is_valid():
          form.save()
          return redirect('tweet_list')  # Redirect to the tweet list after editing
    else:
      form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})  

@login_required   
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user = request.user)  
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list') 
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})  # Render the registration form

def tweet_comments(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = tweet.comments.all().order_by('-created_at')  # Fetch comments related to the tweet
    if request.method == 'POST':
        text = request.POST.get('text')
        attached_photo = request.FILES.get('attached_photo')
        if text:  # Ensure that the comment text is not empty
            comment = Comment(tweet=tweet, user=request.user, text=text, attached_photo=attached_photo)
            comment.save()
            return redirect('tweet_comments', tweet_id=tweet.id)  # Redirect to the same tweet's comments page
    return render(request, 'tweet_comments.html', {'tweet': tweet, 'comments': comments})  # Render the comments page

@login_required
def profile_view(request):
    profile = request.user.profile
    tweet_count = Tweet.objects.filter(user=request.user).count()
    return render(request, 'profile.html', {
        'profile': profile,
        'tweet_count': tweet_count
    })


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_view')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)


    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def toggle_like(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    content_type = ContentType.objects.get_for_model(tweet)
    like, created = Like.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=tweet.id
    )

    if not created:
        like.delete()  # User already liked, so unlike
    return redirect('tweet_list')