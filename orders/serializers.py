from rest_framework import serializers
from .models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['menu_item_name','quantity','price']
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_price','unique_items','user' ]

        def validate_status(self,value):
            valid_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
            if value not valid_statuses:
                raise serializers.ValidationError("Invalid status provided.")
            return value