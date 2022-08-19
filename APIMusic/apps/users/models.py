from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# ------------------------------------------
#                   User
# ------------------------------------------


class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, password, name, is_staff=False, is_superuser=False):
        
        user = self.model(
            username=username,
            email=email,
            name=name,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password) # encrypt password
        user.save(using=self._db)
        
        return user


    def create_superuser(self, username, email, password, name):
        return self.create_user(username, email, password, name, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=150, unique=True,)
    name = models.CharField(max_length=150,)
    email = models.EmailField(blank=False,)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    created_at = models.DateTimeField(auto_now_add=True,)

    objects = CustomUserManager()
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name',]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    def __str__(self) -> str:
        return f'{self.username}'
