from .models import MenuCategory,MenuItem
from .serializers import MenuCategorySerializer,MenuItemSerializer,IngredientSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
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

class MenuItemIngredientView(RetrieveAPIView):
    serializer_class = IngredientSerializer
    def retrive(self,request,*args,**kwargs):
        menu_item = MenuItem.objects.get(pk = self.kwargs['pk'])
        ingredients = menu_item.ingredients.all()
        serializer = self.get_serializer(ingredients,many =True)
        return Response(serializer.data)

class MenuItemsByCategory(APIView):
    def get(self,request):
        category = request.query_params.get('category')
        if category:
            menu_items = MenuItem.objects.fileter(category__category_name__icontains = category)
        else:
            menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items,many = True)
        return Response(serializer.data)