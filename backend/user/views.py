from django.contrib.auth import authenticate

from rest_framework import response, status, generics, permissions
from rest_framework_simplejwt import tokens

from .models import OTP
from .serializers import *
from .utils import sendToken


class LoginAPIView(generics.GenericAPIView):
    """
    An endpoint for users to request for OTP
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = [LoginSerializer]
    
    def post(self, request, *args, **kwargs):
        s = LoginSerializer(data=request.data)
        if s.is_valid():
            phone = s.validated_data["phone"]
            password = s.validated_data["password"]
            
            if authenticate(request=request, phone=phone, password=password):
                user = User.objects.get(phone=phone)
                otp = sendToken(user=user)
                OTP.objects.create(user=user, otp=otp).save()
                return response.Response(data=request.data, status=status.HTTP_202_ACCEPTED)
            else:
                return response.Response("User does not exist!", status=status.HTTP_404_NOT_FOUND)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class OTPLoginAPIView(generics.GenericAPIView):
    """
    An endpoint for users to evaluate their OTP token
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = [OTPSerializer]
    
    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.data)
        if s.is_valid():
            otp = s.validated_data["otp"]
            if OTP.objects.get(otp=otp):
                user_otp = OTP.objects.get(otp=otp)
                user = User.objects.get(phone=user_otp)
                token = tokens.RefreshToken.for_user(user)
                
                # set tokens for user
                
                return response.Response(s.data, status=status.HTTP_202_ACCEPTED)
            else:
                return response.Response("this otp is not valid!", status=status.HTTP_401_UNAUTHORIZED)
        else:
            return response.Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class LogoutAPIView(generics.GenericAPIView):
    """
    An endpoint for users to logout from system
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = tokens.RefreshToken(refresh_token)
            token.blacklist()
            return response.Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(generics.GenericAPIView):
    """
    An endpoint for users to register their account
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = [UserSerializer]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        sendToken(user=user)
        return response.Response(data=serializer, status=status.HTTP_200_OK)


class OTPActiveAccountAPIView(generics.GenericAPIView):
    """
    An endpoint to activate their account via OTP 
    """
    permission_classes = []
    serializer_class = [OTPSerializer]
    
    def post(self, request, *args, **kwargs):
        s = OTPSerializer(data=request.dcd fata)
        if s.is_valid():
            otp = s.validated_data["otp"]
            if OTP.objects.get(otp=otp):
                uo = OTP.objects.get(otp=otp)
        return response.Response() 


class ProfileAPIView(generics.GenericAPIView):
    """
    An endpoint for Users to their profiles
    """ 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [ProfileSerializer]
