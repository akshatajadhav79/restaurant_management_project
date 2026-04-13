
from rest_framework import serializers
from .models import Restaurant,MenuCategory,MenuItem,Ingredient,Table,ContactFormSubmission,UserReview

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

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['id','user','menu_item','rating','comment']
        read_only_fields = ['user']

        def validate_rating(self,value):
            if value <1 or value >5:
                raise serializers.ValidationError("Rating must  be between 1 and 5")
            return value
    
class MenuItemAvailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','is_available']

class RestaurantSerializer(serializers.ModelSerializer):
    operating_hours = DailyOperatingHoursSerializer(many=True,read_only = True)
    class Meta:
        model = 'Restaurant'
        fields = "__all__"

class MenuItemSearchSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = MenuItem
        fields = ["name","image_url"]

    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None