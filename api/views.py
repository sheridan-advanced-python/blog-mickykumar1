from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from . import serializers

@api_view(['GET'])
def index(request):
    return Response()

class PostListView(generics.ListAPIView):
    """
    Returns a list of published posts
    """
    serializer_class = serializers.PostListSerializer
    queryset = Post.objects.published()

class PostDetailView(generics.RetrieveAPIView):
    """
    Returns post details
    """
    serializer_class = serializers.PostDetailSerializer
    queryset = Post.objects.published()

class CommentListCreateView(generics.ListAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all().order_by('-created')

class CommentListCreateView(generics.ListCreateAPIView):
