from django.urls import path
from .views import *
router = DefaultRouter()
router.register(r'orders',orderViewSet,basename = 'orders')
url0

urlpatterns = [
    path('coupons/validate/' ,CouponValidationView.as_view(),name='coupon-validate'),
    path('history/',OrderHistoryView.as_view(),name = 'order-history'),
    path('orders/<int:pk>/update-status/',UpdateOrderStatusView.as_view(),name = 'update-order-status'),
    path('payment-methods/',PaymentMethodListAPIView.as_view(),name = 'payment-methods'),


]