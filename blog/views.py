from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostsSerializer
from .models import PostsModel
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.exceptions import PermissionDenied


# Create your views here.
class Blog(generics.ListAPIView):
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()

class Post(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()
    parser_classes = [FormParser, MultiPartParser]
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
    
class ViewPost(generics.RetrieveAPIView):
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()

class UpdatePost(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()
    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj.created_by:
            raise PermissionDenied()
        return obj
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

class DeletePost(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostsSerializer
    queryset = PostsModel.objects.all()
    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj.created_by:
            raise PermissionDenied()
        return obj
