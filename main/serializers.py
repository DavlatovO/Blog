from rest_framework import serializers
from .import models

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['title', 'text', 'author', 'image', 'created_at']

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = ['is_like', 'user', 'post']   

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['user', 'post']          