from django.shortcuts import render
from django.views.generic import DetailView, CreateView, FormView, ListView
from django.urls import reverse_lazy
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



class FormViewExample(FormView):
    template_name = 'blog/form_example.html'
    form_class = forms.ExampleSignupForm
    success_url = reverse_lazy('home')


class ContactFormView(CreateView):
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)

class contestFormView(CreateView):
    model = models.contest
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'image',
    ]

    def upload_pic(self, request):
        if request.method == 'POST':
            form = photo_contest_form(request.POST, request.FILES)
            if form.is_valid():
                m = photo_contest.objects.get(pk=course_id)
                m.model_pic = form.cleaned_data['image']
                m.save()
                return HttpResponse('image upload success')
        return HttpResponseForbidden('allowed only via POST')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your image for the contest has been submitted.'
        )
        return super().form_valid(form)
