
from rest_framework import serializers
from .models import MenuCategory,MenuItem,Ingredient,Table,ContactFormSubmission

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        field="__all__"
        

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        field = "__all__"

class IngridentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient 
        fields = ['id','name']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"
    
class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields=['id','name','email','message','created_at']
        def validation_name(self,val):
            if len(val)<2:
                raise serializers.ValidationError("Name must be at least 2 characterlong.")
            return value

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','name','description','price']