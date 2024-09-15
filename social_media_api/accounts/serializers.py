from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=validate_password)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password", "bio", "profile_picture")
        extra_kwags = {
            "bio":{"required":False},
            "profile_picture":{"required":False},
        }

        def validate(self, attr):
            if attr["password"] != attr["password2"]:
                raise serializers.ValidationError({"password": "password field did not match"})
            return attr
        
        def create(self, validate_data):
            validate_data.pop("password2")
            user = User.objects.create_user(
                username=validate_data["username"],
                email=validate_data["emial"],
                password=validate_data["password"],
                bio=validate_data.get("bio", ""),
                profile_picture=validate_data.get("profile_picture", None)

            )
            return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "bio", "profile_profile"]
        extra_kwargs = {
            "username": {"read_only":True},
            "email": {"read_only":True},
        }
    

