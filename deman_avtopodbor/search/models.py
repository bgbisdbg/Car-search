from django.db import models



class CarBrand(models.Model):
    name = models.CharField(max_length=64, unique=True)


class CarModel(models.Model):
    name = models.CharField(max_length=64)
    year = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    brand = models.ForeignKey(to=CarBrand, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)
