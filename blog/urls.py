from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('blog', views.Blog.as_view()),
    path('blog/post', views.Post.as_view()),
    path('blog/<int:pk>', views.ViewPost.as_view()),
    path('blog/update/<int:pk>', views.UpdatePost.as_view()),
    path('blog/delete/<int:pk>', views.DeletePost.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]