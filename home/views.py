from ast import List

from django.shortcuts import render
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
