from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, user_feed

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('feed/', user_feed, name='user_feed'),
]