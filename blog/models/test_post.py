#test_post.py

def test_get_authors_returns_users_who_have_authored_a_post(django_user_model):
    # Create a user
    author = mommy.make(django_user_model)
    # Create a post that is authored by the user
    mommy.make('blog.Post', author=author)
    # Create another user – but this one won't have any posts
    mommy.make(django_user_model)

    assert list(Post.objects.get_authors()) == [author]


def test_get_authors_returns_unique_users(django_user_model):
    # Create a user
    author = mommy.make(django_user_model)
    # Create multiple posts. The _quantity argument can be used
    # to specify how many objects to create.
    mommy.make('blog.Post', author=author, _quantity=3)

    assert list(Post.objects.get_authors()) == [author]


def test_get_absolute_url_for_post_with_published_date():
    post = mommy.make(
        'blog.Post',
        published=dt.datetime(2014, 12, 20, tzinfo=dt.timezone.utc),
        slug='model-instances',
    )
    assert post.get_absolute_url() == '/posts/2014/12/20/model-instances/'


def test_get_absolute_url_for_post_without_published_date_or_slug():
    post = mommy.make(
        'blog.Post',
        published=None,
    )

    assert post.get_absolute_url() == f'/posts/{post.pk}/'
