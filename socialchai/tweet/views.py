from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')  # Ensure you have a template at 'tweet/index.html'
  
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # Fetch all tweets ordered by creation date
    return render(request, 'tweet_list.html', {'tweets': tweets})
  
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
    
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user = request.user)  
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list') 
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})  