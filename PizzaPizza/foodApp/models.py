from django.db import models

# Create your models here.
class Pizzas(models.Model):
    name = models.CharField(max_length = 40, primary_key=True)
    description = models.CharField(max_length=200)
    price= models.DecimalField(decimal_places=2, max_digits=9)
    image = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Custom(models.Model):
    customId = models.AutoField(primary_key=True)
    toppings = models.CharField
    customPrice= models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self) -> str:
        return self.id
   

   



