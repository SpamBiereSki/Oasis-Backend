from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("pub_date")
    serializer_class = PostSerializer

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)