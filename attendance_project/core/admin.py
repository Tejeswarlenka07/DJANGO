from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'classes_attended',
        'total_classes',
        'attendance_percentage'
    )