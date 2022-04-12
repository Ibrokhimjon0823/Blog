from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter


class PostList(generics.ListCreateAPIView):
    """
             METHOD : GET, Create
             Endpoint to get List of posts with filtering 'title','tags','categories','created_at' as well as CREATE Post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

