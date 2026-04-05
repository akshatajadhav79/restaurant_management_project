from django.urls import path
from .views import *

urlpatterns = [
    path('coupons/validate/' ,CouponValidationView.as_view(),name='coupon-validate'),
    path('history/',OrderHistoryView.as_view(),name = 'order-history'),
    path('orders/<int:pk>/update-status/',UpdateOrderStatusView.as_view(),name = 'update-order-status'),
    path('payment-methods/',PaymentMethodListAPIView.as_view(),name = 'payment-methods'),
    path('orders/<int:pk>/cancel/',CancelOrderView.as_view(),name ='cancel-order'),
    path("order-status/<int:order_id>/",get_order_sta)

]