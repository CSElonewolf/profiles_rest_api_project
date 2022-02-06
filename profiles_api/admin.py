from django.contrib import admin
from .models import UserProfile,ProfileFeedItem
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
	""" Prevent the hashed password from being edited"""
	readonly_fields = ('password',)

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(ProfileFeedItem)