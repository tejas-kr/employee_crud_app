from django.shortcuts import redirect, render

from .models import Employee

def index(req):
    return render(req, 'index.html')

def add_new_employee(req):
    if req.method == "POST":
        employee = Employee()
        employee.name = req.POST["employee_name"]
        employee.salary = req.POST["employee_salary"]
        employee.save()
        return redirect('index')

def show_all_employees(req):
    employees = Employee.objects.all()
    context = {}
    context["employees"] = employees
    return render(req, "show_all_employees.html", context)

def edit_employee(req, id):
    id = int(id)
    emp = Employee.objects.get(pk=id)
    if req.method == "GET":
        context = {
            "employee": emp
        }
        return render(req, "edit_employee.html", context)

def edit_employee_save(req):
    if req.method == "POST":
        id = req.POST['employee_id']
        id = int(id)
        e = Employee.objects.get(pk=id)
        e.name = req.POST["employee_name"]
        e.salary = req.POST["employee_salary"]
        e.save()
        
        return redirect('show_all_employees')

def delete_employee(req, id):
    if req.method == "GET":
        id = int(id)
        e = Employee.objects.get(pk=id)
        e.delete()

        return redirect("show_all_employees")
