from pyexpat import model

from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name  
    
class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank = True)   
    price = models.DecimalField(max_digits=8,decimal_places=2)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self): 
        return self.name