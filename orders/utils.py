import string 
import secrets
from decimal Decimal,ROUND_HALF_UP 
# from django.apps import apps

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
          

