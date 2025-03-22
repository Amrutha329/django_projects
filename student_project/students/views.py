
from django.shortcuts import render, HttpResponse
from .models import Student

def add_student(request):
    student = Student(name="John Doe", age=22, email="johndoe@example.com")
    student.save()
    return HttpResponse("Student record added successfully!")

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "Amrutha", "age": 17 , "email": "ammu@example.com"},
        {"name": "Manasa", "age": 18, "email": "manasa@example.com"},
        {"name": "Sreeja", "age": 21, "email": "sreeja@example.com"},
        {"name": "Priya", "age": 20, "email": "priya@example.com"},
    ]
    return render(request, 'students/student_list2.html', {'students': students})

