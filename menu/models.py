from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=120)
    
    def __str__(self):
        return self.title

class Dishes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=245)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dishes = models.ForeignKey(Dishes, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
