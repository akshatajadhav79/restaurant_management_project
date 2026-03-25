from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from decimal import Decimal
from home.models import MenuItem
from orders.models import Order,orderItem

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'testuser')
        self.menu1 = MenuItem.objects.create(name = 'pizza',price = Decimal('200.00'))
        self.menu2 = MenuItem.objects.create(name = 'Burger',price = Decimal('300.00'))

        self.order = Order.objects.create(user = self.user)
        OrderItem.objects.create(
            order = self.order,
            menu_item = self.menu1,
            quantity = 2,
            price = Decimal('200.00')
        )

        OrderItem.objects.create(order = self.menu2,menu_item = self.menu2,price = Decimal('100.00'))

        def test_calculate_total(self):
            total = self.order.calculate_total()
            self.assertEqual(total,Decimal('500.00'))
