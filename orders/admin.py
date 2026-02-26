from django.contrib import admin
from .models import Coupon,OrderStatus,Order

# Register your models here.
admin.site.register(Coupon)
admin.site.register(OrderStatus)
admin.site.register(Order)