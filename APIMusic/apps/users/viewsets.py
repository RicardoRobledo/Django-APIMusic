from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


__author__ = 'Ricardo'
__version__ = '0.1'


class UserViewSet(ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
