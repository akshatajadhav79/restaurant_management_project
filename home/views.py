from .models import MenuCategory,MenuItem
from .serializers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.generics import ListAPIView
from rest_framework import generics

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class FeaturedMenuItemListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        return MenuItem.objects.filter(is_featured = True)
    
