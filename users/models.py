from django.db import models
from django.utils import timezone

# Create your models here.

class Eficacia_global(models.Model):
    tramo = models.CharField(max_length=10)
    porcentaje = models.DecimalField(max_digits=4,decimal_places=2)
    fecha = models.DateTimeField(default = timezone.now)
