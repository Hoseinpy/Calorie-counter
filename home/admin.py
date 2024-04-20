from django.contrib import admin
from .models import Food, UserFoodList


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'calorie']



@admin.register(UserFoodList)
class UserFoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'food']