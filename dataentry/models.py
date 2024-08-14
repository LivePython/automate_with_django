from django.db import models


# Create your models here.
class Student(models.Model):
    roll_num = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name
    