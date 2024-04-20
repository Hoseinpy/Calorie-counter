from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=100)
    calorie = models.IntegerField()
    protein = models.FloatField(null=True)

    def __str__(self) -> str:
        return self.name
    

class UserFoodList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.food}'