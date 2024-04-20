from django.urls import path
from .views import FoodListApi, FoodDetailApi, UserFoodListApi


urlpatterns = [
    path('food_list', FoodListApi.as_view(), name='food-list-api'),
    path('food/<int:food_id>', FoodDetailApi.as_view(), name='food-detail-api'),
    path('user_food_list', UserFoodListApi.as_view(), name='user-food-list-api')
]