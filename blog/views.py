from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from . import models


class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.published() \
            .order_by('-published')[:3]

        context.update({'latest_posts': latest_posts})

        return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'
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

 class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')

class PostDetailView(DetailView):
    model = models.Post

    def get_queryset(self):
        # Get the base queryset
        queryset = super().get_queryset().published()
                # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )
