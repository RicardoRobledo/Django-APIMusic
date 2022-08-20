from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'name', 'created_at')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'created_at': instance.created_at,
        }


class UserUpdateSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'name',)
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
        }
