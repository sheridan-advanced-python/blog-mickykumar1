from django.urls import reverse_lazy
import pytest


pytestmark = pytest.mark.django_db

URL = reverse_lazy('api:comment-list')


def test_url():
    assert URL == '/api/comments/'

def test_filtering_by_post(client):
    drf_post = mommy.make('blog.Post')
    comment = mommy.make('blog.Comment', post=drf_post)
    # Unrelated comment
    mommy.make('blog.Comment')

    response = client.get(URL, data={'post': drf_post.pk})

    # Compare the ID field
    expected_ids = [comment.pk]
    result_ids = [obj['id'] for obj in response.json()]

    assert expected_ids == result_ids

class CommentListCreateView(generics.ListAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        queryset = super().get_queryset()
        if post_id:
            # Cast value to integer
            post_id = int(post_id)
            queryset = queryset.filter(post_id=post_id)

        return queryset.order_by('-created')

def test_invalid_post_value(client):
    response = client.get(URL, data={'post': 'THIS IS NOT AN INT!'})
    assert response.status_code == 200
def get_queryset(self):
        post_id = self.request.query_params.get('post')
        queryset = super().get_queryset()
        if post_id and post_id.isdecimal():
            queryset = queryset.filter(post_id=int(post_id))

        return queryset.order_by('-created')
def test_post_new_comment(client):
    post = mommy.make('blog.Post')
    data = {
        'post': post.pk,
        'name': 'Babu Bhatt',
        'email': 'babu@dreamcafe.com',
        'text': 'This was a very good post. Very good.',
    }
    response = client.post(URL, data=data)
    assert response.status_code == 201
