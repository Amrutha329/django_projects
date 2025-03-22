

# Create your views here.
from django.shortcuts import render

def student_list(request):
    students = [
        {'name': 'Manasa', 'marks': 85},
        {'name': 'Priya', 'marks': 40},
        {'name': 'Sreeja', 'marks': 75},
        {'name': 'Bhavana', 'marks': 90},
    ]
    passing_marks = 50  # Define passing marks threshold
    return render(request, 'annualapp/student_list.html', {'students': students, 'passing_marks': passing_marks})

