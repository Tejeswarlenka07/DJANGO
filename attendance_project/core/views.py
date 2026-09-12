from django.shortcuts import render, redirect
from .models import Student


def dashboard(request):
    students = Student.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student_id")
        status = request.POST.get("status")

        student = Student.objects.get(id=student_id)

        student.total_classes += 1

        if status == "present":
            student.classes_attended += 1

        student.save()

        return redirect('dashboard')

    return render(request, 'core/dashboard.html', {
        'students': students
    })