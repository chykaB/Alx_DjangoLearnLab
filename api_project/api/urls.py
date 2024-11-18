from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"book_all", BookViewSet, basename="book_all"),

urlpatterns = [
    path("booklist", BookList.as_view(), name="booklist"), 
    path("auth_token", obtain_auth_token, name="auth_token"),
    path("", include(router.urls)),
]