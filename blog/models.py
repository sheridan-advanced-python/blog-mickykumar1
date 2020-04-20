
from django.conf import settings  # Imports Django's loaded settings
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
39
# Create your models here.
class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    content = RichTextUploadingField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each savenote
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_posts',  # "This" on the user model
        null=False
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible'
    )

    class Meta:
        """sorting the posts in reverse"""
        # Sort by the `created` field. The `-` prefix
        # specifies to order in descending/reverse order.
        # Otherwise, it will be in ascending order.
        ordering = ['-created']

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        if self.published:
            kwargs = {
                'year': self.published.year,
                'month': self.published.month,
                'day': self.published.day,
                'slug': self.slug
            }
        else:
            kwargs = {'pk': self.pk}

        return reverse('post-detail', kwargs=kwargs)
     banner = models.ImageField(
            blank=True,
            null=True,
            help_text='A banner image for the post'
        )

class Comment(models.Model):
    """
    Represents a comments section
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    text = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    def __str__(self):
        return self.name

class PostQuerySet(models.QuerySet):
    # ...
    def get_authors(self):
        User = get_user_model()
        return User.objects.filter(blog_posts__in=self).distinct()

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted']

    def __str__(self):
        return f'{self.submitted.date()}: {self.email}'


class contest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.ImageField(
        blank=True,
        null=True,
        help_text='Upload your picture'
    )
    photo_submitted = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-photo_submitted']
    def __str__(self):
        return f'{self.photo_submitted.date()}: {self.email}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    approved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CommentQuerySet.as_manager()

    def __str__(self):
        return f'{self.name} re: {self.post}'

    class Meta:
        ordering = ['-created']
