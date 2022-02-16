
from django import forms
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from Python_web_basics_projects.employees.models import Department, Employee


class EmployeeForm(forms.Form):
    firs_name = forms.CharField(
        max_length=30,
    )

    last_name = forms.CharField(
        max_length=40,
    )


def home(request):

    context = {
        'employee_form': EmployeeForm(),
    }
    return render(request, 'index.html', context)


def list_departments(request):
    # department = Department(
    #     name='NewDepartment'
    # )
    # department.save()

    context = {
        'departments': Department.objects.all(),
        'employees': Employee.objects.all()
    }
    return render(request, 'list_departments.html', context)


def department_details(request):
    employee = Employee()
    context = {
        'employee': Employee.objects.all(),
        'department': Department.objects.all(),
    }
    return render(request, 'list_departments.html', context)
