import string 
import secrets
from decimal Decimal,ROUND_HALF_UP 
# from django.apps import apps
from .models import Order
from django.db.models import Sum
import logging
from django.core.exceptions import ObjectDoesNotExist, ValidationError

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

def calculate_discount(amt):
    if amt >1000:
        return amt * 0.9
    return amt

ALLOWED_STATUSES = ['pending','processing','completed','cancelled']
def update_order_status(order_id,new_status):
    try:
        if new_status.lower() not in ALLOWED_STATUSES:
            raise ValidationError(f"Invalide status:{new_status}")
        order = Order.objects.get(id = order_id)
        old_status = order.status
        order.status = new_status.lower()
        order.save()
        logger.info(
            f:Order ID {order_id} status changed from '{old_status}'
        )
        return {
            "success":True,
            "message":f"Order status updated to '{new_status}'"
        }
    exceptions ObjectDoesNotExist:
        logger.error(f"Order with ID {order_id} not found.")
        return{
            "success":False,
            "message":"order not Found"
        }
    except ValidationError as ve:
        logger.warning(f"Validation error for ID {order_id}): {str(e)}")
        return{
            "success":False,
            "message":str(ve)
        }
    except Exception as e:
        logger.exception(f"Unexpected error while updating order {order_id}:{str(e)}")
        return {
            "success":False,
            "message":"an unexpected error occurred"
        }
