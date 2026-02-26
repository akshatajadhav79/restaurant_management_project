from dataclasses import field
from pyexpat import model

from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        field=['name']