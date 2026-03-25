from .models import MenuCategory,MenuItem,Table,ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer,MenuCategorySerializer,MenuItemSerializer,IngredientSerializer,TableSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .utils import send_custome_email

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

class TableDetailView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class AvailableTablesAPIView(ListAPIView):
    queryset = Table.objects.filter(is_avaliable =True)
    serializer = TableSerializer

class ContactFormSubmissionCreateView(generics.CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer

    def Create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"Contact Form Submitted Successfully.",
                    "data":serializer.data
                },status = status.HTTP_201_CEATED
            )
        return Response({
            "error":serializer.errors
        },status = status.HTTP_400_BAD_REQUEST
        )

def contact_view(request):
    if request.method == "POST":
        email_sent = send_custome_email(
            to_email = "akshatajadhav7902@gmail.com",
            subject  = "New Contact from Submission",
            message = "A user has submitted the contact form."
        )
        if email_sent:
            return Response({"message":"Email sent successfully."})
        else:
            return Response({"error":"Failed to send email"},status = status.HTTP_500_INTERNAL_SERVER_ERROR)