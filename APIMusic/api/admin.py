from django.contrib import admin
from api.models import Artist, Album, Band


# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Band)