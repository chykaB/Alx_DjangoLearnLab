from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"book_all", BookViewSet, basename="book_all"),

urlpatterns = [
    path("booklist", BookList.as_view(), name="booklist"), 
    path("", include(router.urls)),
]