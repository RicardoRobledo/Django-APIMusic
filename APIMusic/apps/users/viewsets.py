from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import User
from .serializers import UserSerializer, UserUpdateSerializer


__author__ = 'Ricardo'
__version__ = '0.1'


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="""
    list our users
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="""
    get a user

    :param id: id of our user.
    """
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="""
    create a user

    :param username: username of our user.
    :param name: name of our user.
    :param email: email of our user.
    """
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    update a user

    :param username: username of our user.
    :param name: name of our user.
    :param email: email of our user.
    """
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="""
    update a user

    :param username: username of our user.
    :param name: name of our user.
    :param email: email of our user.
    """
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="""
    eliminate a user

    :param id: id of a user.
    """
))
class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    
    def get_serializer_class(self):
        
        if self.action=='update':
            self.serializer_class = UserUpdateSerializer
        else:
            self.serializer_class = UserSerializer
        return self.serializer_class
