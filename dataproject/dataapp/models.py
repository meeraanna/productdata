from django.db import models

# Create your models here.
class DataModel(models.Model):
    API_WELL_NUMBER=models.CharField(max_length=250)
    OIL = models.CharField(max_length=250)
    GAS = models.CharField(max_length=250)
    BRINE = models.CharField(max_length=250)

    def __str__(self):
       return self.API_WELL_NUMBER