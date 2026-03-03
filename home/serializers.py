from dataclasses import field
from pyexpat import model

from rest_framework import serializers
from .models import MenuCategory,MenuItem

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        field=['name']
        

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        field = "__all__"

     
    

