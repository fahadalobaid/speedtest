from django.db import models

class Speedtest(models.Model):
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
   

