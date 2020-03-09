from django.shortcuts import render

# Create your views here.

def home(request):
    """
    The Blog homepage
    """
    # Get last 10 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:10]
    authors = models.Post.objects.get_authors()

    context = {
        'authors': authors,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/home.html', context)
