from .models import Post, Comment
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.http import Http404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("created")
    serializer_class = PostSerializer

    def retrieve(self, request, pk = None, format=None):
        # If only one post, we return the 3 first comments
        pk = int(pk)
        if pk is not None and type(pk) is int:
            post = self.queryset.get(pk=pk)
            serializer = self.serializer_class(post, context={'request': request})
            comments = Comment.objects.filter(idpost=pk)[0:3]
            comment_serializer = CommentSerializer(comments, many=True, context={'request': request})
            ser_comments = comment_serializer.data
            data = serializer.data
            data["comments"] = ser_comments
            return Response(data)
        serializer = self.serializer_class(self.queryset, many= True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=["GET"], detail=True)
    def comments(self, request, pk=None, format=None):
        if pk is None:
            return Http404
        comments = Comment.objects.filter(idpost=pk)
        comment_serializer = CommentSerializer(comments, many=True)
        return Response(comment_serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("created")
    serializer_class = CommentSerializer

    def retrieve(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

