from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Food, UserFoodList
from django.contrib.auth.models import User
from utils.get_ip import get_user_ip


def index(request):
    user_search = request.POST.get('search_food')
    search_food = Food.objects.filter(name=user_search)
    
    ip = get_user_ip(request=request)
    user, create = User.objects.get_or_create(username=ip)

    user_food = UserFoodList.objects.filter(user=user)
    calorie = []
    protin = []
    for f in user_food:
        calorie.append(f.food.calorie)
        protin.append(f.food.protein)
    
    foods = Food.objects.all()[:10]

    return render(request, 'home/index.html', {'search_food':search_food, 'foods':foods, 'user_calorie':sum(calorie), 'user_protin':sum(protin)})


def user_food_list(request):
    ip = get_user_ip(request=request)
    user, create = User.objects.get_or_create(username=ip)
    user_food = UserFoodList.objects.filter(user=user)
    calorie = []
    protin = []
    for f in user_food:
        calorie.append(f.food.calorie)
        protin.append(f.food.protein)

    return render(request, 'home/user_food_list.html', {'user_food_list':user_food, 'user_calorie':sum(calorie), 'user_protin':sum(protin)})


def food_detail(request, food_id):
    ip = get_user_ip(request=request)
    user, create = User.objects.get_or_create(username=ip)

    if request.method == 'GET':
        food = Food.objects.filter(id=food_id).first()

        user_food_list = UserFoodList.objects.filter(food=food, user=user)

        return render(request, 'home/food_detail.html', {'food':food, 'user_food_list':user_food_list})
    
    elif request.method == 'POST':
        add_food = request.POST.get('add_food')
        if add_food:
            food = Food.objects.filter(name=add_food).first()
            c_food = UserFoodList.objects.create(food=food, user=user)
        
        remove_food = request.POST.get('remove_food')
        if remove_food:
            food = Food.objects.filter(name=remove_food).first()
            r_food = UserFoodList.objects.filter(user=user, food=food).delete()

        return redirect('user_food_list')