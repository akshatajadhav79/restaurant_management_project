from django.contrib import admin
from .models import MenuCategory,Restaurant,MenuItem

# Register your models here.

admin.site.register(MenuCategory)
admin.site.register(MenuItem)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','phone_number','email','is_active')

admin.site.register(Restaurant,RestaurantAdmin)