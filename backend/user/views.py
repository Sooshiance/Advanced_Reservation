from django.contrib.auth import authenticate

from rest_framework import response, status, generics, permissions

from .serializers import *
from .permissions import *


class LoginAPIView(generics.GenericAPIView):
    pass


class OTPLoginAPIView(generics.GenericAPIView):
    pass


class RegisterAPIView(generics.GenericAPIView):
    pass


class OTPActiveAccountAPIView(generics.GenericAPIView):
    pass 
