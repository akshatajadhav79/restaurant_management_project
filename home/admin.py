from django.contrib import admin
from .models import MenuCategory,Restaurant,MenuItem

# Register your models here.

admin.site.register(MenuCategory)
admin.site.register(MenuItem)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_delivery')