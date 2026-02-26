from os import name
from pyexpat import model

from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from  = models.DateField()
    valid_until =models.DateField()
    
    def __str__(self):
        return f'{self.code} - {self.discount_percentage}%'
    
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True,blank=True)
    def __str__(self):
        return f"Order{self.id}"
    
    
        