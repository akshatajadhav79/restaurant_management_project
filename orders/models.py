from django.db import models
from orders.utils import generate_coupon_code

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

class OrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in =['pending','processing'])
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),('processing','Processsing'),
        ('completed','Completed'),('canceled','Canceled')
    ]
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Ostatus = models.ForeignKey(OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(max_length = 20,choices = STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=5,decimal_places = 2)
    objects = OrderManager()

    def save(self,*args,**kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        super().save(*args,**kwargs)

    def get_unique_item_names(self):
        unique_items = set()
        for ord_i in self.orderitem_set.all():
            unique_items.add(ord_i.menu_item.name)
        return list(unique_items)

    def __str__(self):
        return f"Order {self.id}"