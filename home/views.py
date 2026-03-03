from .models import MenuCategory,MenuItem
from .serializers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class FeaturedMenuItemListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    def get_queryset(self):
        return MenuItem.objects.filter(is_featured = True)
    
class MenuItemPagiantion(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = MenuItemPagiantion

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains = search_query)
        return queryset