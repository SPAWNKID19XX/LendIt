from django.contrib import admin
from .models import Category, Item


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    filds = ('name', 'slug')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', "owner", "category", "price")
    filds =  ('title','description', "owner", "category", "city", "price")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
