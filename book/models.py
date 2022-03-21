from django.db import models
from base_user.models import Main_User, Address
from main.models import Tovar

class Liked(models.Model):
    user = models.ForeignKey(Main_User, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)

class Box(models.Model):
    user = models.ForeignKey(Main_User, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(default=1)

class Book(models.Model):
    box = models.ManyToManyField(Box)
    user = models.ForeignKey(Main_User, on_delete=models.CASCADE)
    delivery_time = models.IntegerField()
    general_sum = models.IntegerField()
    status = models.CharField(max_length=30, default="Progress")
