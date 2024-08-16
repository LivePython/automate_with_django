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
    
class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    salary = models.FloatField()
    retirement = models.FloatField()
    other_benefits = models.FloatField()
    total_benefits = models.FloatField()
    total_compensation = models.FloatField()

    def __str__(self):
        return self.employee_name+' - '+ self.designation+' - '+ f'${self.salary}'