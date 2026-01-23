from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    field = ["__all__"]
    list_display = ('email','first_name','last_name')

admin.site.register(CustomUser, CustomUserAdmin)

