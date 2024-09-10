from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register, profile, PostListView, PostCreateView, PostDetailView, PostDelete, PostUpdateView

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("accounts/profile/", profile, name="profile"),
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>", PostDetailView.as_view, name="post-detail" ),
    path("post/new", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>", PostDelete.as_view(), name="post-delete"),

]