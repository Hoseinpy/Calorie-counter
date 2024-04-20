from django.urls import path
from .views import index, user_food_list, food_detail


urlpatterns = [
    path('', index, name='index-page'),
    path('user_food_list', user_food_list, name='user_food_list'),
    path('food/<int:food_id>', food_detail, name='food-detail')
]
