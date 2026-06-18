from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.name}'
    
    
