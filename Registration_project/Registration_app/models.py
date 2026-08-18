from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=100)

    def __str__(self):
        return self.username