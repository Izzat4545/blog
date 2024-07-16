from django.contrib import admin
from .models import PostsModel
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ["title", "created_by", "posted_date"]

admin.site.register(PostsModel, PostsAdmin)