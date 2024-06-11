from django.shortcuts import render
from .import models
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializers, LikeSerializers, CommentSerializers
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action

class PostViewset(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    
        

class LikeViewset(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = LikeSerializers

    
class LikeAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Like.objects.all()
    serializer_class = LikeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    
        
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializers

class CommentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]    

