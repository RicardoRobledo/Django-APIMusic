"""APIMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('.urls')),
    path('albums/', include('apps.albums.routers')),
    path('bands/', include('apps.bands.routers')),
    path('artists/', include('apps.artists.routers')),
    #path('users/', include('.urls')),
    path('api-auth/', include('rest_framework.urls')), # authentification
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # endpoint for API 
]
