from django.contrib import admin
from main.models import *
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
	list_items = ("name", "price", )

class CategoryAdmin(admin.ModelAdmin):
	list_items = ("id", "name", )

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
