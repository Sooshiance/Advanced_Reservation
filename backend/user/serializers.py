from rest_framework import serializers

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for user registering
    """
    class Meta:
        model = User 
        fields = ["id", "email", "phone", "password", "first_name", "last_name"]


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for users to see their profile
    """
    class Meta:
        model = Profile
        fields = ["id", "user", "phone", "email", "first_name", "last_name"]


class LoginSerializer(serializers.Serializer):
    """
    Serializer class for Login functionalities
    """
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class OTPSerializer(serializers.Serializer):
    """
    Serializer class for OTP functionalities
    """
    otp = serializers.CharField(required=True)
