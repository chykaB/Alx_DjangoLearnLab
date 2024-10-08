from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r"book", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
]


