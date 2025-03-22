from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})

def insert(request):
    if request.method == "POST":
        ename = request.POST['ename']
        email = request.POST['email']
        phone = request.POST['phone']
        eid = request.POST['eid']
        Employee.objects.create(ename=ename, email=email, phone=phone, eid=eid)
        return redirect('index')
    return render(request, 'insert.html')

def update_view(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        emp.ename = request.POST['ename']
        emp.email = request.POST['email']
        emp.phone = request.POST['phone']
        emp.eid = request.POST['eid']
        emp.save()
        return redirect('index')
    return render(request, 'update.html', {'emp': emp})

def delete(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('index')