from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:pk>/',UserProfileViewSet.as_view({'put':'update'}),name = 'update-profile'),
    
]