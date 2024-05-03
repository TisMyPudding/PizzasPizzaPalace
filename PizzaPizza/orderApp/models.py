from django.db import models
from foodApp.models import Pizzas, Custom
from userApp.models import User

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    standard= models.ForeignKey(Pizzas ,blank=True,default=None, on_delete=models.CASCADE)#custom if not standard
    custom=models.ForeignKey(Custom,blank=True,default=None, on_delete=models.CASCADE)#standard if not custom
