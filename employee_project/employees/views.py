from django.shortcuts import render,redirect
from .models import Employees

# Create your views here.
def employee_list(request):
    employees=Employees.objects.all()
    return render(request,'employees/employee_list.html',{'employees': employees})
def add_employee(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        salary=request.POST['salary']

        employee=Employees.objects.create(name=name,email=email,phone=phone,department=department,salary=salary)
        return redirect('employee_list')

    return render(request,'add_employee.html')

def edit_employee(request, employee_id):
    employee = Employees.objects.get(id=employee_id)

    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']

        employee.save()

        return redirect('employee_list')

    return render(
        request,
        'employees/edit_employee.html',
        {'employee': employee}
    )

def delete_employee(request, employee_id):
    employee = Employees.objects.get(id=employee_id)
    employee.delete()
    return redirect('employee_list')