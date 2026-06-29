from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}'
    
    
