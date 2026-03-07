from django.contrib import admin
from .models import Coupon,OrderStatus,Order

# Register your models here.
admin.site.register(Coupon)
admin.site.register(OrderStatus)
admin.site.register(Order)

def mark_orders_processed(modeladmin,request,queryset):
    queryset.update(status = 'Processed')

mark_orders_processed.short_description = "Mark selected orders as Processed"

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','status','created_at')
    actions = [mark_orders_processed]

admin.site.register(Order,OrderAdmin)