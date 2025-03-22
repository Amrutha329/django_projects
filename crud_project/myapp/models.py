from django.db import models
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    eid=models.IntegerField()

