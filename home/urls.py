from django.urls import path
from .views import *

urlpatterns = [
    path('categories/' ,MenuCategoryListView.as_view(),name = 'menu-category-list') ,
    path('menu/featured/',FeaturedMenuItemListView.as_view(),name = 'featured-menu'), 
    path('menu-items',)

]