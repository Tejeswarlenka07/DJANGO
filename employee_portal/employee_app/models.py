from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    emp_salary = models.FloatField()
    emp_address = models.CharField(max_length=200)

    def __str__(self):
        return self.emp_name
