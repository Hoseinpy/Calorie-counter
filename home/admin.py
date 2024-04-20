from django.contrib import admin
from .models import Food, UserFood


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'calorie']



@admin.register(UserFood)
class UserFoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'food']