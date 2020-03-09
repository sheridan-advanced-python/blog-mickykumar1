from django.shortcuts import render

# Create your views here.

def home(request):
    """
    The Blog homepage
    """
    # Get last 10 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:10]
    # Add as context variable "latest_posts"
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/home.html', {'message': 'Hello world!'})
