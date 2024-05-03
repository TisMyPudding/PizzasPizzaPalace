from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30,unique=True, primary_key=True)
    password=models.CharField(max_length=40)
    name=models.CharField(max_length=30)
    card=models.BigIntegerField
    address=models.CharField(max_length=100)
    rewardPoints=models.PositiveIntegerField