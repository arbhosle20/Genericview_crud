from django.db import models

class Laptop(models.Model):
    company = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    ram = models.IntegerField()
    rom = models.IntegerField()
    processor = models.CharField(max_length=50)
    price = models.FloatField(blank=True)
    weight = models.FloatField(blank=True)


# Create your models here.
