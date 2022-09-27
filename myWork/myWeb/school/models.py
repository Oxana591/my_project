from django.db import models
class Student(models.Model):
   name = models.CharField(max_length=20)
   lastname = models.CharField(max_length=20)
   post = models.TextField(max_length=50)
    
   def __str__(self):
        return f("{self.id} {self.name} {self.lastname} -  {self.post} ")
# Create your models here.
