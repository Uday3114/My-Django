from django.contrib import admin
from .models import UserProfile, Messages, Friends

# Register your models here.

admin.site.register(Messages)
admin.site.register(Friends)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'username']