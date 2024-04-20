from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from home.models import Food, UserFoodList
from .seralizers import FoodListSeralizer, UserFoodSeralizer, AddFoodSeralizer, RemoveFoodSeralizer
from django.contrib.auth.models import User
from utils.get_ip import get_user_ip
from django.shortcuts import get_object_or_404
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator


class FoodListApi(generics.ListAPIView):
    permission_classes = [AllowAny]

    queryset = Food.objects.all()[:10]
    serializer_class = FoodListSeralizer


@method_decorator(ratelimit(key='ip', rate='60/m'), name='dispatch')
class FoodDetailApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, food_id):

        # get user or create with ip
        ip = get_user_ip(request=request)
        user, create = User.objects.get_or_create(username=ip)

        food = get_object_or_404(Food, id=food_id)
        seralizer = FoodListSeralizer(food)

        return Response(seralizer.data, status.HTTP_200_OK)

    def post(self, request, food_id):

        # get user or create with ip
        ip = get_user_ip(request=request)
        user, create = User.objects.get_or_create(username=ip)

        food = get_object_or_404(Food, id=food_id)

        # get user_list_food and check food for user_list exists or not
        if user_list_food := UserFoodList.objects.filter(user=user, food=food):
            serializer = RemoveFoodSeralizer(data=request.data)
            if serializer.is_valid():
                user_list_food.delete()
                return Response({'message': 'successfuly, remove'})
            
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        # if food is not exists for user can add to user_food_list
        else:
            serializer = AddFoodSeralizer(data=request.data)
            if serializer.is_valid():
                add_food = UserFoodList.objects.create(user=user, food=food)
                return Response({'message': 'successfuly, add'})
            
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    
class UserFoodListApi(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserFoodSeralizer

    def get_queryset(self):

        ip = get_user_ip(request=self.request)
        user, create = User.objects.get_or_create(username=ip)

        user_list_food = UserFoodList.objects.filter(user=user)
        return user_list_food