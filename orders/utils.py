import string 
import secrets
from decimal Decimal,ROUND_HALF_UP 
# from django.apps import apps
from .models import Order
from django.db.models import Sum

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits
    
    while True: 
        code = ''.join(secrets.choice(characters) for _ in range(length)) 
        if not Coupon.objects.filter(code = code).exists():
            return code

def calculate_tip_amount(order_total,tip_precentage):
    order_total  = Decimal(str(order_total))
    tip_precentage = Decimal(str(tip_precentage))
    tip_amount = order_total * (tip_precentage/Decimal("100"))
    return tip_amount.quantize(Decimal("0.01"),rounding = ROUND_HALF_UP)
          
def get_daily_sales_total(date):
    orders = Order.objects.filter(created_at__date = date)
    total = orders.aggregate(total_sum = Sum('total_price'))['total_sum']
    return total if total is not None else Decimal('0.00')


def generate_unique_order_id(length=8):
    Order = apps.get_model('orders','Order')
    characters = string.ascii_uppercase + string.digits
    if not Order.objects.filter(order_id = order_id).exists():
        return order_id