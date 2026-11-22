from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import RegisterSerializers, LoginSerializer, RefreshSerializer, LogoutSerializer

from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class RegistarView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {'error': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })

class RefreshView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RefreshSerializer
    
    def post(self,request):
        serializer = RefreshSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        token = serializer.validated_data['refresh']
        
        try:
            refresh = RefreshToken(token)
            return Response({'access':str(refresh.access_token)})
        
        except TokenError:
            return Response(
                {'error': 'Invalid or expired refresh token'},
                status=status.HTTP_401_UNAUTHORIZED)
            
class LogoutView(APIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data['refresh']
        try:
            refresh = RefreshToken(token)
            if refresh['user_id'] != request.user.id:
                return Response({'error': 'This token does not belong to you'},status=status.HTTP_403_FORBIDDEN)

            refresh.blacklist()
            return Response({'message': 'Logged out successfully'},status=status.HTTP_200_OK)

        except TokenError:
            return Response({'error': 'Invalid or expired refresh token'},status=status.HTTP_400_BAD_REQUEST)
            
        
