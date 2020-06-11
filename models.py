from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True)
    link=models.URLField(max_length=250, null=True)
    price=models.FloatField(null=True)
    period=models.DateField(null=True)

    def __str__(self):
        return '%s %s %s %s'%(self.user, self.name, self.price, self.period)
        


