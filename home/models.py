from django.db import models
from django.db.models import Count
from orders.models import Order

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    phone_number = models.IntergerField()
    operating_days = models.CharField(max_length = 50,help_text = "Enter days like Mon,Tue,Wed,Thu,Fri")
    def __str__(self):
        return f"{self.name}"

class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True,null = True)
    def __str__(self):
        return self.name  

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class MenuItemManager(models.Manager):
    def get_top_selling_items(self,num_items =5):
        return(self.get_queryset()
        .annotate(total_orders = Count('orderitem'))
        .order_by('-total_orders')[:num_items]
        )


class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank = True)   
    price = models.DecimalField(max_digits=8,decimal_places=2)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(MenuCategory,on_delete = models.CASCADE)
    objects = MenuItemManager()
    is_daily_special = models.BooleanField(default = False)
    def __str__(self): 
        return self.name   


class NutritionalInformation(models.Model):
    meun_item = models.ForeignKey(MenuItem,on_delete = models.CASCADE,related_name = 'nutritional_info')
    calories = models.IntergerField()
    protein_gram = models.DecimalField(max_digits=5,decimal_places =2)
    fat_grams = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate_grams = models.DecimalField(max_digits=5,decimal_places = 2)

    def __str__(self):
        return f"{self.menu_item.name} - {self.calories} Kcal"


class DailySpecialManager(models.Manager):
    def upcoming (self):
        today = datetime.date.today()
        return self.filter(date__gte = today)

class DailySpecial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    is_activate = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add = True)
    objects = DailySpecialManager()

    def __str__(self):
        return self.title

    @staticmethod
    def get_random_special():
        specials = DailySpecial.objects.filter(is_activate=True)
        if specials.exists():
            return specials.order_by('?').first()
        return None

class Table(models.Model):
    table_number = models.IntergerField()
    capacity = models.IntergerField()
    is_available =models.BooleanField(default=True)
    def __str__(self):
        return f"Table {self.table_number}"

class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=50,unique = True)
    points_required  = models.IntergerField(unique =True,help_text="Minimum loyalty points required to reach this tier")

    discount_percentage = models.DecimalField(max_length = 5
    ,decimal_places = 2,help_text = "Discount percentage for this tier")
    description = models.TextField()
    def __str__(self):
        return self.name


class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.name} - {self.email}"

class UserReview(models.Models):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'reviews')
    menu_item = models.ForeignKey(MenuItem,on_delete= models.CASCADE,related_name = "reviews")
    rating =models.IntergerField()
    comment = models.TextField(blank =True,null = True)
    review_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self..menu_item.name}({self.rating})"

    class Meta:
        unique_together = ('user','menu_item')
        ordering = ['-review_date']
        
             
