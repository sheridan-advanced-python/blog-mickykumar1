from django.shortcuts import render

# Create your views here.

def home(request):
    """
    The Blog homepage
    """
    # Get last 10 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:10]
    authors = models.Post.objects.get_authors()
    get_posts = models.Post.objects.return_10_post_with_the_most_comments()[:10]
    get_topics = models.Topic.objects.return_10_topics_with_the_most_post()[:10]

    context = {
        'authors': authors,
        'latest_posts': latest_posts
        'get_posts': get_posts,
        'get_topics': get_topics
    }

    return render(request, 'blog/home.html', context)

def terms_and_conditions(request):
   return render(request, 'blog/terms_and_conditions.html')
