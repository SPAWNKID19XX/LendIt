from django.contrib import admin
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    filds = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)
