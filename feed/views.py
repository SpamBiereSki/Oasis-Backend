from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("pub_date")
    serializer_class = PostSerializer

    
