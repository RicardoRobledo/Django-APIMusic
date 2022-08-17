from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from ..users.serializers import UserSerializer

from apps.users.models import User


__author__ = 'Ricardo'
__version__ = '0.1'


class LoginView(TokenObtainPairView):
    """
    This class allow us do a login
    """
    
    serializer_class = TokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        """
        Allow us login
        
        :param username: username of our user
        :param password: password of our user
        """
        
        login_serializer = self.serializer_class(data=request.data)
        
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        
        if login_serializer.is_valid():
            login(request, user)

        return Response(login_serializer.validated_data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
    This class allow us logout
    """

    def get(self, request, *args, **kwargs):
        """
        Allow us logout
        
        :param username: username
        """
        

        user = User.objects.get(username=request.data.get('username'))
        
        if user:
            logout(request)
        
        return Response({'message':'logout success'}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    
    permission_classes = ()
    
    def post(self, request, *args, **kwargs):
        """
        Allow us register
        
        :param username: username
        """
        
        
        message = None
        user_serializer = UserSerializer(data=request.data)
        
        user = User.objects.filter(
            Q(email=request.data['email']) | Q(username=request.data['username'])
        )
        
        if user:
            message = {'message': 'Existing username or email'}
        
        elif user_serializer.is_valid():
            user_serializer.save()
            message = {'message':'user created'}
        
        else:
            message = {'message':'wrong record'}
            
        
        return Response(message, status=status.HTTP_200_OK)
