from django.contrib import admin
from .models import Coupon,OrderStatus

# Register your models here.
admin.site.register(Coupon)
admin.site.register(OrderStatus)