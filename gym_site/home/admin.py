from django.contrib import admin

from home.models import Setting, UserProfile

# Register your models here.

admin.site.register(Setting)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

admin.site.register(UserProfile, UserProfileAdmin)