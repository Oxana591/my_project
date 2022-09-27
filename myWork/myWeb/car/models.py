from django.db import models

# Create your models here.
class car(models.Model):
    name=models.CharField(max_length=20)

class car_foto(models.Model):
    foto_id=models.IntegerField()
    foto=models.TextField(max_length=255)