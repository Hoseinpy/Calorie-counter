from rest_framework import serializers
from home.models import Food, UserFoodList


class FoodListSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

    
class UserFoodSeralizer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField()
    
    class Meta:
        model = UserFoodList
        fields = ['food']

    def get_food(self, obj):
        return obj.food.name


class AddFoodSeralizer(serializers.Serializer):
    add = serializers.ChoiceField(choices={'add':'Add'})


class RemoveFoodSeralizer(serializers.Serializer):
    remove = serializers.ChoiceField(choices={'remove':'Remove'})