from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')  # Ensure you have a template at 'tweet/index.html'