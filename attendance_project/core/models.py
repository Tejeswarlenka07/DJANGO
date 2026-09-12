from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    total_classes = models.IntegerField(default=0)
    classes_attended = models.IntegerField(default=0)

    @property
    def attendance_percentage(self):
        if self.total_classes == 0:
            return 0

        return round((self.classes_attended / self.total_classes) * 100, 1)

    def __str__(self):
        return self.name