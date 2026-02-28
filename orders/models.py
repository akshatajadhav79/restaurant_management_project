from pyexpat import model

from django.db import models
from orders.utils import generate_coupon_code
from django.contrib.auth.models import User


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from  = models.DateField()
    valid_until =models.DateField()
    
    def save(self,*args,**kwargs):
        if not self.code:
            self.code = generate_coupon_code()
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f'{self.code} - {self.discount_percentage}%'
    
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    
    def __str__(self): 
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    status = models.ForeignKey(OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return f"Order {self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    menu_item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    
    def __str__(self):
        return self.menu_item_name