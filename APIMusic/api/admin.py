from django.contrib import admin
from api.models import Artist, Album, Band
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Band)