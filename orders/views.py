from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from django.utils import timezone
from .models import Coupon,Order
from .serializers import OrderSerializer    

# Create your views here.

class CouponValidationView(APIView):
    def post(self,request):
        code = request.data.get('code')
        
        if not code:
            return Response(
                {"error":"Coupon code is required"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        coupon = Coupon.objects.filter(code__iexact=code).first()
        if not coupon:
            return Response(
                {"error": "Invalid coupon code."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        today = timezone.now().date()
        
        if not coupon.is_active:
            return Response(
                {"error":"Coupon is inactive"},
                status = status.HTTP_400_BAD_REQUEST
            )
            
        if not (coupon.valid_from <= today <= coupon.valid_until):
            return Response(
                {"error":"coupon is expired or not yet valid"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        return Response(
            {"message":"Coupon is valid",
             "discount_percentege":coupon.discount_percentage },
            status = status.HTTP_200_OK
        )
        
    
class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')  


class OrderGetView(APIView):
    def get(self,request,id):
        order = Order.objects.get(id = id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

from utils.email_utils import send_order_confirmation_email
def create_order(request):
    order = Order.objects.create(...)
    send_order_confirmation_email(order_id = order.id,
    customer_email = order.customer.email,
    customer_name = order.customer.name)

class UpdateOrderStatusView(APIView):
    def put(self,request,pk):
        try:
            order = Order.objects.get(pk = pk)
        except Order.DoesNotExist:
            return Response(
                {"error":"Order not found"},
                status = status.HTTP_400_NOT_FOUND
            )
        serializer = OrderSerializer(order,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"Order status updated successfully","data":serializer.data},
                status = status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
