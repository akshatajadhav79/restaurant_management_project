from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',MenuCategoryViewSet,basename = 'categories')

urlpatterns = [
    path("cat",include(router.urls)),
    path('categories/' ,MenuCategoryListView.as_view(),name = 'menu-category-list') ,
    path('menu/featured/',FeaturedMenuItemListView.as_view(),name = 'featured-menu'), 
    path('menu-items',MenuItemViewSet.as_view(),name = 'menu-items'),
    path("api/menu-items/<int:pk>/ingredients/",MenuItemIngredientsView.as_view(),name='menu-item-ingredients'),
    path('menu-items/',MenuItemsByCAtegory.as_view(),name = 'menu-items-by-category'),
    path('api/tables/<int:pk>/',TableDetailView.as_view(),name = "table_detail"),
    path("avaliable-tables/",AvalibleTablesAPIView.as_view(),name ="available_tables"),
    path("contact/",ContactFormSubmissionCreateView.as_view(),name = "contact-form"),
    path("daily-specials/",DailySpecialsView.as_view(),name ="daily-specials")
]