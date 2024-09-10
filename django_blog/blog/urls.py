from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    register, 
    profile, 
    PostListView, 
    PostCreateView, 
    PostDetailView, 
    PostDelete, 
    PostUpdateView, 
    add_comment,
    CommentUpdateView, 
    CommentDeletView,
)

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("accounts/profile/", profile, name="profile"),
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>", PostDetailView.as_view, name="post-detail" ),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDelete.as_view(), name="post-delete"),

    path("posts/<int:post_id>,comments/new/", add_comment, name="comments-new"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("comments/<int:pk>/delete/", CommentDeletView.as_view(), name="comment-delete"),

]