from django.contrib import admin
from .models import ProfileModel

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProfileModel, ProfileAdmin)

