from rest_framework import serializers
from .models import PostsModel
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsModel
        fields = ["id","created_by", "image", "posted_date", "title", "content"]