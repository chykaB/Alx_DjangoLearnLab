from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user =serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": RegisterSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *arg, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username,
        })
    
class UserProfileView(generics.RetrieveAPIView):
    query_set = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    request.user.following.add(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)



